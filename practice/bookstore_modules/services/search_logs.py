from pymongo import MongoClient
from collections import Counter

client = MongoClient(
    "mongodb://ich_editor:verystrongpassword"
    "@mongo.itcareerhub.de/?readPreference=primary"
    "&ssl=false&authMechanism=DEFAULT&authSource=ich_edit"
)

collection = client["ich_edit"]["bookstore_logs_searches"]


def log_search(query):
    if query.strip():
        collection.insert_one({"query": query.strip().lower()})


def show_popular_queries():
    queries = [doc["query"] for doc in collection.find() if doc.get("query")]

    counter = Counter(queries)
    top = counter.most_common(5)

    if not top:
        print("No search data found.")
        return

    print("Most frequent search queries:")
    for i, (q, count) in enumerate(top, 1):
        print(f"{i}. {q} — {count} times")
