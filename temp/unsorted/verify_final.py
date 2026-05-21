from docx import Document
doc = Document(r'C:\xampp\htdocs\ICC_Companion\temp\ppt_and_report\my_report\ICC_Companion_v5.docx')
print(f'Total tables: {len(doc.tables)}')
print()

# Show all tables
for i, t in enumerate(doc.tables):
    rows = len(t.rows)
    cols = len(t.columns)
    first = t.rows[0].cells[0].text.strip()[:60]
    second = ''
    if len(t.rows) > 1:
        second = t.rows[1].cells[0].text.strip()[:35]
    print(f'Table[{i:2d}]: {rows:2d}r x {cols}c | "{first}" | e.g. "{second}"')

print()
# Show database section
print('Database section (paragraphs 295-340):')
for i in range(295, min(345, len(doc.paragraphs))):
    p = doc.paragraphs[i]
    if p.text.strip():
        print(f'  P[{i}]: "{p.text.strip()[:120]}"')
