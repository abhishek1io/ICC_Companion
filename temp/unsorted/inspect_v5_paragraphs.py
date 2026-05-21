from docx import Document
doc = Document(r'C:\xampp\htdocs\ICC_Companion\temp\ppt_and_report\my_report\ICC_Companion_v5.docx')
# Look at paragraphs 295-330 to understand the database section structure
for i in range(290, min(340, len(doc.paragraphs))):
    p = doc.paragraphs[i]
    txt = p.text.strip()
    if txt:
        print(f'P[{i}]: "{txt[:120]}"')
