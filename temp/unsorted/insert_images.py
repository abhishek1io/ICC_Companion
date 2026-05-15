"""Insert diagrams and screenshots into the ICC Companion report."""
from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from copy import deepcopy
import os

import tempfile
src = r'C:\xampp\htdocs\ICC_Companion\temp\ppt_and_report\my_report\PROJECT_REPORT.docx'
out = os.path.join(tempfile.gettempdir(), 'ICC_FINAL_REPORT.docx')
img_dir = r'C:\xampp\htdocs\ICC_Companion\temp\ppt_and_report\my_report'

doc = Document(src)

def add_image_after(para, img_path, width_inches=5.5):
    """Add an image paragraph right after the target paragraph."""
    if not os.path.exists(img_path):
        return False
    
    # Create a new paragraph element (clone the current one, then clear)
    new_para_elem = deepcopy(para._element)
    for child in list(new_para_elem):
        new_para_elem.remove(child)
    
    # Create a new paragraph to get the run factory
    new_para = type(para)(new_para_elem, para._parent)
    
    # Add image to the new paragraph
    run = new_para.add_run()
    run.add_picture(img_path, width=Inches(width_inches))
    new_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # Insert after current paragraph
    para._element.addnext(new_para_elem)
    return True

# Build paragraph text -> paragraph object map
para_map = {}
for p in doc.paragraphs:
    t = p.text.strip()
    if t:
        para_map[t] = p

def insert_image(label_text, filename, width=5.5):
    """Find paragraph by text and insert image after it."""
    p = para_map.get(label_text)
    if p:
        path = os.path.join(img_dir, filename)
        if add_image_after(p, path, width):
            print(f"  [OK] {filename} after '{label_text[:40]}'")
        else:
            print(f"  [NOFILE] {filename}")
    else:
        print(f"  [NOTFOUND] '{label_text[:50]}'")

print("=== Diagrams ===")
insert_image('Figure 6.2 \u2014 DFD Level 0: Context Diagram', 'dfd_level0.png')
insert_image('Figure 6.3 \u2014 DFD Level 1: Detailed Process Flow', 'dfd_level1.png')
insert_image('Figure 6.5 \u2014 Entity-Relationship (ER) Diagram', 'er_diagram.png')

print("\n=== Screenshots (Public Pages) ===")
insert_image('HOME PAGE', 'screenshot_home.png')
insert_image('STUDENT LOGIN PAGE', 'screenshot_student_login.png')
insert_image('ADMIN LOGIN PAGE', 'screenshot_admin_login.png')

print("\n=== Screenshots (Student Portal) ===")
insert_image('STUDENT DASHBOARD', 'screenshot_student_dashboard.png')
insert_image('MY SUBJECTS PAGE', 'screenshot_subjects.png')
insert_image('MY ATTENDANCE PAGE', 'screenshot_attendance.png')
insert_image('EXAM TIMETABLE PAGE', 'screenshot_exams.png')
insert_image('LOST & FOUND PAGE', 'screenshot_lost_found.png')
insert_image('ANNOUNCEMENTS PAGE', 'screenshot_announcements.png')

print("\n=== Screenshots (Student Portal cont.) ===")
# The student announcements page wasn't in Ch9 - insert at the existing announcement section
insert_image('ANNOUNCEMENTS PAGE', 'screenshot_announcements.png')

print("\n=== Screenshots (Admin Portal) ===")
insert_image('ADMIN DASHBOARD', 'screenshot_admin_dashboard.png')
insert_image('MANAGE STUDENTS PAGE', 'screenshot_manage_students.png')
insert_image('ATTENDANCE MANAGEMENT PAGE', 'screenshot_manage_attendance.png')
insert_image('MANAGE EXAMS PAGE', 'screenshot_manage_exams.png')
insert_image('MANAGE ANNOUNCEMENTS PAGE', 'screenshot_manage_announcements.png')
insert_image('MANAGE FACULTY PAGE', 'screenshot_manage_faculty.png')

doc.save(out)
import shutil
final = r'C:\xampp\htdocs\ICC_Companion\temp\ppt_and_report\my_report\PROJECT_REPORT.docx'
shutil.copy2(out, final)
print(f"\nFinal report saved to: {final}")
print(f"File size: {os.path.getsize(final) / 1024:.1f} KB")
