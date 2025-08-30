# 📊 Agentic AI Financial Assistant  

A simple learning project exploring **Agentic AI** using **PhiData** and **Claude 3.5 Sonnet**.  
This project demonstrates how multiple AI agents can collaborate to fetch and summarize financial data in real time.  

---

## 🚀 Features  
- 🔍 **Web Search Agent**  
  - Powered by DuckDuckGo.  
  - Fetches real-time information with sources for credibility.  

- 📊 **Finance Agent**  
  - Uses PhiData's **YFinanceTools**.  
  - Provides stock prices, analyst recommendations, company fundamentals, and the latest news.  
  - Displays results in structured tables.  

- 🤝 **Multi-AI Agent**  
  - Combines multiple agents for seamless collaboration.  
  - Example: Summarizes analyst recommendations and shares the latest news for **NVIDIA**.  

---

## 🛠 Tech Stack  
- **PhiData** – Agent orchestration & tools  
- **Claude 3.5 Sonnet (Anthropic)** – LLM reasoning  
- **YFinanceTools** – Financial data retrieval  
- **DuckDuckGo Tool** – Real-time web search  
- **Python** – Core programming  

---

## 📂 Project Structure  
├── finance_agent.py # Main script with agents

├── requirements.txt # Dependencies

└── README.md # Project documentation

Install dependencies:

pip install -r requirements.txt


Run the project:

python finance_agent.py
