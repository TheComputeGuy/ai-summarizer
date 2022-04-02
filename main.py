import os
from flask import Flask, request, abort
from werkzeug.utils import secure_filename
from flask_cors import CORS
from summarization_utils import extract_input_text
from summarization_service import *

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1000 * 1000

# Needed in case files need to be saved on the server
# UPLOAD_FOLDER = './temp/uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app)

@app.route('/summary', methods=['POST'])
def get_summary():
    body = request.get_json()

    input_text = body["input"]

    summary_text = process_in_batches(input_text = input_text)

    output_text = {}
    output_text["input"] = input_text
    output_text["summary"] = summary_text
    output_text["status"] = "200"
    output_text["message"] = "Request complete"

    return output_text

@app.route('/pdfSummary', methods=['POST'])
def get_pdf_summary():

     # check if the post request has the file part
    if 'input_file' not in request.files:
        output = {}
        output["status"] = "400"
        output["message"] = "File missing in request"
        return output

    file = request.files['input_file']
    if file:
        # Needed if files are to be read from the server
        # filename = secure_filename(file.filename)
        # input_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        # file.save(input_file_path)
        # input_text = extract_input_text(file_object = input_file_path)
        # os.remove(input_file_path)

        # Perform read from memory - important to have bounds on file size (MAX_CONTENT_LENGTH)
        input_text = extract_input_text(file_object = file.stream)

        summary_text = process_in_batches(input_text=input_text)

        output = {}
        output["input"] = input_text
        output["summary"] = summary_text
        output["status"] = "200"
        output["message"] = "Request complete"

        return output

    return abort(404)

if __name__ == '__main__':
    app.run(debug=True, port=5000)