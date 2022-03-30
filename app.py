from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
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

if __name__ == '__main__':
    app.run(debug=True, port=5000)