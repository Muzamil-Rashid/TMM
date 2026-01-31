from flask import Flask, jsonify
import random
import requests

app = Flask(__name__)

# Home route (already working)
@app.route("/")
def home():
    return "Typing Speed Test Backend Running"

# Paragraph API route (THIS WAS MISSING)
@app.route("/paragraph", methods=["GET"])
def get_paragraph():
    url = "https://raw.githubusercontent.com/Muzamil-Rashid/TMM/refs/heads/main/paragraphs.txt"
    
    response = requests.get(url)
    paragraphs = response.text.split(",")

    selected = random.choice(paragraphs).strip()

    return jsonify({
        "paragraph": selected
    })

if __name__ == "__main__":
    app.run()

