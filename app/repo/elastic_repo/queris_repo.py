from app.settings.elastic_config import elastic_client

def search_in_all(index, query):
    try:
        body = {
            "query": {
                "match": {
                    "summary": query
                }
            }
        }

        response = elastic_client.search(index=index, body=body)
        return response["hits"]["hits"]

    except Exception as e:
        print(f"Error executing search: {e}")
        return []


def search_in_history(index, query):
    try:
        body = {
            "query": {
                "bool": {
                    "must": [
                        {"match": {"summary": query}},
                        {"match": {"new": False}}
                    ]
                }
            }
        }

        response = elastic_client.search(index=index, body=body)
        return response["hits"]["hits"]

    except Exception as e:
        print(f"Error executing search: {e}")
        return []


def search_in_news(index, query):
    try:
        body = {
            "query": {
                "bool": {
                    "must": [
                        {"match": {"summary": query}},
                        {"match": {"new": True}}
                    ]
                }
            }
        }

        response = elastic_client.search(index=index, body=body)
        return response["hits"]["hits"]

    except Exception as e:
        print(f"Error executing search: {e}")
        return []




def search_between_dates(index, query, start_date, end_date):
    try:
        body = {
            "query": {
                "bool": {
                    "must": [
                        {"match": {"summary": query}},
                        {"range": {"date": {"gte": start_date, "lte": end_date}}}
                    ]
                }
            }
        }

        response = elastic_client.search(index=index, body=body)
        return response["hits"]["hits"]

    except Exception as e:
        print(f"Error executing search: {e}")
        return []

