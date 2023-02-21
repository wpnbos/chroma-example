import chromadb
from chromadb.config import Settings

client = chromadb.Client(
    Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory="db",
    )
)
collection = client.get_collection("reviews")

print(collection.count())

print(collection.query(query_texts=["Shit movie. Hate it."]))
