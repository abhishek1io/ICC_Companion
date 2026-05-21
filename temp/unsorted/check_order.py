from docx import Document
doc = Document(r'C:\xampp\htdocs\ICC_Companion\temp\ppt_and_report\my_report\ICC_Companion_v5.docx')

# Find the two paragraphs near Chapter 8
for i, p in enumerate(doc.paragraphs):
    txt = p.text.strip()
    if 'Table 7:' in txt:
        print(f'Found P[{i}]: "{txt}"')
    if 'Table 8:' in txt:
        print(f'Found P[{i}]: "{txt}"')
    if txt == 'CHAPTER 8':
        print(f'Found P[{i}]: "CHAPTER 8"')

# Check order in body by looking at all elements before CHAPTER 8
print('\nElements before CHAPTER 8 (by type):')
ch8_found = False
for elem in doc.element.body:
    tag = elem.tag.split('}')[-1]
    if tag == 'p':
        texts = [t.text for t in elem.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text]
        txt = ''.join(texts).strip()
        if txt:
            if txt == 'CHAPTER 8':
                ch8_found = True
                break
            if 'Table 7:' in txt or 'Table 8:' in txt:
                print(f'  BEFORE CH8: p - "{txt}"')
    elif tag == 'tbl':
        try:
            t_elem = elem.find('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
            first_text = t_elem.text if t_elem is not None else 'unknown'
            print(f'  BEFORE CH8: tbl - "{first_text[:40]}"')
        except:
            print(f'  BEFORE CH8: tbl')
