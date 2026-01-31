from flask import Flask, jsonify
from flask_cors import CORS
import random
import requests

app = Flask(__name__)
CORS(app)

# Home route (already working)
@app.route("/")
def home():
    return "Typing Speed Test Backend Running"

# Paragraph API route (THIS WAS MISSING)
@app.route("paragraph", methods=["GET"])
def get_paragraph():
    url = "https://raw.githubusercontent.com/Muzamil-Rashid/TMM/refs/heads/main/paragraphs.txt"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        paragraphs = [p.strip() for p in response.text.split("\n\n") if p.strip()]
    

            
            if not paragraphs:
                return jsonify({"error": "No paragraphs available"}), 500
            
            return jsonify({
                "paragraph": random.choice(paragraphs)
        })
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to fetch paragraphs: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)






