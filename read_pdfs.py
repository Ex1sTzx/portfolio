import sys
try:
    import pypdf
except ImportError:
    print("pypdf not installed")
    sys.exit(1)

files = ['PortFolioWebsite.pdf', 'SamarthKajla_AI.pdf']
for f in files:
    print(f"\n=== {f} ===")
    try:
        reader = pypdf.PdfReader(f)
        text = ''
        for page in reader.pages:
            t = page.extract_text()
            if t: text += t + '\n'
        print(text)
    except Exception as e:
        print(f"Error reading {f}: {e}")
