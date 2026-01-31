from flask import Flask, jsonify
from flask_cors import CORS
import random
import requests
import os

app = Flask(__name__)
CORS(app)

PARAGRAPHS_URL = "https://raw.githubusercontent.com/Muzamil-Rashid/TMM/refs/heads/main/paragraphs.txt"


@app.route("/")
def home():
    return "Typing Speed Test Backend is Running"


@app.route("/paragraph")
def get_paragraph():
    try:
        response = requests.get(PARAGRAPHS_URL, timeout=5)
        response.raise_for_status()
        
        paragraphs = [p.strip() for p in response.text.split(""") if p.strip()]
        
        if not paragraphs:
            return jsonify({"error": "No paragraphs available"}), 500
        
        return jsonify({
            "paragraph": random.choice(paragraphs)
        })
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to fetch paragraphs: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)


