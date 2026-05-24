import os

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")

print(api_key)  

client = ElevenLabs(
    api_key=api_key
)

audio = client.text_to_speech.convert(
    text="Rajoute un peu de paprika dans la sauce tomate pour lui donner plus de goût.",
    voice_id="EXAVITQu4vr4xnSDxMaL",
    model_id="eleven_multilingual_v2"
)

with open("output.mp3", "wb") as f:
    for chunk in audio:
        f.write(chunk)

print("Audio generated successfully!")