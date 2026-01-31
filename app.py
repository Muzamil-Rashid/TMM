from flask import Flask, jsonify
from flask_cors import CORS
import random
import requests

app = Flask(__name__)
CORS(app)

# 1. URL ko update karein (txt ki jagah json)
GITHUB_JSON_URL = "https://raw.githubusercontent.com/Muzamil-Rashid/TMM/refs/heads/main/paragraphs.json"

@app.route("/paragraph", methods=["GET"])
def get_paragraph():
    try:
        # 2. GitHub se JSON data fetch karein
        response = requests.get(GITHUB_JSON_URL)
        response.raise_for_status() # Agar 404 hoga to ye error pakad lega
        
        data = response.json()
        paragraphs = data.get("paragraphs", [])

        if not paragraphs:
            return jsonify({"error": "No paragraphs found in JSON"}), 404

        return jsonify({
            "paragraph": random.choice(paragraphs)
        })
        
    except Exception as e:
        return jsonify({"error": f"Backend Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run()
