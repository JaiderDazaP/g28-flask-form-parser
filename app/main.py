from flask import Flask, jsonify, request, abort, render_template
from pdf_extractor import extract_form_data
import json
import os

app = Flask(__name__)

# Generate output.json automatically at startup if it doesn't exist
PDF_PATH = "g-28_data.pdf"
OUTPUT_JSON = "output.json"

if not os.path.exists(OUTPUT_JSON):
    extract_form_data(PDF_PATH, OUTPUT_JSON)

# Authenticated endpoint to return the extracted JSON data
@app.route("/api/json", methods=["GET"])
def get_json():
    auth = request.authorization
    if not auth or not (auth.username == "admin" and auth.password == "admin"):
        return abort(401, description="Unauthorized")

    try:
        with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
            form_data = json.load(f)
        return jsonify(form_data)
    except FileNotFoundError:
        return {"error": "JSON file not found"}, 404

# Endpoint to serve the HTML viewer
@app.route("/")
def index():
    return render_template("viewer.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4532)