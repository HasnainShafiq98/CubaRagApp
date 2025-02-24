import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec  # ✅ Updated Pinecone import
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings  # ✅ Using MistralAI embeddings
from langchain_pinecone import PineconeVectorStore  # ✅ Updated Pinecone import

load_dotenv("config.env")
pinecone_api_key = os.getenv("PINECONE_API_KEY")
mistral_api_key = os.getenv("MISTRALAI_API_KEY")
hf_token = os.getenv("HUGGINGFACE_TOKKEN")

if not hf_token:
    raise ValueError("❌ Hugging Face token (`HF_TOKEN`) is missing! Set it in your `.env` file.")

os.environ["HF_TOKEN"] = hf_token  # ✅ Set Hugging Face Token in environment

pc = Pinecone(api_key=pinecone_api_key)

index_name = "cubabuddy"

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=1024,  # Mistral embeddings use 1024 dimensions
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")  # Adjust region as needed
    )

index = pc.Index(index_name)

def load_data(file_path):
    loader = TextLoader(file_path)
    return loader.load()

def split_text(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return text_splitter.split_documents(documents)

embeddings = MistralAIEmbeddings(model="mistral-embed", api_key=mistral_api_key)

vector_store = PineconeVectorStore(embedding=embeddings, index=index)

def store_in_pinecone(chunks):
    vector_store.add_documents(documents=chunks)

def process_data(file_path):
    docs = load_data(file_path)
    chunks = split_text(docs)
    store_in_pinecone(chunks)
    print("✅ Data successfully stored in Pinecone with MistralAI embeddings!")

process_data("cuba_info.txt")  # Replace with your actual data file