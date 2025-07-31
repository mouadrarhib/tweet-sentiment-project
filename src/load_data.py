from pyspark.sql import SparkSession

def load_tweets(spark, path):
    """
    Charge le dataset de tweets depuis HDFS.
    """
    df = spark.read.csv(path, header=True, inferSchema=True)
    return df

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("LoadTweets") \
        .getOrCreate()

    # Exemple d'utilisation (à adapter pour HDFS)
    # Pour l'instant, nous allons charger le fichier localement pour le développement
    # et simuler le chargement HDFS plus tard.
    tweets_df = load_tweets(spark, "/home/ubuntu/tweet-sentiment-project/data/tweets.csv")
    tweets_df.show()
    spark.stop()


