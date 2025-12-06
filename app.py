from flask import Flask, render_template, request
from google.genai import Client
import os
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

client = Client(api_key=gemini_api_key)

app = Flask(__name__)

def simplify_text(text):
    response = client.models.generate_content(
        model="gemini-2.0-flash",   # correct model name
        contents=f"Convert the following text into simplified, easy-to-read language:\n\n{text}"
    )
    return response.text

@app.route("/", methods=["GET", "POST"])
def index():
    simplified = ""
    original_text = ""
    if request.method == "POST":
        file = request.files.get("file")
        if file:
            original_text = file.read().decode("utf-8")
            simplified = simplify_text(original_text)
    return render_template("index.html", simplified=simplified, original_text=original_text)

if __name__ == "__main__":
    app.run(debug=True)