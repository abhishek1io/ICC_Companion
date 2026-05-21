from docx import Document
doc = Document(r'C:\xampp\htdocs\ICC_Companion\temp\ppt_and_report\my_report\ICC_Companion_v5.docx')
for i, t in enumerate(doc.tables):
    print(f'=== Table {i} ({len(t.rows)}r x {len(t.columns)}c) ===')
    for ri, row in enumerate(t.rows):
        vals = [cell.text.strip()[:40] for cell in row.cells]
        print(f'  Row {ri}: {vals}')
    print()
