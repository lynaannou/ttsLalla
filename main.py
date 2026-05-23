from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File
from fastapi import Form

app = FastAPI()

@app.post("/analyze")
async def analyze(

    input_type: str = Form(...),

    text: str = Form(None),

    audio: UploadFile = File(None),

    video: UploadFile = File(None),

    session_id: str = Form(None),

    language: str = Form(None),

    timestamp: str = Form(None)
):

    return {

        "message": "Request received",

        "input_type": input_type,

        "text": text,

        "audio_filename":
            audio.filename if audio else None,

        "video_filename":
            video.filename if video else None,

        "session_id": session_id,

        "language": language,

        "timestamp": timestamp
    }