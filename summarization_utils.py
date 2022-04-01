import pdfplumber

def extract_input_text_from_file(filepath):    
    text = ""
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text = text + page.extract_text() + "\n"
        text = text + "tl;dr:\n"
    return text

def extract_input_text(file_object):
    text = ""
    with pdfplumber.open(file_object) as pdf:
        for page in pdf.pages:
            text = text + page.extract_text() + "\n"
        text = text + "tl;dr:\n"
    return text