import json
from fastapi import APIRouter, UploadFile, File, Form, HTTPException # <-- IMPORT Form
import PyPDF2
import io

# Kita tidak lagi butuh scraper_service
from app.services import gemini_service

router = APIRouter()

@router.post("/generate-path")
# V-- UBAH TANDA TANGAN FUNGSI DI SINI --V
async def generate_learning_path_from_cv(
    file: UploadFile = File(...), 
    job_title: str = Form(...) 
):
    if file.content_type != 'application/pdf':
        raise HTTPException(status_code=400, detail="File must be a PDF.")

    try:
        # 1. Ekstrak teks dari PDF (Tetap sama)
        pdf_content = await file.read()
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_content))
        cv_text = ""
        for page in pdf_reader.pages:
            cv_text += page.extract_text()

        if not cv_text.strip():
            raise HTTPException(status_code=400, detail="Could not extract text from PDF.")

        # 2. Hapus panggilan ke scraper. Gunakan job_title dari frontend.
        # job_postings_text = scraper_service.scrape_job_postings() <-- HAPUS INI
        job_requirements_text = job_title # <-- GUNAKAN DATA DINAMIS INI

        # 3. Panggil service Gemini dengan data yang dinamis
        learning_path_str = gemini_service.generate_personalized_learning_path(
            cv_text=cv_text, 
            job_requirements_text=job_requirements_text
        )
        
        if not learning_path_str:
            raise HTTPException(status_code=500, detail="AI service failed to generate learning path.")

        return json.loads(learning_path_str)

    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="AI service returned invalid JSON.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))