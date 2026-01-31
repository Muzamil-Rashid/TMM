from flask import Flask, jsonify
from flask_cors import CORS
import random
import os

app = Flask(__name__)
CORS(app)

@app.route("/paragraph", methods=["GET"])
def get_paragraph():
    try:
        # 1. File path check karein
        file_path = "paragraphs.txt"
        
        if not os.path.exists(file_path):
            return jsonify({"error": "File paragraphs.txt not found!"}), 404

        # 2. File read karke har line ko list ka element banana
        with open(file_path, "r", encoding="utf-8") as f:
            # .read().splitlines() se ye auto-list ban jayegi
            paragraphs = f.read().splitlines()

        # 3. Khali items remove karna (clean list)
        paragraphs = [p.strip() for p in paragraphs if p.strip()]

        if not paragraphs:
            return jsonify({"error": "File is empty!"}), 404

        # 4. RANDOM paragraph pick karna
        selected_paragraph = random.choice(paragraphs)

        return jsonify({
            "paragraph": selected_paragraph
        })

    except Exception as e:
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run()
