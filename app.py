from flask import Flask, render_template, request, flash
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

# Gemini 1.5 Flash API setup
GEMINI_API_KEY = ''  # 🔐 Replace with your actual key
GEMINI_URL = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}'

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    
    if request.method == "POST":
        input_text = request.form["input_text"]
        input_length = len(input_text.split())

        if input_length < 50:
            flash("Please enter at least 50 words for summarization.", "error")
        else:
            prompt = f"Summarize the following text into a clear and concise paragraph:\n\n{input_text}"

            data = {
                "contents": [
                    {
                        "parts": [{"text": prompt}]
                    }
                ]
            }

            try:
                response = requests.post(GEMINI_URL, json=data)

                if response.status_code == 200:
                    result = response.json()
                    summary = result['candidates'][0]['content']['parts'][0]['text']
                else:
                    flash(f"Gemini API error: {response.status_code} - {response.text}", "error")

            except Exception as e:
                flash(f"An error occurred: {str(e)}", "error")

    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
