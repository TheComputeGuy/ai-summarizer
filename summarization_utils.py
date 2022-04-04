import pdfplumber
import requests
import os

HCAPTCHA_SECRET = os.getenv("HCAPTCHA_SECRET")
HCAPTCHA_VERIFY_URL = "https://hcaptcha.com/siteverify"

def extract_input_text(file_object):
    text = ""
    with pdfplumber.open(file_object) as pdf:
        for page in pdf.pages:
            text = text + page.extract_text() + " "
    return text

def post_processing(response_text):
    # Incomplete sentence removal - splice until last index of fullstop
    try:
        fullstop_index = response_text.rindex('.')
        response_text = response_text[:fullstop_index + 1]
    except Exception as e:
        print(e)
    return response_text.replace('\\n', '')

def verify_hcaptcha(captcha_response):
    verify_input = {}
    verify_input["secret"] = HCAPTCHA_SECRET
    verify_input["response"] = captcha_response
    verify_response = requests.post(HCAPTCHA_VERIFY_URL, data=verify_input)
    return verify_response.json()['success']