# 🧠 MCQ Generator using LLaMA 3.1 + RAG

This project uses **LLaMA 3.1** and a **Retrieval-Augmented Generation (RAG)** approach to automatically generate **Multiple Choice Questions (MCQs)** from large documents. It’s perfect for creating quizzes, practice tests, and educational content.

---

## ✨ Features

- 📄 Splits large documents into smaller chunks
- 🦙 Uses LLaMA 3.1 to generate 3 MCQs per chunk
- ✅ Cleans and validates outputs into structured JSON
- 🔁 Retries generation if invalid output is received
- 🎯 Returns a final set of randomly selected questions

---

## 🧰 Technologies Used

- **LLaMA 3.1**
- **FastAPI** for API Creation 

---

## ⚙️ How It Works

1. **Text Chunking**  
   Long documents are split into smaller chunks that fit within LLaMA’s input size.

2. **MCQ Generation**  
   Each chunk is sent to LLaMA 3.1 with a prompt to generate 3 multiple choice questions in JSON format.

3. **Output Cleaning**  
   The raw response is processed to extract valid JSON data using custom cleaning functions.

4. **Final Question Selection**  
   After collecting valid MCQs from all chunks, a specified number of random questions are selected for the final output.

---

## 🧑‍💻 Usage

```
git clone https://github.com/divyansh89532/Question_Generation.git
```

# Create a virtual Environment 
```
python -m venv .
```

# Installing the dependencies

```
pip install -r requirements.txt
```

# Running the code 
```
uvicorn app:app --reload
```
Then specify the number of questions and select the PDF file. 
