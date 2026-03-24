import sys
try:
    import fitz # PyMuPDF
except ImportError:
    print("PyMuPDF not installed")
    sys.exit(1)

files = ['PortFolioWebsite.pdf', 'Samarth_AI.pdf']
for f in files:
    print(f"\n========== {f} ==========\n")
    try:
        doc = fitz.open(f)
        text = ""
        for page in doc:
            text += page.get_text() + "\n"
        print(text.strip())
    except Exception as e:
        print(f"Error reading {f}: {e}")
