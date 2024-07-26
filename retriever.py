from dotenv import load_dotenv
import os
from llama_index.core import Settings, VectorStoreIndex, StorageContext
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb

class Retriever:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        self.api_key = os.getenv('GEMINI_API_KEY')
        
        if not self.api_key:
            raise ValueError("API key for Gemini model is not set.")
        
        # Initialize the Gemini embedding model
        self.embedding_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
        
        # Initialize the Gemini language model
        self.llm = Gemini(api_key=self.api_key, model_name="models/gemini-pro")
        
        # Set Global settings
        Settings.llm = self.llm
        Settings.embed_model = self.embedding_model

        # Load the ChromaDB client
        self.client = chromadb.PersistentClient(path='./chroma_db')
        
        # Fetch the collection from ChromaDB
        self.chroma_collection = self.client.get_collection("quickstart")
        
        # Fetch the vector store from the collection
        self.vector_store = ChromaVectorStore(chroma_collection=self.chroma_collection)
        
        # Create a storage context
        self.storage_context = StorageContext.from_defaults(vector_store=self.vector_store)
        
        # Get the index from the vector store
        self.index = VectorStoreIndex.from_vector_store(self.vector_store)

    def generate_answers(self, question):
        query_engine = self.index.as_query_engine()
        return query_engine.query(question)