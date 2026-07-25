"""
parser.py - Document & Image Parsing Engine
"""
import io
import pandas as pd
from PIL import Image
import PyPDF2
import docx

def parse_uploaded_file(uploaded_file):
    filename = uploaded_file.name
    file_ext = filename.split(".")[-1].lower()

    try:
        if file_ext in ["png", "jpg", "jpeg", "webp"]:
            image = Image.open(uploaded_file)
            return {"type": "image", "content": image, "filename": filename}

        elif file_ext == "pdf":
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            extracted_text = ""
            for page_num, page in enumerate(pdf_reader.pages):
                text = page.extract_text()
                if text:
                    extracted_text += f"\n--- Page {page_num + 1} ---\n{text}"
            return {"type": "text", "content": extracted_text.strip(), "filename": filename}

        elif file_ext == "docx":
            doc = docx.Document(uploaded_file)
            full_text = [para.text for para in doc.paragraphs if para.text.strip()]
            return {"type": "text", "content": "\n".join(full_text), "filename": filename}

        elif file_ext in ["csv", "xlsx", "xls"]:
            df = pd.read_csv(uploaded_file) if file_ext == "csv" else pd.read_excel(uploaded_file)
            return {"type": "text", "content": df.head(50).to_markdown(index=False), "filename": filename}

        elif file_ext in ["txt", "md"]:
            return {"type": "text", "content": uploaded_file.getvalue().decode("utf-8"), "filename": filename}

        else:
            return {"type": "error", "content": f"Unsupported format: {file_ext}", "filename": filename}

    except Exception as e:
        return {"type": "error", "content": str(e), "filename": filename}