# Accessibility Helper

**Accessibility Helper** is a web application that allows teachers and educators to simplify their notes and documents into clear, easy-to-read language. Powered by **Google Gemini**, it converts complex text into accessible content for all learners.

---

## Features

* Upload `.txt` files containing notes or lesson materials.
* Automatically simplifies text using Google Gemini 2.5 Flash model.
* View original and simplified notes side by side.
* Copy simplified text to clipboard easily.
* Fully accessible UI with keyboard-friendly navigation and ARIA support.

---
## Interface
<img width="1294" height="766" alt="Demo" src="https://github.com/user-attachments/assets/c5c67ca5-3f7e-4c37-aaa3-869854f276ce" />


---

## Installation

### Prerequisites

* Python 3.9+
* Google Gemini API key

### Steps

1. **Clone the repository**

```bash
git clone <https://github.com/Ghazanfar-Abbas550/Accesbility_Helper>
cd Accessibility_Helper
```

2. **Create and activate a virtual environment (must)**

```bash
python -m venv venv
# On PowerShell
venv\Scripts\Activate.ps1
# On Command Prompt
venv\Scripts\activate.bat
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Create a `.env` file in the project root**

```env
GEMINI_API_KEY=your_api_key_here
```

5. **Run the application**

```bash
python app.py
```

6. Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## Folder Structure

```
Accessibility_Helper/
├── app.py                # Flask app
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (API key)
├── templates/
│   └── index.html        # Main HTML page
├── static/
│   └── style.css         # CSS for the app
```

---

## Dependencies

* `Flask==3.1.2` – Web framework
* `google-genai==1.47.0` – Google Gemini API SDK
* `requests==2.32.5` – HTTP requests
* `python-dotenv==1.2.1` – Environment variable management

---

## Usage

1. Upload a `.txt` file with notes.
2. Click **Simplify**.
3. View original notes on the left and simplified notes on the right.
4. Click **Copy** to copy simplified notes to clipboard.

---

## Notes

* Only plain text files (`.txt`) are supported.
* Requires a valid Gemini API key saved in `.env`.
* Works best with clear, structured educational notes.
