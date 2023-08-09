# Handwritten Image to Text Extraction

The Handwritten Image to Text Extraction Flask application allows users to extract text from handwritten images, with a captivating Coffee Shop Experience. It utilizes the Tesseract OCR library for accurate text recognition and conversion. The extracted text can be downloaded as a text file.

![Screenshot 2023-06-26 052102](https://github.com/ad1tyahere/Image_To_Text/assets/136618806/0b5f6458-3c7d-4569-b86a-bcf3d3af5ff3)


## Features

- Upload an image containing handwritten text.
- Extract text using Tesseract OCR.
- Download the extracted text as a text file.
- Responsive web interface with error handling.

## Technologies Used

- Python
- Flask
- pytesseract
- PIL
- HTML
- CSS
- Bootstrap

## Usage

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set the path to the Tesseract OCR executable in `app.py` if necessary.

3. Run the application:
   ```
   python app.py
   ```

4. Access the application in your web browser at `http://localhost:5000`.

5. Upload an image file containing handwritten text.

6. Click the "Extract Text" button to initiate text extraction.

7. Download the extracted text as a text file.

## Deployment

Deploy the application to a hosting platform like Heroku, PythonAnywhere, or AWS Elastic Beanstalk. Follow their instructions for deploying a Flask application.

## Contributing

Contributions are welcome! If you find any issues or have suggestions, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

