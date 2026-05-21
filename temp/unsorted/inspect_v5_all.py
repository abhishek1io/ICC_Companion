from docx import Document
doc = Document(r'C:\xampp\htdocs\ICC_Companion\temp\ppt_and_report\my_report\ICC_Companion_v5.docx')
for i in range(295, 330):
    p = doc.paragraphs[i]
    txt = p.text
    print(f'P[{i}]: "{txt}"')
