from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
import re

def clean_text(text):
    if text is None: # Handle None values
        return ""
    text = re.sub(r"@\w+", "", text)  # Remove mentions
    text = re.sub(r"#\w+", "", text)  # Remove hashtags
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # Remove punctuation and numbers
    text = text.lower()  # Convert to lowercase
    text = text.strip()  # Remove leading/trailing whitespace
    return text

clean_text_udf = udf(clean_text, StringType())

def preprocess_tweets(df):
    """
    Nettoie le texte des tweets en utilisant PySpark.
    """
    # Assurez-vous que la colonne des tweets est bien 'text' ou 'tweet'
    # Le dataset Sentiment140 a une colonne 'text' pour le contenu du tweet
    df_cleaned = df.withColumn("cleaned_text", clean_text_udf(df["_c5"]))
    return df_cleaned

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("PreprocessTweets") \
        .getOrCreate()

    # Pour le test, chargez un petit échantillon du dataset
    # Assurez-vous que le chemin est correct pour votre environnement
    try:
        tweets_df = spark.read.csv("/home/ubuntu/tweet-sentiment-project/data/tweets.csv", header=False, inferSchema=True)
        # Le dataset Sentiment140 a la colonne de texte à l'index 5 (_c5)
        processed_df = preprocess_tweets(tweets_df)
        processed_df.select("_c5", "cleaned_text").show(truncate=False)
    except Exception as e:
        print(f"Erreur lors du chargement ou du traitement du fichier: {e}")
    finally:
        spark.stop()


