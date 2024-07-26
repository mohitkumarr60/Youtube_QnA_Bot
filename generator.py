from dotenv import load_dotenv
import os
import chromadb
from llama_index.core import (
    Settings, StorageContext, VectorStoreIndex
)
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore


class Generator:
    def __init__(self, data):
        # Load environment variables
        load_dotenv()
        self.api_key = os.getenv('GEMINI_API_KEY')
        
        # Set embedding and language models
        self.embedding_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
        self.llm = Gemini(api_key=self.api_key, model_name="models/gemini-pro")

        # Load documents
        self.documents = data
        
        # Create a client and a new collection
        self.client = chromadb.PersistentClient(path='./chroma_db')
        self.chroma_collection = self.client.get_or_create_collection("quickstart")

        # Create a vector store
        self.vector_store = ChromaVectorStore(chroma_collection=self.chroma_collection)

        # Create a storage context
        self.storage_context = StorageContext.from_defaults(vector_store=self.vector_store)

        # Set Global settings
        Settings.llm = self.llm
        Settings.embed_model = self.embedding_model

    # Create an index from the documents and save it to the disk
    def generate_embeddings(self):
        self.index = VectorStoreIndex.from_documents(
        self.documents, storage_context=self.storage_context
    )