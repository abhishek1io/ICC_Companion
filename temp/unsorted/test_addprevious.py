"""Quick test of addprevious order."""
from docx.oxml import OxmlElement

body = OxmlElement('w:body')

def make_p(text):
    p = OxmlElement('w:p')
    r = OxmlElement('w:r')
    t = OxmlElement('w:t')
    t.text = text
    t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    r.append(t)
    p.append(r)
    return p

ns = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'

# Existing content
p0 = make_p('EXISTING')
body.append(p0)

# Reference (CHAPTER 8)
ref = make_p('CHAPTER 8')
body.append(ref)

# Elements to insert before ref
sp2 = make_p('sp2')
table = make_p('TABLE')
sp1 = make_p('sp1')
heading = make_p('HEADING')

# Insert in order [sp2, table, sp1, heading]
ref.addprevious(sp2)
ref.addprevious(table)
ref.addprevious(sp1)
ref.addprevious(heading)

print('Order after addprevious [sp2, table, sp1, heading]:')
for elem in body:
    texts = [t.text for t in elem.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text]
    print(f'  {elem.tag.split("}")[-1]}: {", ".join(texts)}')
