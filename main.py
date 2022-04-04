import os
from flask import Flask, request, abort
from werkzeug.utils import secure_filename
from flask_cors import CORS
from summarization_utils import extract_input_text, verify_hcaptcha
from summarization_service import *

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1000 * 1000

# Needed in case files need to be saved on the server
# UPLOAD_FOLDER = './temp/uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app)

@app.route('/', methods=['GET'])
@app.route('/isAlive', methods=['GET'])
def get_health():
    return "Ready to summarize!"

@app.route('/summary', methods=['POST'])
def get_summary():
    body = request.form

    if 'hcaptcha_response' not in body.keys():
        abort(401)

    hcaptcha_response = body['hcaptcha_response']

    is_hcaptcha_valid = verify_hcaptcha(captcha_response = hcaptcha_response)

    if not is_hcaptcha_valid:
        abort(403)

    if 'input' not in body.keys():
        output = {}
        output["status"] = "400"
        output["message"] = "Input missing in request"
        return output, 400

    input_text = body["input"]

    if input_text:
        try:
            summary_text = process_in_batches(input_text = input_text)
            output = {}
            output["input"] = input_text
            output["summary"] = summary_text
            output["status"] = "200"
            output["message"] = "Request complete"
            return output
        except Exception as e:
            print(e)
            output = {}
            output["status"] = "500"
            output["message"] = "An error occured while processing your request"
            return output, 500

    output = {}
    output["status"] = "400"
    output["message"] = "Input text missing in request"
    return output, 400

@app.route('/pdfSummary', methods=['POST'])
def get_pdf_summary():

    body = request.form

    if 'g-recaptcha-response' not in body.keys():
        abort(401)

    hcaptcha_response = body['g-recaptcha-response']

    is_hcaptcha_valid = verify_hcaptcha(captcha_response = hcaptcha_response)

    if not is_hcaptcha_valid:
        abort(403)

     # check if the post request has the file part
    if 'input_file' not in request.files:
        output = {}
        output["status"] = "400"
        output["message"] = "File missing in request"
        return output, 400

    file = request.files['input_file']
    if file:
        # Needed if files are to be read from the server
        # filename = secure_filename(file.filename)
        # input_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        # file.save(input_file_path)
        # input_text = extract_input_text(file_object = input_file_path)
        # os.remove(input_file_path)

        # Perform read from memory - important to have bounds on file size (MAX_CONTENT_LENGTH)
        try:
            input_text = extract_input_text(file_object = file.stream)
            summary_text = process_in_batches(input_text=input_text)

            output = {}
            output["input"] = input_text
            output["summary"] = summary_text
            output["status"] = "200"
            output["message"] = "Request complete"
            return output
        except Exception as e:
            print(e)
            output = {}
            output["status"] = "500"
            output["message"] = "An error occured while processing your request"
            return output, 500

    output = {}
    output["status"] = "400"
    output["message"] = "Could not extract any text from the file!"
    return output, 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)