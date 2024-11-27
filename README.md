# Vision Speak Insight Generator 🌟

A powerful web application that enhances accessibility for visually impaired users by generating detailed image descriptions and converting them into audio outputs. This project leverages cutting-edge AI models and intuitive interfaces to bridge the gap between digital media and accessibility.

---

## Features 🚀
- **AI-Powered Image Description**: Utilizes the [BLIP (Bootstrapped Language-Image Pretraining)](https://huggingface.co/Salesforce/blip-image-captioning-large) model for generating detailed and context-aware captions for uploaded images.
- **Audio Output**: Converts generated descriptions into high-quality audio files using `pyttsx3`.
- **User-Friendly Interface**: A clean and responsive web interface built with Flask and Bootstrap.
- **Accessibility First**: Designed to empower visually impaired users by making image content comprehensible.

---

## Tech Stack 🛠️
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS
- **AI Model**: BLIP (via Hugging Face Transformers)
- **Text-to-Speech**: pyttsx3
- **Others**: Torch, Pillow

---

## How It Works 🖼️🔊
1. **Upload an Image**: Users upload an image through the web interface.
2. **Generate Description**: The AI model processes the image and generates a textual description.
3. **Convert to Audio**: The description is converted into an audio file for easy playback.
4. **Download/Listen**: Users can listen to or download the generated audio.

---
