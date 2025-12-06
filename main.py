import os

# Create folders
os.makedirs("AccessibilityHelper/templates", exist_ok=True)
os.makedirs("AccessibilityHelper/static", exist_ok=True)

# Create files with basic content
files = {
    "AccessibilityHelper/requirements.txt": """Flask==3.1.2
requests==2.32.5
python-dotenv==1.2.1
google-genai
""",
    "AccessibilityHelper/.env": "GEMINI_API_KEY=your_gemini_api_key_here\n",
    "AccessibilityHelper/app.py": "# Paste the app.py code here\n",
    "AccessibilityHelper/templates/index.html": "<!-- Paste index.html code here -->\n",
    "AccessibilityHelper/static/style.css": "/* Paste style.css code here */\n"
}

for path, content in files.items():
    with open(path, "w") as f:
        f.write(content)

print("Project files created successfully!")
