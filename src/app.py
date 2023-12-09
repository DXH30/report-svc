from flask import Flask, request, jsonify
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
import requests
import os

app = Flask(__name__)

# Get the forward API URL from the environment variable
FORWARD_API_URL = os.getenv('FORWARD_API_URL', 'http://mail-svc:3000/send')

def create_pdf(content, pdf_path):
    # Create a PDF file using ReportLab with wrapped text
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    styles = getSampleStyleSheet()
    style = styles['Normal']

    # Add content to the PDF
    story = [Paragraph(content, style)]

    # Build the PDF document
    doc.build(story)

@app.route('/convert', methods=['POST'])
def convert_content_to_pdf():
    try:
        # Get input parameters from the request
        content = request.form.get('content')
        email = request.form.get('email')

        # Generate a PDF from the content
        pdf_file_path = f'./output.pdf'
        create_pdf(content, pdf_file_path)

        # Forward the PDF to another API using the environment variable
        files = {
                'attachment': ('report.pdf', open(pdf_file_path, 'rb'), 'application/pdf')
                }

        data = {'email': email}
        response = requests.post(FORWARD_API_URL, files=files, data=data)

        # Optional: You may want to check the response from the forward API
        if response.status_code == 200:
            return jsonify({'status': 'success', 'message': 'PDF forwarded successfully'})
        else:
            return jsonify({'status': 'error', 'message': response.content, 'request': request})

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

