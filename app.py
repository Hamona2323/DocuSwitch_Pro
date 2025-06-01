from flask import Flask, render_template, request, send_file, flash, redirect, url_for
from pdf2docx import Converter
import os
import tempfile
import zipfile
import io
from datetime import datetime
import traceback

app = Flask(__name__)
app.secret_key = 'your_secure_key_here'  # For flash messages

# Configuration
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB limit
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'files' not in request.files:
            flash('No files selected', 'error')
            return redirect(url_for('home'))
        
        files = request.files.getlist('files')
        if not files or all(f.filename == '' for f in files):
            flash('No files selected', 'error')
            return redirect(url_for('home'))
        
        return process_files(files)
    
    return render_template('index.html')

def process_files(files):
    valid_files = []
    for file in files:
        if file and allowed_file(file.filename):
            valid_files.append(file)
        else:
            flash(f'Invalid file skipped: {file.filename}', 'warning')
    
    if not valid_files:
        flash('No valid PDF files to convert', 'error')
        return redirect(url_for('home'))
    
    try:
        # Single file processing
        if len(valid_files) == 1:
            file = valid_files[0]
            output = convert_to_word(file)
            return send_file(
                output['path'],
                as_attachment=True,
                download_name=output['name'],
                mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            )
        
        # Batch processing
        else:
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for file in valid_files:
                    result = convert_to_word(file)
                    zip_file.write(result['path'], result['name'])
            
            zip_buffer.seek(0)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            return send_file(
                zip_buffer,
                as_attachment=True,
                download_name=f'converted_files_{timestamp}.zip',
                mimetype='application/zip'
            )
    
    except Exception as e:
        app.logger.error(f"Conversion error: {str(e)}\n{traceback.format_exc()}")
        flash('Conversion failed. Please try again.', 'error')
        return redirect(url_for('home'))

def convert_to_word(file):
    """Convert single PDF to Word with proper cleanup"""
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as pdf_temp:
        file.save(pdf_temp.name)
        pdf_path = pdf_temp.name
    
    word_temp = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
    word_path = word_temp.name
    word_temp.close()  # Close so Converter can access
    
    try:
        cv = Converter(pdf_path)
        cv.convert(word_path)
        cv.close()
        
        return {
            'path': word_path,
            'name': f"converted_{os.path.splitext(file.filename)[0]}.docx"
        }
    finally:
        try:
            os.unlink(pdf_path)
        except:
            pass

if __name__ == '__main__':
    app.run(debug=True)