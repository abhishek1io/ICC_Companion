from docx import Document
doc = Document(r'C:\xampp\htdocs\ICC_Companion\temp\ppt_and_report\my_report\ICC_Companion_v5.docx')
print('Paragraphs 320-340:')
for i in range(320, min(345, len(doc.paragraphs))):
    p = doc.paragraphs[i]
    txt = p.text
    print(f'P[{i}]: "{txt}"')
print()
print('Check if docx loads correctly...')
print(f'Total paragraphs: {len(doc.paragraphs)}')
print(f'Total tables: {len(doc.tables)}')
print('All good!')
