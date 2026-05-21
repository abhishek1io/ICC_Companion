from docx import Document
doc = Document(r'C:\xampp\htdocs\ICC_Companion\temp\ppt_and_report\my_report\ICC_Companion_v5.docx')
print(f'Total tables: {len(doc.tables)}')
print()
# Show all tables
for i, t in enumerate(doc.tables):
    rows = len(t.rows)
    cols = len(t.columns)
    first = t.rows[0].cells[0].text.strip()[:60] if rows > 0 else 'empty'
    second = t.rows[1].cells[0].text.strip()[:30] if rows > 1 else ''
    print(f'Table {i}: {rows}r x {cols}c | "{first}" | e.g. "{second}"')

print()
# Find all headings for database tables  
print('Database table headings in paragraphs:')
for i, p in enumerate(doc.paragraphs):
    txt = p.text.strip()
    if txt.startswith('Table ') and ('Field' not in txt) and len(txt) < 80:
        print(f'  P[{i}]: "{txt}"')

print()
print('Paragraphs 300-325 after fix:')
for i in range(300, 330):
    p = doc.paragraphs[i]
    txt = p.text
    print(f'P[{i}]: "{txt}"')
