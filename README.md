# 🎙️ Whisper Speech-to-Text App (Multilingual: French, English, etc.)

Cette application propose une transcription automatique de la voix vers le texte à l'aide du modèle **Whisper** d'OpenAI, un modèle auto-supervisé de pointe en reconnaissance vocale (ASR - Automatic Speech Recognition). Elle fonctionne **en français, anglais et dans plus de 90 langues**.

Fonctionne parfaitement pour :
- La transcription de **notes vocales**
- Le traitement **multilingue**
- Des démonstrations simples et pratiques de modèles préentraînés en SSL (Self-Supervised Learning)

---

##  Fonctionnalités

-  Transcription **multilingue** (français, anglais, etc.)
-  Utilisation du modèle Whisper **préentraîné** (pas de ré-entraînement nécessaire)
-  Interface **Gradio** conviviale pour uploader ou enregistrer de l'audio
-  Fonctionne en local ou sur Google Colab avec GPU
-  Basé sur le paradigme **Self-Supervised Learning**

---

## Pourquoi Whisper ?

Whisper est un modèle de type **SSL (Self-Supervised Learning)** développé par OpenAI. Il a été entraîné sur **680 000 heures d'audio multilingue**. Il permet de :

- Détecter automatiquement la langue
- Transcrire la parole en texte
- Traduire de l’audio vers l’anglais

---

## Dépendances

```txt
gradio>=4.0.0
datasets>=2.18.0
git+https://github.com/openai/whisper.git
torchaudio

