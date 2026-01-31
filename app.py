from flask import Flask, jsonify
from flask_cors import CORS
import random
import requests

app = Flask(__name__)
CORS(app)
@app.route("/paragraph", methods=["GET"])
def get_paragraph():
    try:
        with open("paragraphs.txt", "r", encoding="utf-8") as f:
            # .splitlines() har line ko alag kar dega
            content = f.read().splitlines()

        # Khali lines ko filter out karein
        paragraphs = [p.strip() for p in content if p.strip()]

        if not paragraphs:
            return jsonify({"paragraph": "No paragraphs found in file."})

        # Return ONE random paragraph
        return jsonify({
            "paragraph": random.choice(paragraphs)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
if __name__ == "__main__":
    app.run()





