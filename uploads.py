import streamlit as st



MAX_CHARS = 12000



def limit_text(text):

    if len(text) > MAX_CHARS:

        return (
            text[:MAX_CHARS]
            +
            "\n\n[Content truncated]"
        )

    return text





def extract_file_content(file):

    file.seek(0)
    text = ""
    """
    Extract useful business information
    from uploaded files.
    """


    text = ""


    try:


        # =====================
        # PDF
        # =====================

        if file.name.endswith(".pdf"):


            import PyPDF2


            reader = PyPDF2.PdfReader(
                file
            )


            for page in reader.pages:


                text += (
                    page.extract_text()
                    or ""
                )



        # =====================
        # TXT
        # =====================


        elif file.name.endswith(".txt"):


            text = file.read().decode(
                "utf-8",
                errors="ignore"
            )



        # =====================
        # DOCX
        # =====================


        elif file.name.endswith(".docx"):


            from docx import Document


            doc = Document(file)


            for paragraph in doc.paragraphs:


                text += (
                    paragraph.text
                    +
                    "\n"
                )



        # =====================
        # CSV
        # =====================


        elif file.name.endswith(".csv"):


            import pandas as pd


            df = pd.read_csv(file)


            text = df.to_string()



        # =====================
        # EXCEL
        # =====================


        elif file.name.endswith(".xlsx"):


            import pandas as pd


            excel = pd.ExcelFile(
                file
            )


            for sheet in excel.sheet_names:


                df = pd.read_excel(
                    file,
                    sheet_name=sheet
                )


                text += f"""

SHEET:

{sheet}


{df.to_string()}

"""


        # =====================
        # IMAGE
        # =====================


        elif file.type.startswith(
            "image"
        ):


            text = """

Image uploaded.

Visual analysis required.

The file may contain:
- Dashboard
- Screenshot
- Document image
- Chart
- Notes

"""


        else:


            text = (
                "Unsupported file type."
            )



    except Exception as e:


        text = f"""

File extraction failed:

{e}

"""



    return limit_text(text)







def upload_file():


    st.markdown(
        "## 📎 Attach Business Files (Optional)"
    )


    uploaded_files = st.file_uploader(

        "Upload documents, spreadsheets, screenshots",

        type=[

            "pdf",
            "docx",
            "txt",
            "csv",
            "xlsx",
            "png",
            "jpg",
            "jpeg"

        ],


        accept_multiple_files=True,


        label_visibility="collapsed"

    )



    extracted_data = []



    if uploaded_files:


        st.success(
            f"{len(uploaded_files)} file(s) attached."
        )



        for file in uploaded_files:


            content = extract_file_content(
                file
            )



            extracted_data.append({


                "filename": file.name,


                "type": file.type,


                "content": content


            })



    return extracted_data