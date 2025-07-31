from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import FloatType, StringType
from textblob import TextBlob
from preprocess import preprocess_tweets # Importer la fonction de prétraitement

def get_polarity(text):
    """
    Retourne la polarité du sentiment d'un texte.
    """
    return TextBlob(text).sentiment.polarity

def get_sentiment(polarity):
    """
    Catégorise la polarité en 'Positif', 'Neutre' ou 'Négatif'.
    """
    if polarity > 0:
        return "Positif"
    elif polarity == 0:
        return "Neutre"
    else:
        return "Négatif"

get_polarity_udf = udf(get_polarity, FloatType())
get_sentiment_udf = udf(get_sentiment, StringType())

def analyze_sentiments(df):
    """
    Analyse les sentiments des tweets et ajoute la polarité et la catégorie.
    """
    df_with_polarity = df.withColumn("polarity", get_polarity_udf(df["cleaned_text"]))
    df_with_sentiment = df_with_polarity.withColumn("sentiment", get_sentiment_udf(df_with_polarity["polarity"]))
    return df_with_sentiment

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("SentimentAnalysis") \
        .getOrCreate()

    try:
        # Charger et prétraiter les données
        tweets_df = spark.read.csv("/home/ubuntu/tweet-sentiment-project/data/tweets.csv", header=False, inferSchema=True)
        processed_df = preprocess_tweets(tweets_df)

        # Analyser les sentiments
        final_df = analyze_sentiments(processed_df)
        final_df.select("cleaned_text", "polarity", "sentiment").show(truncate=False)

        # Sauvegarder les résultats dans un fichier CSV
        final_df.write.csv("/home/ubuntu/tweet-sentiment-project/data/cleaned_tweets.csv", header=True, mode="overwrite")

    except Exception as e:
        print(f"Une erreur est survenue: {e}")
    finally:
        spark.stop()


