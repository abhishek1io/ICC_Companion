"""Test addnext order too."""
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

# Existing content
p0 = make_p('EXISTING')
body.append(p0)

# Insert after p0
sp2 = make_p('sp2')
table = make_p('TABLE')
sp1 = make_p('sp1')
heading = make_p('HEADING')

# Insert in order [sp2, table, sp1, heading]
p0.addnext(sp2)
p0.addnext(table)
p0.addnext(sp1)
p0.addnext(heading)

print('Order after addnext [sp2, table, sp1, heading]:')
for elem in body:
    texts = [t.text for t in elem.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text]
    print(f'  {", ".join(texts)}')
