CREATE EXTERNAL TABLE IF NOT EXISTS tweets_sentiment (
    original_text STRING,
    cleaned_text STRING,
    polarity FLOAT,
    sentiment STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ","
STORED AS TEXTFILE
LOCATION "/user/hive/warehouse/tweets_sentiment";


