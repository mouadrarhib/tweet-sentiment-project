SELECT sentiment, COUNT(*) as count FROM tweets_sentiment GROUP BY sentiment;

SELECT * FROM tweets_sentiment WHERE polarity > 0.5 LIMIT 10;

SELECT * FROM tweets_sentiment WHERE sentiment = 'Négatif' ORDER BY polarity ASC LIMIT 10;


