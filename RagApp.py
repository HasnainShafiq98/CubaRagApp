import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_mistralai import MistralAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.chains import RetrievalQA
from langsmith import traceable

load_dotenv("config.env")

pinecone_api_key = os.getenv("PINECONE_API_KEY")
mistral_api_key = os.getenv("MISTRALAI_API_KEY")
hf_token = os.getenv("HUGGINGFACE_TOKKEN")

if not pinecone_api_key:
    raise ValueError("❌ Pinecone API key is missing! Ensure it's set in your `.env` file.")

if not mistral_api_key:
    raise ValueError("❌ MistralAI API key is missing! Ensure it's set in your `.env` file.")

if not hf_token:
    raise ValueError("❌ Hugging Face API token is missing! Ensure it's set in your `.env` file.")

os.environ["HF_TOKEN"] = hf_token
pc = Pinecone(api_key=pinecone_api_key)
index_name = "cubabuddy"


if index_name not in pc.list_indexes().names():
    print(f"🔍 Index '{index_name}' not found. Creating it now...")
    pc.create_index(
        name=index_name,
        dimension=1024,  # Mistral embeddings use 1024 dimensions
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")  # Adjust region as needed
    )
    print(f"✅ Index '{index_name}' created successfully!")

index = pc.Index(index_name)
embeddings = MistralAIEmbeddings(model="mistral-embed", api_key=mistral_api_key)
vector_store = PineconeVectorStore(embedding=embeddings, index=index)
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 5})
llm = ChatMistralAI(api_key=mistral_api_key, model="mistral-small")


@traceable
def get_rag_response(query):
    qa_chain = RetrievalQA.from_chain_type(llm, retriever=retriever)
    return qa_chain.run(query)