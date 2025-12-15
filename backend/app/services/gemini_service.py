# app/services/gemini_service.py

import json
import google.generativeai as genai
from app.core.config import settings
from app.services import youtube_service # <-- IMPORT SERVICE BARU KITA

genai.configure(api_key=settings.GOOGLE_API_KEY)

def generate_personalized_learning_path(cv_text: str, job_requirements_text: str) -> str:
    """
    Generates a hyper-adaptive learning path and enriches it with YouTube video suggestions.
    """
    # print("job_requirements_text", job_requirements_text)
    # PROMPT KITA PERBARUI UNTUK MENGHASILKAN STRUKTUR TOPIK YANG BARU
    prompt = f"""
    Anda adalah seorang konselor karir dan arsitek pembelajaran AI yang canggih.
    Tugas Anda adalah membuat rencana belajar yang durasinya paling optimal dan sangat personal.

    PROSES BERPIKIR DAN ATURAN WAJIB:
    1. Lakukan analisis kesenjangan (gap analysis) antara 'TEKS LENGKAP CV PENGGUNA' dan 'SKILL PEKERJAAN TARGET'.
    2. Tentukan sendiri durasi rencana belajar yang paling optimal (antara 1 hingga 12 minggu) berdasarkan besarnya kesenjangan.
    3. Buat rencana belajar mingguan. Untuk setiap topik, JANGAN menyarankan topik yang sudah jelas dikuasai pengguna.
    4. Berikan alasan singkat mengapa Anda memilih durasi tersebut.

    ---
    INPUT DATA:

    1. TEKS LENGKAP CV PENGGUNA:
    ```
    {cv_text}
    ```

    2. SKILL PEKERJAAN TARGET:
    ```
    {job_requirements_text}
    ```
    ---

    OUTPUT:
    Berikan jawaban HANYA dalam format JSON yang valid.
    PENTING: Di dalam 'learning_path', setiap item di dalam array 'topics' harus berupa OBJEK dengan satu kunci 'name', seperti ini: {{"name": "Nama Topik"}}.

    Contoh Format JSON yang BENAR:
    {{
      "rationale": "...",
      "learning_path": [
        {{ 
          "week": 1, 
          "goal": "...", 
          "topics": [
            {{"name": "Pengantar FastAPI"}},
            {{"name": "Konsep REST API"}}
          ], 
          "project_idea": "..." 
        }}
      ]
    }}
    """
    
    try:
        model_flash = genai.GenerativeModel('gemini-1.5-flash')
        # Panggil Gemini untuk mendapatkan struktur dasar
        response = model_flash.generate_content(prompt)
        response_text = response.text.strip().replace("```json", "").replace("```", "")

        data = json.loads(response_text)

######################## pakai ini kalau mau tipa path ada youtube, tapi bikin quota habis ########################

                # *** PROSES PENAMBAHAN YOUTUBE ***
        for week in data.get("learning_path", []):
            for topic in week.get("topics", []):
                topic_name = topic.get("name")
                if topic_name:
                    print(f"Searching YouTube for topic: {topic_name}")
                    # video_info = youtube_service.find_youtube_video(f"{topic_name}")
        #             topic["youtube_suggestion"] = video_info

######################## pakai ini kalau mau tipa path ada youtube, tapi bikin quota habis ########################

            # 2. PROSES BARU: Cari video untuk Ide Proyek Mingguan
            project_text = week.get("project_idea")
            if project_text:
                print(f"Searching YouTube for project: {project_text}")
                # Membuat query lebih spesifik untuk proyek
                project_video_info = youtube_service.find_youtube_video(f"{project_text} project tutorial")
                
                # Ubah struktur 'project_idea' dari string menjadi objek
                week["project_idea"] = {
                    "text": project_text,
                    "video": project_video_info # Hasilnya bisa berupa dict atau None
                }

        # Ubah kembali objek yang sudah diperkaya ke dalam format teks JSON
        return json.dumps(data, indent=2)

    except Exception as e:
        print(f"An error occurred: {e}")
        return None