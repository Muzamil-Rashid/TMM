from flask import Flask, jsonify
from flask_cors import CORS
import random
import json

app = Flask(__name__)
CORS(app)

@app.route("/paragraph", methods=["GET"])
def get_paragraph():
    try:
        # JSON file ko read karna
        with open("paragraphs.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        paragraphs = data.get("paragraphs", [])

        if not paragraphs:
            return jsonify({"error": "No paragraphs found"}), 404

        # Ek random paragraph select karna
        random_para = random.choice(paragraphs)

        return jsonify({
            "paragraph": random_para
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
