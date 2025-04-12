# LLM calling chooose the model with 

# 1. Extended context window: Suitable for processing larger chunks if needed.
# 2. High reasoning ability: For generating in-depth and insightful questions.
# 3. Scalability: Can be deployed on local/high‑performance setups.

import json 
from chunking import chunk_text
import random
import concurrent.futures
from langchain_ollama import OllamaLLM


# -------------------------
# LLM Question Generation
# -------------------------
def call_ollama_llm(prompt: str) -> str:
    """
    :param prompt: The prompt text to send to the LLM.
    :return: JSON string response from the LLM.
    """
    # Integration point for your Ollama LLM: 
    # For example, using a Python SDK or CLI to get the output.

    llm = OllamaLLM(model="llama3.1", temperature=0.3)
    response = llm.invoke(prompt)
    print(f"LLM Response: {response}")
    return response

def generate_questions_from_chunk(chunk: str) -> list:
    prompt = f"""
You are an expert educator. Read the following passage and generate 3 high-quality, insightful single choice questions that cover various aspects of the content.
Please return the output strictly in JSON format (no extra text or explanation) exactly as shown in this example:

Example JSON output:
{{
  "questions": [
    {{
      "Question": "What is the sample question?",
      "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
      "Answer": "Option 1",
      "Explanation": "This is why Option 1 is correct."
    }},
    {{
      "Question": "What is another sample question?",
      "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
      "Answer": "Option 3",
      "Explanation": "This is why Option 3 is correct."
    }},
    {{
      "Question": "What is the third sample question?",
      "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
      "Answer": "Option 4",
      "Explanation": "This is why Option 4 is correct."
    }}
  ]
}}

Do not output any additional text. 

Passage:
"{chunk}"
"""
    response = call_ollama_llm(prompt)
    try:
        result = json.loads(response)
        return result.get("questions", [])
    except Exception as e:
        print(f"Error parsing LLM response: {e}")
        return []



def generate_all_questions(pages: list) -> list:
    """
    Processes all pages in parallel to generate candidate questions.
    :param pages: List of page texts extracted from the PDF.
    :return: Flattened list of candidate questions from all chunks.
    """
    candidate_questions = []
    all_chunks = []
    
    # Build a list of all text chunks
    for page in pages:
        chunks = chunk_text(page)
        all_chunks.extend(chunks)

    # Parallel processing using ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Submit all chunk processing tasks
        futures = [executor.submit(generate_questions_from_chunk, chunk) for chunk in all_chunks]
        for future in concurrent.futures.as_completed(futures):
            candidate_questions.extend(future.result())
    
    return candidate_questions



def randomize_questions(candidate_questions: list, desired_count: int) -> list:
    """
    Randomly selects a desired number of questions from the candidate pool.
    :param candidate_questions: List of candidate questions.
    :param desired_count: Number of questions required.
    :return: Randomized list of questions.
    """
    if len(candidate_questions) <= desired_count:
        return candidate_questions
    return random.sample(candidate_questions, desired_count)
