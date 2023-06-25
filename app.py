from flask import Flask, render_template, request, send_file
import pytesseract
from PIL import Image
import tempfile

# Set the path to the Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract_text', methods=['POST'])
def extract_text():
    # Check if the post request has the file part
    if 'image' not in request.files:
        return render_template('index.html', error='No image selected!')

    file = request.files['image']

    if file.filename == '':
        return render_template('index.html', error='No image selected!')

    # Read the uploaded image
    image = Image.open(file)
    
    # Extract text from the image
    text = pytesseract.image_to_string(image)

    # Create a temporary file with the extracted text
    with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as tmp_file:
        tmp_file.write(text.encode())

    # Return the temporary file for download
    return send_file(tmp_file.name, as_attachment=True, download_name='extracted_text.txt')

if __name__ == '__main__':
    app.run(debug=True)
