from pyspark.sql import SparkSession
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

def generate_pie_chart(spark, data_path, output_path):
    """
    Génère un graphique camembert des sentiments.
    """
    df = spark.read.csv(data_path, header=True, inferSchema=True)
    sentiment_counts = df.groupBy("sentiment").count().collect()

    labels = [row["sentiment"] for row in sentiment_counts]
    sizes = [row["count"] for row in sentiment_counts]
    colors = ["#66b3ff", "#99ff99", "#ffcc99"]

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
    plt.title("Distribution des Sentiments")
    plt.axis("equal")
    plt.savefig(output_path)
    plt.close()

def generate_word_cloud(spark, data_path, output_path):
    """
    Génère un nuage de mots à partir des textes nettoyés.
    """
    df = spark.read.csv(data_path, header=True, inferSchema=True)
    text_data = df.select("cleaned_text").rdd.flatMap(lambda x: x).collect()
    text = " ".join(text_data)

    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(output_path)
    plt.close()

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("VisualizeSentiments") \
        .getOrCreate()

    cleaned_tweets_path = "/home/ubuntu/tweet-sentiment-project/data/cleaned_tweets.csv"
    pie_chart_output = "/home/ubuntu/tweet-sentiment-project/visuals/sentiments_pie.png"
    word_cloud_output = "/home/ubuntu/tweet-sentiment-project/visuals/wordcloud.png"

    try:
        generate_pie_chart(spark, cleaned_tweets_path, pie_chart_output)
        print(f"Graphique camembert généré: {pie_chart_output}")

        generate_word_cloud(spark, cleaned_tweets_path, word_cloud_output)
        print(f"Nuage de mots généré: {word_cloud_output}")

    except Exception as e:
        print(f"Erreur lors de la génération des visualisations: {e}")
    finally:
        spark.stop()


