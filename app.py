import uuid
import os
from fastapi import FastAPI, UploadFile, File
from pdf_utils import extract_pages
import tempfile
from question_generator import generate_all_questions, randomize_questions


# -------------------------
# FastAPI Application
# -------------------------
app = FastAPI()

@app.post("/generate-questions")
async def generate_questions_endpoint(custom_count: int,pdf: UploadFile = File(...)):
    """
    Endpoint to process a PDF file, generate candidate questions in parallel,
    and return a JSON with a randomized set of questions.
    :param pdf: The uploaded PDF file.
    :param custom_count: Custom number of questions desired in the output.
    :return: JSON with generated questions.
    """
    # Save the uploaded PDF to a temporary file
    temp_dir = tempfile.gettempdir()
    temp_path = os.path.join(temp_dir, f"{uuid.uuid4()}.pdf")


    with open(temp_path, "wb") as f:
        f.write(await pdf.read())
    
    try:
        # Extract text from PDF pages
        pages = extract_pages(temp_path)
        
        # Generate candidate questions in parallel
        candidate_questions = generate_all_questions(pages)
        
        # Randomly select the custom number of questions
        final_questions = randomize_questions(candidate_questions, custom_count)
    
    finally:
        # Clean up temporary file
        if os.path.exists(temp_path):
            os.remove(temp_path)
    
    return {"questions": final_questions}