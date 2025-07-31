# Projet Big Data - Analyse de Sentiments sur les Tweets

Ce projet implémente un pipeline Big Data complet pour l'analyse de sentiments sur des tweets en utilisant Apache Spark, Hadoop HDFS, et Apache Hive. Il utilise le dataset Sentiment140 et TextBlob pour l'analyse de sentiments.

## Structure du Projet

```
tweet-sentiment-project/
├── data/
│   ├── tweets.csv              # Dataset Sentiment140 (500 lignes)
│   └── cleaned_tweets.csv      # Résultats avec polarité et catégorie
│
├── visuals/
│   ├── sentiments_pie.png      # Graphique camembert
│   └── wordcloud.png           # Nuage de mots
│
├── src/
│   ├── load_data.py            # Chargement des données avec Spark
│   ├── preprocess.py           # Nettoyage de texte avec PySpark
│   ├── sentiment_analysis.py   # Analyse de sentiments avec TextBlob UDF
│   └── visualize.py            # Génération des visualisations
│
├── hive/
│   ├── create_table.hql        # Script de création de table Hive
│   └── sample_queries.hql      # Exemples de requêtes SQL
│
├── docker/
│   ├── docker-compose.yml      # Configuration Docker pour Hadoop/Spark/Hive
│   └── hadoop-hive.env         # Variables d'environnement
│
│
│
├── README.md                   # Ce fichier
└── requirements.txt            # Dépendances Python
```

## Prérequis

### Logiciels requis
- Python 3.7+
- Docker et Docker Compose
- Java 8 (pour Spark)

### Dépendances Python
Installez les dépendances avec :
```bash
pip install -r requirements.txt
```

## Installation et Configuration

### 1. Cloner le projet
```bash
git clone <url-du-projet>
cd tweet-sentiment-project
```

### 2. Démarrer l'environnement Big Data avec Docker
```bash
cd docker
docker-compose up -d
```

Cela démarre les services suivants :
- Hadoop HDFS (NameNode, DataNode)
- YARN (ResourceManager, NodeManager)
- Apache Spark (Master, Worker)
- Apache Hive (Server, Metastore)
- PostgreSQL (pour le metastore Hive)

### 3. Vérifier que les services sont démarrés
- Hadoop NameNode : http://localhost:9870
- Spark Master : http://localhost:8080
- Hive Server : port 10000

## Utilisation

### 1. Exécuter le pipeline de traitement

#### Prétraitement des données
```bash
cd src
python3 preprocess.py
```

#### Analyse de sentiments
```bash
python3 sentiment_analysis.py
```

#### Génération des visualisations
```bash
python3 visualize.py
```

### 2. Utiliser Hive pour les requêtes SQL

#### Créer la table Hive
```bash
# Se connecter au conteneur Hive
docker exec -it hive-server bash

# Exécuter le script de création de table
hive -f /path/to/hive/create_table.hql
```

#### Exécuter des requêtes d'exemple
```bash
hive -f /path/to/hive/sample_queries.hql
```

### 3. Visualiser les résultats

Les visualisations sont générées dans le répertoire `visuals/` :
- `sentiments_pie.png` : Distribution des sentiments
- `wordcloud.png` : Nuage de mots des termes les plus fréquents

## Architecture Technique

### Technologies utilisées
- **Apache Spark** : Traitement distribué des données
- **Hadoop HDFS** : Stockage distribué
- **Apache Hive** : Requêtes SQL sur les données
- **TextBlob** : Analyse de sentiments
- **Docker** : Conteneurisation des services
- **Python** : Langage de programmation principal

### Pipeline de traitement
1. **Chargement** : Lecture du dataset Sentiment140 depuis HDFS
2. **Prétraitement** : Nettoyage du texte (suppression des mentions, URLs, etc.)
3. **Analyse** : Application de TextBlob via UDF Spark pour déterminer la polarité
4. **Stockage** : Sauvegarde des résultats dans HDFS
5. **Visualisation** : Génération de graphiques et nuages de mots

## Dataset

Le projet utilise le dataset **Sentiment140**, une collection de 1,6 million de tweets annotés. Pour ce projet de démonstration, un échantillon de 500 tweets est utilisé.

**Format du dataset :**
- Colonne 0 : Polarité (0 = négatif, 4 = positif)
- Colonne 5 : Texte du tweet

## Résultats

Le pipeline produit :
- Un fichier CSV avec les tweets nettoyés et leur analyse de sentiment
- Un graphique camembert montrant la distribution des sentiments
- Un nuage de mots des termes les plus fréquents
- Une table Hive interrogeable via SQL

## Dépannage

### Problèmes courants

1. **Docker ne démarre pas** : Vérifiez que Docker est installé et démarré
2. **Erreurs de mémoire Spark** : Ajustez les paramètres de mémoire dans `hadoop-hive.env`
3. **Problèmes de connexion Hive** : Vérifiez que PostgreSQL est démarré

### Logs
Consultez les logs des conteneurs :
```bash
docker-compose logs [nom-du-service]
```

## Limitations

- Le projet utilise un échantillon réduit du dataset pour la démonstration
- L'environnement Docker est configuré pour un usage local/développement
- TextBlob peut avoir des limitations pour certaines nuances linguistiques

## Perspectives d'amélioration

- Intégration de modèles de NLP plus avancés (BERT, RoBERTa)
- Support multilingue
- Traitement en temps réel avec Spark Streaming
- Déploiement sur un cluster cloud

## Auteur

Projet développé par Manus AI dans le cadre d'une démonstration de pipeline Big Data pour l'analyse de sentiments.

## Licence

Ce projet est fourni à des fins éducatives et de démonstration.

