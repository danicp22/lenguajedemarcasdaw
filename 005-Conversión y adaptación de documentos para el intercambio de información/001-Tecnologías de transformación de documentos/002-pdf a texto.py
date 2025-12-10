from pypdf import PdfReader

reader = PdfReader("librophp.pdf")
all_text = ""

for page in reader.pages:
    all_text += page.extract_text() + "\n"

print(all_text)