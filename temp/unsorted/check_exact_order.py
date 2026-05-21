from docx import Document
from lxml import etree
doc = Document(r'C:\xampp\htdocs\ICC_Companion\temp\ppt_and_report\my_report\ICC_Companion_v5.docx')

# Print ALL body elements in order from lost_found to CHAPTER 8
print('Sequential body elements:')
capture = False
for elem in doc.element.body:
    tag = elem.tag.split('}')[-1]
    if tag == 'p':
        texts = [t.text for t in elem.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text]
        txt = ''.join(texts).strip()
        if 'Table 6:' in txt:
            capture = True
        if 'CHAPTER 8' in txt:
            print(f'  >>> CHAPTER 8 <<<')
            break
        if capture:
            if txt.startswith('Table ') or txt.startswith('CHAPTER'):
                print(f'  P(txt) -> "{txt[:60]}"')
            elif txt:
                print(f'  P -> "{txt[:60]}"')
    elif tag == 'tbl' and capture:
        try:
            rows = elem.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tr')
            if len(rows) > 1:
                tc = rows[1].find('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
                name = tc.text[:30] if tc is not None else '?'
                print(f'  TBL -> first data: "{name}"')
            else:
                print(f'  TBL -> (header only)')
        except:
            print(f'  TBL -> (error)')
