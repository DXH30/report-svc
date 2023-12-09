from flask import Flask, request, Response
from reportlab.pdfgen import canvas
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def generate_pdf():
    # Get input parameters from query parameters
    name = request.args.get('name', 'World')
    greeting = request.args.get('greeting', 'Hello')

    # Create a PDF using ReportLab
    pdf_buffer = generate_report(name, greeting)

    # Return the PDF as a response
    response = Response(pdf_buffer, content_type='application/pdf')
    filename = f"{name}_report.pdf"
    response.headers['Content-Disposition'] = f'inline; filename={filename}'
    return response

def generate_report(name, greeting):
    # Create a ReportLab PDF
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.drawString(100, 750, f"{greeting}, {name}! This is a customized PDF.")
    pdf.showPage()
    pdf.save()
    buffer.seek(0)
    return buffer

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

