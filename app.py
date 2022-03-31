import os
from flask import Flask, request, abort
from werkzeug.utils import secure_filename
from flask_cors import CORS

UPLOAD_FOLDER = './temp/uploads'

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 2 * 1000 * 1000
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

@app.route('/summary', methods=['POST'])
def get_summary():
    body = request.get_json()

    input_text = body["input"]

    summary_text = "This is some summary text"

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
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Either save the file as ^ or directly feed it into the PDF parser
        # Get output text. Then pass it to the model method

        input_text = "dummy"
        summary_text = "dummy"

        output = {}
        output["input"] = input_text
        output["summary"] = summary_text
        output["status"] = "200"
        output["message"] = "Request complete"

        return output

    return abort(404)

if __name__ == '__main__':
    app.run(debug=True, port=5000)