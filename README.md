\# StyleHub AI Customer Support Assistant



A local AI-powered customer support chatbot for a fictional online clothing store. This project uses Retrieval-Augmented Generation (RAG) to answer customer questions using company documents rather than relying entirely on the AI model's general knowledge.



\## Project Overview



The StyleHub AI Customer Support Assistant helps customers find information about:



\- Shipping and delivery

\- Returns and refunds

\- Payment methods and payment issues

\- Product information

\- Frequently asked questions



The assistant searches a company knowledge base, retrieves relevant information, and uses a locally running AI model to generate a response.



When the available information is insufficient, the assistant provides a fallback response rather than intentionally inventing company policies.



\## Features



\- \*\*Document-based answers:\*\* Uses company policy and product documents as its knowledge base.

\- \*\*Semantic search:\*\* Finds relevant information based on the meaning of a customer's question.

\- \*\*RAG architecture:\*\* Supplies retrieved company information to the AI model before generating an answer.

\- \*\*Local AI processing:\*\* Uses Ollama and Qwen to generate responses locally.

\- \*\*Unknown-answer handling:\*\* Directs customers to Customer Support when the knowledge base does not contain sufficient information.

\- \*\*Human support warnings:\*\* Identifies selected questions that may require human attention.

\- \*\*Interactive chat interface:\*\* Built with Streamlit, including suggested questions and chat history.

\- \*\*Persistent vector database:\*\* Stores document embeddings using ChromaDB.

\- \*\*Automated tests:\*\* Uses pytest to test document loading, text splitting, retrieval, and escalation logic.



\## Technologies Used



| Technology | Purpose |

|---|---|

| Python 3.13 | Main programming language |

| Ollama | Local AI model runtime |

| Qwen 3.5 4B | AI response generation |

| Sentence Transformers | Converts text into numerical embeddings |

| all-MiniLM-L6-v2 | Text embedding model |

| ChromaDB | Vector database and semantic search |

| Streamlit | Chat application interface |

| Requests | Communicates with Ollama |

| Pytest | Automated testing |



\## How It Works



The application follows a Retrieval-Augmented Generation (RAG) workflow.



1\. \*\*Document loading:\*\* Reads StyleHub company documents from the `documents/` folder.

2\. \*\*Text splitting:\*\* Divides documents into smaller overlapping chunks.

3\. \*\*Embedding generation:\*\* Converts each text chunk into a numerical representation.

4\. \*\*Vector storage:\*\* Saves embeddings and their corresponding text in ChromaDB.

5\. \*\*Question processing:\*\* Converts a customer's question into an embedding.

6\. \*\*Information retrieval:\*\* Searches ChromaDB for relevant document chunks.

7\. \*\*AI response generation:\*\* Sends the retrieved information and customer question to Qwen through Ollama.

8\. \*\*Response display:\*\* Shows the generated answer in the Streamlit chat interface.



If relevant information cannot be retrieved, the application returns a fallback response.



\## Project Structure



```text

AI-Customer-Support-Assistant/

│

├── app.py

├── requirements.txt

├── README.md

├── .gitignore

│

├── documents/

│   ├── shipping\_policy.txt

│   ├── returns\_refunds\_policy.txt

│   ├── payment\_policy.txt

│   ├── product\_information.txt

│   └── frequently\_asked\_questions.txt

│

├── src/

│   ├── document\_loader.py

│   ├── text\_chunker.py

│   ├── process\_documents.py

│   ├── embedding\_generator.py

│   ├── vector\_store.py

│   ├── ollama\_client.py

│   ├── rag\_engine.py

│   └── escalation.py

│

├── tests/

│   ├── test\_document\_loader.py

│   ├── test\_text\_chunker.py

│   ├── test\_rag\_engine.py

│   └── test\_escalation.py

│

├── data/

└── logs/

```



The `data/` and `logs/` folders contain local application data and are excluded from Git.



\## Installation and Setup



\### 1. Requirements



Before running the project, install:



\- Python 3.13

\- Ollama

\- Git (optional, for version control)



\### 2. Clone the Repository



```bash

git clone YOUR\_GITHUB\_REPOSITORY\_URL

cd AI-Customer-Support-Assistant

```



Replace `YOUR\_GITHUB\_REPOSITORY\_URL` with the repository URL.



\### 3. Create a Virtual Environment



```bash

py -3.13 -m venv .venv

```



Activate it on Windows PowerShell:



```powershell

.\\.venv\\Scripts\\Activate.ps1

```



\### 4. Install Dependencies



```bash

python -m pip install -r requirements.txt

```



\### 5. Download the AI Model



Make sure Ollama is installed and running.



```bash

ollama pull qwen3.5:4b

```



\### 6. Build the Knowledge Base



Generate document embeddings and save them to ChromaDB:



```bash

python -m src.vector\_store

```



This creates the local vector database in `data/chroma\_db/`.



\### 7. Start the Application



```bash

streamlit run app.py

```



Streamlit will provide a local address where you can open the chatbot in your browser.



\## Running Automated Tests



Run the test suite with:



```bash

python -m pytest tests/ -v

```



The current test suite contains \*\*16 automated tests\*\* covering:



\- Document loading

\- Text chunking

\- Relevant information retrieval

\- Rejection of irrelevant information

\- AI response generation using mocked responses

\- Missing-information fallback behavior

\- AI connection failure handling

\- Human support escalation checks



The tests use mocked AI responses where appropriate, so they do not need to generate real Qwen responses.



\## Current Limitations



This project is a local portfolio prototype, not a production customer support system.



\- It does not connect to a real e-commerce platform.

\- It cannot retrieve live order status or inventory information.

\- It does not process refunds, returns, or payments.

\- Human support warnings do not automatically create support tickets or contact staff.

\- AI responses may still contain errors and should be reviewed.

\- The similarity threshold is experimental and has not been validated against a comprehensive evaluation dataset.

\- The application must run locally with Ollama and its required models available.



\## Future Improvements



Possible next steps include:



\- Integrating a real e-commerce platform.

\- Adding order tracking through an authorized API.

\- Creating a customer support ticket workflow.

\- Improving retrieval accuracy through evaluation and tuning.

\- Adding conversation feedback and analytics.

\- Deploying the application to a hosted environment.



\## Project Purpose



This project demonstrates practical skills in Python automation, local AI integration, document processing, semantic search, vector databases, RAG architecture, Streamlit application development, and automated testing.



Created as an AI automation portfolio project using free and locally runnable tools.

