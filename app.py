import os
from flask import Flask, render_template, request, send_file
import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import pyttsx3

class VisionSpeakInsightGenerator:
    def __init__(self):
        # Initialize BLIP model for image captioning
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")
        
        # Initialize text-to-speech engine
        self.tts_engine = pyttsx3.init()
        
    def generate_image_description(self, image):
        """
        Generate detailed description of the input image
        """
        # Prepare image for processing
        inputs = self.processor(image, return_tensors="pt")
        
        # Generate description
        with torch.no_grad():
            generated_ids = self.model.generate(**inputs, max_length=50)
        
        # Decode the generated description
        description = self.processor.decode(generated_ids[0], skip_special_tokens=True)
        
        return description
    
    def text_to_speech(self, text):
        """
        Convert text description to audio
        """
        # Ensure output directory exists
        os.makedirs('static', exist_ok=True)
        
        # Save audio to a file in the static directory
        output_file = "static/image_description.mp3"
        self.tts_engine.save_to_file(text, output_file)
        self.tts_engine.runAndWait()
        
        return output_file

# Flask application setup
app = Flask(__name__)

# Initialize the generator
generator = VisionSpeakInsightGenerator()

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    description = None
    audio_file = None
    
    if request.method == 'POST':
        # Check if an image was uploaded
        if 'image' not in request.files:
            return render_template('index.html', error='No image uploaded')
        
        file = request.files['image']
        
        # Check if filename is empty
        if file.filename == '':
            return render_template('index.html', error='No selected file')
        
        # Check file type
        allowed_extensions = {'png', 'jpg', 'jpeg'}
        if not file.filename.lower().split('.')[-1] in allowed_extensions:
            return render_template('index.html', error='Invalid file type. Please upload PNG, JPG, or JPEG.')
        
        # Open and process the image
        image = Image.open(file)
        
        # Generate description
        description = generator.generate_image_description(image)
        
        # Generate audio description
        audio_file = generator.text_to_speech(description)
    
    return render_template('index.html', 
                           description=description, 
                           audio_file=audio_file)

@app.route('/audio/<path:filename>')
def serve_audio(filename):
    return send_file(os.path.join('static', filename), mimetype='audio/mp3')

if __name__ == '__main__':
    app.run(debug=True)