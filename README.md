# Advanced PDF to Word Batch Converter (Python + Flask)

Welcome to Docuswitch_Pro PDF to Word converter, powered by pure Python using Flask and pdf2docx.

This tool is designed to allow both single and batch PDF uploads, converting them into high-quality Word documents—all through a clean, Bootstrap-enhanced web interface.

## Features

- Batch conversion — Upload one or multiple PDF files and get back individual `.docx` files or a ZIP of all.
- Secure file handling — Uses Python’s tempfile to ensure files are stored temporarily and cleaned up.
- Professional UI — Responsive, Bootstrap 5 interface with friendly file previews and alerts.
- Robust error handling — Users get clear flash messages when something goes wrong.
- Download-ready output — Files are returned with appropriate MIME types and timestamps.

## Project Structure

```
DocuSwitch_Pro/
│
├── app.py                  # Flask backend logic and PDF-to-Word conversion
├── templates/
│   └── index.html          # HTML frontend using Bootstrap 5
├── requirements.txt        # Python dependencies (Flask, pdf2docx)
├── .gitignore              # Git exclusions (temp files, cache, etc.)
└── README.txt              # Project documentation

```

## Requirements

- Python 3.7+
- Flask
- pdf2docx
- Bootstrap (loaded via CDN)

Install the dependencies:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install flask pdf2docx
```

## How to Run the App

1. Clone or download the repository:

```bash
git clone https://github.com/Hamona2323/DocuSwitch_Pro
cd DocuSwitch_Pro
```

2. Run the Flask app:

```bash
python app.py
```

3. Open your browser and go to:

```
http://localhost:5000
```

4. Upload PDF(s) -> Convert -> Download

## How It Works

1. User uploads one or multiple PDF files.
2. Backend checks if each file is valid (.pdf) and under the size limit (50MB).
3. If a single file: converts and returns .docx.
4. If multiple files: converts all, zips them with a timestamp, and sends as a .zip.
5. Temporary files are deleted after processing.

## Security & Limitations

- 50MB upload limit per file (configured via MAX_CONTENT_LENGTH).
- No external APIs — fully offline and Python-based.
- Uses Flask’s secure handling of file uploads.
- Temporary files are cleaned up safely after each request.

## UI & Design Choices

- Bootstrap 5 for a modern, clean interface.
- Drag-and-drop-inspired upload area (simulated with styled label).
- Minimal JavaScript used for previewing selected files.
- Flash messages for feedback (success, error, warning).
- Responsive card layout for mobile-friendly experience.

## Example Use Case

A teacher wants to batch convert student-submitted PDFs to editable Word docs. Instead of converting them manually, she uploads all files at once and downloads a ZIP in seconds.

## Example Output

When uploading 3 PDFs named:

- essay1.pdf
- report2.pdf
- final_paper.pdf

You'll get:

```
converted_essay1.docx
converted_report2.docx
converted_final_paper.docx
```

If multiple: all are packaged into:

```
converted_files_20250601_144530.zip
```

## Testing Tips

- Upload a mix of valid and invalid files (e.g., .pdf, .jpg) to test flash messages.
- Try with large files to trigger the 50MB limit.
- Test one vs multiple file upload behaviors.

## Technologies Used

| Technology   | Purpose                     |
|--------------|-----------------------------|
| Python       | Main programming language   |
| Flask        | Web framework               |
| pdf2docx     | PDF to Word conversion      |
| Bootstrap 5  | UI styling (via CDN)        |
| JavaScript   | Basic file preview          |

### Prepared by:

**Hemon Gergsh Gebremariam 161507**  
**WSB Merito University**
