import chromadb
from chromadb.config import Settings

def setup_chroma():
    client = chromadb.Client(Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory="./chroma_db"
    ))

    # Create a collection for resumes if it doesn't exist
    try:
        collection = client.get_collection("resumes")
    except ValueError:
        collection = client.create_collection("resumes")

    print("Chroma DB setup complete.")

if __name__ == "__main__":
    setup_chroma()