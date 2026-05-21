from docx import Document
doc = Document(r'C:\xampp\htdocs\ICC_Companion\temp\ppt_and_report\my_report\ICC_Companion_v5.docx')
print('=== SIX UPDATED TABLES (actual DB schema) ===\n')
targets = ['announcement_id', 'routine_id', 'resource_id', 'item_id', 'schedule_id', 'assignment_id']
for elem in doc.element.body:
    tag = elem.tag.split('}')[-1]
    if tag == 'tbl':
        try:
            rows = elem.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tr')
            if len(rows) > 1:
                tc = rows[1].find('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
                if tc is not None and tc.text and tc.text.strip() in targets:
                    name = tc.text.strip()
                    row_count = len(rows)
                    print(f'  Table: {name} ({row_count} fields)')
                    for ri, r in enumerate(rows):
                        cells = r.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tc')
                        vals = []
                        for c in cells:
                            t = c.find('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
                            vals.append(t.text[:25] if t is not None and t.text else '')
                        print(f'    {vals[0]:25s} {vals[1]:20s} {vals[2][:25]}')
                    print()
        except:
            pass
