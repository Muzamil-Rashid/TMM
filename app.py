from flask import Flask, jsonify
from flask_cors import CORS
import random
import os

app = Flask(__name__)
CORS(app)

@app.route("/paragraph", methods=["GET"])
def get_paragraph():
    file_path = os.path.join(os.path.dirname(__file__), "paragraphs.txt")

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Split paragraphs by blank line
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

    return jsonify({
        "paragraph": random.choice(paragraphs)
    })

@app.route("/")
def home():
    return "KeyMaster Backend Running"

if __name__ == "__main__":
    app.run()
