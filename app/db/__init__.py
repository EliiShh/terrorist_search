from elasticsearch import Elasticsearch

from app.settings.elastic_config import elastic_client

# חיבור ל-ElasticSearch
es = elastic_client

# שם האינדקס
index_name = "events"

# בקשה למספר המסמכים באינדקס
response = es.count(index=index_name)

# הצגת כמות המסמכים
print(f"מספר המסמכים באינדקס {index_name}: {response['count']}")
