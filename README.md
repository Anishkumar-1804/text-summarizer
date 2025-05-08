`markdown
# 📝 TextSummarizerApp

A web-based AI-powered Text Summarization application built with Python and Flask. It uses Hugging Face's `transformers` library with the `facebook/bart-large-cnn` model to generate concise summaries from long input texts.

---

## 🚀 Features

- 🧠 **AI-Powered Summarization**  
  Automatically condenses long texts into brief, informative summaries using the BART model.

- 📏 **Dynamic Summary Length**  
  Summary length adjusts based on the input length (30%–50%).

- ⚠️ **Minimum Word Check**  
  Displays a warning if the input contains fewer than 50 words.

- 🧾 **Copy-to-Clipboard**  
  Easily copy the summarized text with a single click.

- 🎨 **Clean UI**  
  Simple and modern interface with responsive design.

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python 3, Flask
- **Libraries**:
  - [`transformers`](https://huggingface.co/transformers/)
  - `torch` (backend for model inference)
  - `Flask` (web framework)

---

## 📦 Installation

### 1. Clone the Repository

`bash
git clone https://github.com/your-username/TextSummarizerApp.git
cd TextSummarizerApp
`

### 2. Set Up Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> Make sure to include `torch`, `transformers`, and `flask` in `requirements.txt`.

---

## ▶️ Run the App

```bash
python app.py
```

Then open your browser and go to:
**[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 📂 Project Structure

```
TextSummarizerApp/
│
├── static/
│   └── style.css             # Styling for the web interface
│
├── templates/
│   └── index.html            # Main HTML page
│
├── app.py                    # Flask backend
├── requirements.txt          # Project dependencies
├── README.md                 # Project documentation
```

---

## 🧠 How It Works

1. User inputs a long paragraph of text.
2. Flask sends the text to the Hugging Face BART summarization pipeline.
3. The model returns a summary, which is displayed on the page.
4. User can click a button to copy the summary.

---

## 👨‍💻 Author

**Anishkumar**
GitHub: [Anishkumar-1804](https://github.com/Anishkumar-1804)
---

## 📜 License

This project is open-source and available for educational and personal use.

---

## 💡 Future Enhancements

* Add support for file input (PDF, DOCX)
* Allow customization of summary length
* Integrate other models like PEGASUS or T5
* Enable summary history and export options

---

```
```
