from flask import Flask, render_template, request, flash
from transformers import pipeline

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

# Initialize the Hugging Face summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_text = request.form["input_text"]
        input_length = len(input_text.split())

        # Define dynamic length ratios
        min_ratio = 0.3  # Summary length as 30% of input length
        max_ratio = 0.5  # Summary length as 50% of input length

        # Calculate dynamic min_length and max_length
        min_length = max(50, int(input_length * min_ratio))
        max_length = min(1500, int(input_length * max_ratio))  # Set a reasonable upper limit

        if input_length < 50:
            flash("Please enter at least 50 words for summarization.", "error")
        else:
            try:
                summary = summarizer(input_text, min_length=min_length, max_length=max_length, do_sample=False)[0]['summary_text']
                return render_template("index.html", summary=summary)
            except Exception as e:
                flash(f"An error occurred: {str(e)}", "error")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
