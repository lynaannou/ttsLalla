import os

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY1")

print(api_key)

client = ElevenLabs(
    api_key=api_key
)

transcription = client.speech_to_text.convert(
    file=open("output.mp3", "rb"),
    model_id="scribe_v1"
)
print(transcription.text)

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(transcription.text)

print("Text generated successfully!")