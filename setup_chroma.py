import chromadb
import pandas as pd
from chromadb.config import Settings
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

import config

client = chromadb.Client(
    Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory="db",
    )
)
collection = client.create_collection(
    name="reviews",
    embedding_function=OpenAIEmbeddingFunction(
        api_key=config.OPENAI_KEY,
    ),
)


df = pd.read_csv("IMDB Dataset.csv.zip")
docs = df["review"].tolist()

# Sample the shortest 100 documents
docs = sorted(docs, key=lambda x: len(x))[:100]

collection.add(
    documents=docs,
    ids=[str(i) for i in range(len(docs))],
)

print(collection.query(query_texts=["Shit movie. Hate it."]))
