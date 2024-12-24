from elasticsearch import Elasticsearch




cloud_id =  "8dd91d02fa444e05bb1e12b148ef1a18:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvOjQ0MyRjZGFjNzk0NjNjNzU0MmUzYTkyNTM2YWEwNTVjYWQyMiQ4MWNiYjdkODE2ZDY0MWY4YTAxMzQyNjI4YzhkYzdlYw=="
username = "elish"
password = "5nEhfViA3yaFRc9"


# יצירת חיבור
elastic_client = Elasticsearch(
    cloud_id=cloud_id,
    basic_auth=(username, password)
)
# elastic
# elastic_client = Elasticsearch(['http://localhost:9200'])