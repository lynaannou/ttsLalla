import os

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")

client = ElevenLabs(
    api_key=api_key
)

user_text = input("Lalla > ")

audio = client.text_to_speech.convert(
    text=user_text,
    voice_id="EXAVITQu4vr4xnSDxMaL",
    model_id="eleven_multilingual_v2"
)

with open("output.mp3", "wb") as f:
    for chunk in audio:
        f.write(chunk)

print("Audio generated successfully!")