from flask import Flask, jsonify
from flask_cors import CORS
import random
import requests

app = Flask(__name__)
CORS(app)
@app.route("/paragraph", methods=["GET"])
def get_paragraph():
    with open("paragraphs.txt", "r", encoding="utf-8") as f:
        content = f.read()

    # 🔹 split by empty line = paragraphs
    paragraphs = [p.strip() for p in content.split("\n\n\n\n") if p.strip()]

    # 🔹 return ONE random paragraph
    return jsonify({
        "paragraph": random.choice(paragraphs)
    })

if __name__ == "__main__":
    app.run()




