# Authentification à Hugging Face (nécessaire si le dataset est protégé)
from getpass import getpass
from huggingface_hub import login

login(getpass("🔑 Entre ton token Hugging Face ici : "))  # <- Colle ici ton token HF

# Installer les bibliothèques nécessaires
!pip install -q gradio
!pip install -q git+https://github.com/openai/whisper.git
!pip install -q datasets torchaudio

# Télécharger 1% du dataset Common Voice 13.0 (français)
from datasets import load_dataset

dataset = load_dataset(
    "mozilla-foundation/common_voice_13_0",
    "fr",
    split="train[:1%]"
)

#  Sélectionner un échantillon audio
sample = dataset[0]
audio_path = sample["audio"]["path"]
print(f"Chemin du fichier audio : {audio_path}")
print("Texte attendu :", sample["sentence"])

# Charger le modèle Whisper
import whisper
model = whisper.load_model("base")  # ou "small" pour aller plus vite

# Transcrire l'audio
result = model.transcribe(audio_path, language="fr")
print("Texte transcrit :", result["text"])

import gradio as gr

# Fonction de transcription depuis un fichier
def transcribe_from_file(audio_file):
    result = model.transcribe(audio_file, language="fr")
    return result["text"]

# Interface utilisateur Gradio
demo = gr.Interface(
    fn=transcribe_from_file,
    inputs=gr.Audio(type="filepath", label="🎙️ Enregistre ou téléverse un fichier audio"),
    outputs=gr.Textbox(label="📝 Transcription"),
    title="Transcription vocale avec Whisper",
    description="Enregistre ta voix ou charge un fichier audio (.mp3, .wav...) pour obtenir la transcription automatique avec Whisper."
)

# Lancer l'application
demo.launch(debug=True)




