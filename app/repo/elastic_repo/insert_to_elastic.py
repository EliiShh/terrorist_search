from typing import List, Dict
from app.db.elastic.database import create_index
from app.settings.elastic_config import elastic_client


def insert_many_descriptions(description:List[Dict]) -> None:
    create_index("events")
    try:
        for x in description:
            x["new"] = True
            elastic_client.index(index="events", body=x)
        print(len(description), "in elastic")
    except Exception as e:
        print(e)


