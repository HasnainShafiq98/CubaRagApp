🇨🇺 Cuba Travel Chatbot

A Retrieval-Augmented Generation (RAG) Chatbot built with MistralAI, Pinecone, and Streamlit to answer travel-related queries about Cuba. This chatbot retrieves relevant travel information from a vector database and generates AI-powered responses using MistralAI.

🚀 Features

MistralAI for Text Generation: Uses mistral-small for high-quality responses.

Pinecone for Vector Storage: Stores and retrieves relevant information efficiently.

Streamlit for UI: Interactive web-based interface for user-friendly interactions.

LangSmith for Observability: Tracks queries and debugging logs for better monitoring.

Data Pipeline & Scraping: Automated data extraction and processing for up-to-date information.
_________________________________________________________________
📂 Project Structure

CubaTravelChatbot/
│── config.env        # (Not uploaded - contains API keys)
│── app.py           # Streamlit frontend
│── rag_chatbot.py   # Chatbot logic with MistralAI & Pinecone
│── data_pipeline.py # Data pipeline for preprocessing & indexing
│── data_scraper.py  # Web scraper for travel-related information
│── requirements.txt # Required dependencies
│── README.md        # Documentation
│── .gitignore       # Prevents sensitive files from being uploaded
_________________________________________________________________
🔧 Setup & Run

1️⃣ Clone the Repository

git clone https://github.com/HasnainShafiq98/CubaRagApp.git
cd CubaRagApp

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Create a config.env File

⚠️ Important: The config.env file is not included in Git for security reasons.

Create a config.env file in the root directory and add:

PINECONE_API_KEY=your-pinecone-api-key

MISTRALAI_API_KEY=your-mistral-api-key

HF_TOKEN=your-huggingface-token

4️⃣ Run the Data Pipeline

python data_pipeline.py

5️⃣ Run the Chatbot Backend

python rag_chatbot.py

6️⃣ Start the Frontend

streamlit run app.py
_________________________________________________________________
🛠 How It Works

🔹 Data Scraping & Pipeline

Web Scraping: data_scraper.py extracts travel-related data from online sources.

Data Preprocessing: data_pipeline.py processes and cleans the data.

Chunk & Embed: Splits text into smaller chunks and generates embeddings using mistral-embed.

Store in Pinecone: Stores embeddings in a vector database for retrieval.

🔹 Query Process

User Query: The user enters a travel-related question.

Retrieve Relevant Chunks: Pinecone retrieves the most relevant travel information.

Generate Response: MistralAI uses the retrieved information to generate an AI-powered response.

Display Response: The final answer is displayed in the Streamlit UI.
_________________________________________________________________
📜 API Keys & Configuration

Environment Variables (Stored in config.env):

PINECONE_API_KEY: API key for Pinecone vector database.


MISTRALAI_API_KEY: API key for MistralAI text generation.


HF_TOKEN: Hugging Face token to download the Mistral tokenizer.

_________________________________________________________________
🎯 Future Improvements

Enhance Retrieval: Use rerankers for better relevance.

Improve UI: Add chat history and a better design.

Expand Knowledge Base: Add more travel-related data sources.

🚀 Enjoy your AI-powered Cuba Travel Chatbot! 🇨🇺
