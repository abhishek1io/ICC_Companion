#!/usr/bin/env python3
"""Generate ICC Companion Project Report - 53 pages matching reference format."""

from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml
import os

doc = Document()

# Page setup
for section in doc.sections:
    section.top_margin = Cm(2.54)
    section.bottom_margin = Cm(2.54)
    section.left_margin = Cm(3.17)
    section.right_margin = Cm(3.17)

style = doc.styles['Normal']
font = style.font
font.name = 'Times New Roman'
font.size = Pt(12)
style.paragraph_format.line_spacing = 1.5

def add_heading_numbered(text, level=1):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.color.rgb = RGBColor(0, 0, 0)
    return h

def add_page_break():
    doc.add_page_break()

def add_para(text, bold=False, italic=False, size=12, align=None, space_after=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    if align:
        p.alignment = align
    run = p.add_run(text)
    run.font.size = Pt(size)
    run.font.name = 'Times New Roman'
    run.bold = bold
    run.italic = italic
    return p

def add_body(text):
    p = doc.add_paragraph(text)
    p.paragraph_format.first_line_indent = Cm(1.27)
    p.paragraph_format.space_after = Pt(6)
    for run in p.runs:
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
    return p

def add_bullet(text):
    p = doc.add_paragraph(text, style='List Bullet')
    p.paragraph_format.space_after = Pt(3)
    for run in p.runs:
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
    return p

def add_table(headers, data, col_widths=None):
    table = doc.add_table(rows=1+len(data), cols=len(headers))
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = ''
        p = cell.paragraphs[0]
        run = p.add_run(h)
        run.bold = True
        run.font.size = Pt(11)
        run.font.name = 'Times New Roman'
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="D9E2F3"/>')
        cell._tc.get_or_add_tcPr().append(shading)
    for r_idx, row_data in enumerate(data):
        for c_idx, val in enumerate(row_data):
            cell = table.rows[r_idx+1].cells[c_idx]
            cell.text = ''
            p = cell.paragraphs[0]
            run = p.add_run(str(val))
            run.font.size = Pt(11)
            run.font.name = 'Times New Roman'
    return table

# ===================== COVER PAGE =====================
add_para('', size=12, space_after=60)
add_para('A PROJECT REPORT ON', bold=True, size=18, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24)
add_para('"ICC COMPANION"', bold=True, size=22, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24)
add_para('(Icon Commerce College Campus Portal)', size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=30)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('A Project Report in partial fulfilment of the requirement for the degree of')
run.font.size = Pt(12)
run.font.name = 'Times New Roman'
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('Bachelor of Computer Application')
run.bold = True
run.font.size = Pt(14)
run.font.name = 'Times New Roman'

add_para('Under GAUHATI UNIVERSITY', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=40)

# Guide and student info table
info_table = doc.add_table(rows=2, cols=2)
info_table.alignment = WD_TABLE_ALIGNMENT.CENTER
# Row 0
info_table.rows[0].cells[0].text = ''
p = info_table.rows[0].cells[0].paragraphs[0]
run = p.add_run('Name of the Guide:')
run.bold = True
run.font.size = Pt(12)
run.font.name = 'Times New Roman'
p2 = info_table.rows[0].cells[0].add_paragraph()
run2 = p2.add_run('Manas Chakraborty, Asst. Prof')
run2.font.size = Pt(12)
run2.font.name = 'Times New Roman'
p3 = info_table.rows[0].cells[0].add_paragraph()
run3 = p3.add_run('Department:')
run3.bold = True
run3.font.size = Pt(12)
run3.font.name = 'Times New Roman'
p4 = info_table.rows[0].cells[0].add_paragraph()
run4 = p4.add_run('Bachelor of Computer Application')
run4.font.size = Pt(12)
run4.font.name = 'Times New Roman'
p5 = info_table.rows[0].cells[0].add_paragraph()
run5 = p5.add_run('ICON Commerce College')
run5.font.size = Pt(12)
run5.font.name = 'Times New Roman'

info_table.rows[0].cells[1].text = ''
p = info_table.rows[0].cells[1].paragraphs[0]
run = p.add_run('Submitted By:')
run.bold = True
run.font.size = Pt(12)
run.font.name = 'Times New Roman'
p2 = info_table.rows[0].cells[1].add_paragraph()
run2 = p2.add_run('Abhishek Sharma')
run2.font.size = Pt(12)
run2.font.name = 'Times New Roman'
p3 = info_table.rows[0].cells[1].add_paragraph()
run3 = p3.add_run('Roll No: UT-231-049-0004')
run3.font.size = Pt(12)
run3.font.name = 'Times New Roman'
p4 = info_table.rows[0].cells[1].add_paragraph()
run4 = p4.add_run('Registration No: 23084891')
run4.font.size = Pt(12)
run4.font.name = 'Times New Roman'

# Merge bottom row
info_table.rows[1].cells[0].merge(info_table.rows[1].cells[1])
info_table.rows[1].cells[0].text = ''
p = info_table.rows[1].cells[0].paragraphs[0]
run = p.add_run('BCA 6th Semester (FYUGP)')
run.bold = True
run.font.size = Pt(12)
run.font.name = 'Times New Roman'
p.alignment = WD_ALIGN_PARAGRAPH.CENTER

add_para('', size=12, space_after=20)
add_para('Guwahati-781003', size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
add_para('ICON Commerce College', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER)

# ===================== CERTIFICATE =====================
add_page_break()
add_para('CERTIFICATE', bold=True, size=18, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24)

add_body('This is to certify that the project entitled "ICC COMPANION" has been submitted by Abhishek Sharma (Roll No: UT-231-049-0004, Registration No: 23084891) in partial fulfilment of the requirements for the degree of Bachelor of Computer Applications (BCA), 6th Semester, at Icon Commerce College, Gauhati University, during the Academic Session 2025\u201326.')

add_body('This is an authentic work carried out by him under my supervision and guidance. The project has not been submitted to any other university or institution for the award of any degree or diploma.')

add_para('', space_after=12)
add_para('Date: ____________________', size=12, space_after=24)
add_para('Name of the Guide: Manas Chakraborty', size=12, space_after=6)
add_para('Designation: Assistant Professor', size=12, space_after=6)
add_para('Department: Bachelor of Computer Application', size=12, space_after=6)
add_para('Institution: Icon Commerce College', size=12, space_after=6)
add_para('Guwahati \u2013 781021', size=12, space_after=24)
add_para('Signature of the Guide: ____________________', size=12)

# ===================== DECLARATION =====================
add_page_break()
add_para('DECLARATION', bold=True, size=18, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24)

add_body('I hereby declare that the project report \u201cICC Companion\u201d, submitted in partial fulfilment of the requirement for the degree of Bachelor of Computer Application (BCA) in Icon Commerce College, under Gauhati University, is my original work and has not been submitted for the award of any other degree, diploma, fellowship or any other similar titles.')

add_para('', space_after=12)
add_para('Date: ____________________', size=12, space_after=6)
add_para('Signature: ________________', size=12, space_after=24)
add_para('Place: Guwahati', size=12, space_after=6)
add_para('NAME: ABHISHEK SHARMA', size=12, space_after=6)
add_para('ROLL NO: UT-231-049-0004', size=12, space_after=6)
add_para('REGISTRATION NO: 23084891', size=12, space_after=6)
add_para('DEPARTMENT: BCA 6TH SEMESTER', size=12, space_after=6)
add_para('ICON COMMERCE COLLEGE', size=12)

# ===================== ACKNOWLEDGEMENT =====================
add_page_break()
add_para('ACKNOWLEDGEMENT', bold=True, size=18, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24)

add_body('First of all, I would like to express my special thanks of gratitude to my project guide and mentor Manas Chakraborty for instilling confidence in me and providing me with invaluable comments and criticism on many issues and constant rendering of timely advice and sparing valuable time throughout my project work.')

add_body('It is my honour to thank Dr. Mandira Saha, Principal of Icon Commerce College and Tridib Kr. Handique, Co-Ordinator of B.C.A of Icon Commerce College for providing all the facilities and permission to undertake this project work. I would also like to thank the whole B.C.A department without whose help success could not have been attained.')

add_body('My heartfelt gratitude goes to all those who agreed to participate in this project, for their time expended and for sharing insights and suggestions.')

add_body('Finally, I would like to thank my parents and friends who helped a lot in finalizing this project within limited time frame.')

add_para('', space_after=12)
add_para('Place: Guwahati', size=12, space_after=6)
add_para('Date: ____________________', size=12, space_after=6)
add_para('Name: Abhishek Sharma', size=12, space_after=6)
add_para('Roll No: UT-231-049-0004', size=12, space_after=6)
add_para('Registration No: 23084891', size=12, space_after=6)
add_para('BCA 6th Semester, Icon Commerce College', size=12)

# ===================== ABSTRACT =====================
add_page_break()
add_para('ABSTRACT', bold=True, size=18, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24)

add_body('ICC Companion (Icon Commerce College Campus Portal) is a comprehensive web-based college management system developed using PHP, MySQL, HTML5, CSS3, and JavaScript. The system is designed to digitize and simplify campus life for both students and staff by providing real-time access to academic data, attendance, and campus-wide communications.')

add_body('The system provides two separate portals \u2014 a Student Portal and an Admin Portal \u2014 with independent session-based authentication. Students can log in using their roll number and date of birth to access attendance records with visual progress trackers, view exam timetables with countdown timers, browse college announcements, use the Lost & Found portal, and access academic resources such as class routines.')

add_body('Administrators have access to a powerful control center with a Student Information System for full CRUD operations on student profiles, a Smart Attendance Marker for marking daily attendance, an Exam Controller for scheduling examinations, a Global Communications module for posting announcements, a Lost & Found Manager, and a Dynamic File Manager for uploading class routines and exam schedules.')

add_body('The system employs a well-structured MySQL relational database named campus_portal with 12 core tables including departments, subjects, students, admins, attendance, exams, lost_found, announcements, class_routines, exam_schedules, resources, and faculty_subjects. Security is ensured through PHP session management, SQL injection prevention via MySQLi prepared statements, and input sanitization.')

add_body('The system is deployable on any standard Apache server environment such as XAMPP and follows a mobile-first responsive design for accessibility across devices.')

# ===================== TABLE OF CONTENTS =====================
add_page_break()
add_para('CONTENTS', bold=True, size=18, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24)

toc_items = [
    ('Chapter 1: Introduction', '1-3'),
    ('    1.1 Background', '2'),
    ('    1.2 Problem Statement', '2'),
    ('    1.3 Proposed Solution', '3'),
    ('Chapter 2: REQUIREMENT SPECIFICATION', '4-6'),
    ('    2.1 System Requirements', '5'),
    ('    2.2 Technologies Used', '5-6'),
    ('Chapter 3: Object of the Project', '7-8'),
    ('Chapter 4: Scope of the Project', '9-11'),
    ('Chapter 5: System Analysis', '12-14'),
    ('    5.1 Existing System', '13'),
    ('    5.2 Proposed System', '13'),
    ('    5.3 Feasibility Study', '14'),
    ('Chapter 6: System Design', '15-20'),
    ('    6.1 System Architecture', '16'),
    ('    6.2 Data Flow Diagram (Level 0)', '17'),
    ('    6.3 Data Flow Diagram (Level 1)', '18'),
    ('    6.4 Use Case Diagram', '19'),
    ('    6.5 ER Diagram', '20'),
    ('Chapter 7: Database Design', '21-24'),
    ('Chapter 8: Implementation / Working', '25-29'),
    ('Chapter 9: Sample Screenshots', '30-38'),
    ('Chapter 10: Advantages & Limitations', '39-41'),
    ('Chapter 11: Future Enhancements', '42-44'),
    ('Chapter 12: Conclusion', '45-47'),
]

for item, page in toc_items:
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.tab_stops.add_tab_stop(Cm(15))
    is_chapter = not item.startswith('    ')
    run = p.add_run(item)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run.bold = is_chapter
    run2 = p.add_run('\t' + page)
    run2.font.name = 'Times New Roman'
    run2.font.size = Pt(12)

# ===================== CHAPTER 1: INTRODUCTION =====================
add_page_break()
add_para('Chapter 1', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
add_para('INTRODUCTION', bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('1', bold=True, size=12, align=WD_ALIGN_PARAGRAPH.RIGHT)

add_page_break()
add_heading_numbered('1.1 Background', level=2)
add_body('In modern educational institutions, students and faculty interact with numerous administrative processes on a daily basis \u2014 attendance tracking, examination scheduling, announcement dissemination, resource sharing, and grievance handling. Traditionally, many of these processes have been managed through manual, paper-based methods or through disparate systems that do not communicate with one another.')

add_body('With the widespread adoption of web-based technologies in the education sector, it has become practical to develop an integrated campus portal that consolidates all academic and administrative functions into a single, user-friendly platform. A well-designed campus management system provides a centralized, transparent, and efficient digital environment where students can access their academic data in real time and administrators can manage institutional workflows systematically.')

add_body('Icon Commerce College, affiliated with Gauhati University, offers multiple undergraduate programmes including BCA, BBA, BA, and B.COM across six semesters. The need for a unified digital platform to serve the diverse needs of students and staff across these departments formed the motivation for this project.')

add_heading_numbered('1.2 Problem Statement', level=2)
add_body('The absence of a structured, integrated digital platform in the college leads to several issues:')
add_bullet('Attendance records are maintained manually or through disconnected spreadsheets, making it difficult for students to track their attendance in real time.')
add_bullet('Exam schedules and class routines are communicated through physical notices that can be missed or misplaced.')
add_bullet('College announcements and important notices are disseminated through informal channels without a permanent, searchable record.')
add_bullet('The Lost & Found process relies on physical notice boards with no centralized inventory or tracking mechanism.')
add_bullet('Administrators have no consolidated view of student data, attendance patterns, or academic schedules.')
add_bullet('There is no standardized platform for managing academic resources such as syllabi, books, and study materials.')
add_bullet('Students and staff have to navigate multiple offline and online channels to access routine information.')

add_heading_numbered('1.3 Proposed Solution', level=2)
add_body('ICC Companion is a web-based campus portal developed using PHP and MySQL. It provides a comprehensive, integrated platform where students can log in using their roll number and date of birth to view attendance records, exam timetables, announcements, Lost & Found listings, and academic resources. Administrators log into a separate management panel where they can manage student records, mark attendance, schedule exams, post announcements, manage Lost & Found items, and upload class routines.')

add_body('The system is designed with a mobile-first responsive approach, ensuring accessibility on smartphones, tablets, and desktop computers. By consolidating all campus services into a single portal, the system improves transparency, efficiency, and communication across the institution.')

# ===================== CHAPTER 2: REQUIREMENT SPECIFICATION =====================
add_page_break()
add_para('Chapter 2', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
add_para('REQUIREMENT SPECIFICATION', bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('4', bold=True, size=12, align=WD_ALIGN_PARAGRAPH.RIGHT)

add_page_break()
add_heading_numbered('2.1 System Requirements', level=2)
p = doc.add_paragraph()
run = p.add_run('Hardware Requirements')
run.bold = True
run.font.size = Pt(12)
run.font.name = 'Times New Roman'

add_table(
    ['Component', 'Minimum Specification'],
    [
        ('Processor', 'Intel Core i3 or equivalent'),
        ('RAM', '4 GB or higher'),
        ('Storage', '20 GB available disk space'),
        ('Network', 'Internet connection for hosting / local network for LAN'),
    ]
)

add_heading_numbered('2.2 Technologies Used', level=2)
add_body('The following technologies were used in the development of ICC Companion:')

add_table(
    ['Technology', 'Version / Detail', 'Role in Project'],
    [
        ('PHP', '7.4+', 'Server-side scripting \u2014 handles form processing, session management, database interaction, file uploads, and authentication logic.'),
        ('MySQL', '5.7+', 'Relational database \u2014 stores all data: students, admins, departments, subjects, attendance, exams, lost_found, announcements, routines, and resources.'),
        ('mysqli (PHP Extension)', '\u2014', 'Used for database connectivity, prepared statements, and parameterized queries to prevent SQL injection.'),
        ('HTML5', '\u2014', 'Provides semantic structure for all web pages \u2014 login, dashboards, forms, tables, and portals.'),
        ('CSS3', '\u2014', 'Provides responsive styling, layout, sidebar navigation, cards, badges, forms, and mobile-first design.'),
        ('JavaScript (Vanilla)', '\u2014', 'Client-side logic \u2014 form validation, modal control, Fetch API for AJAX, dynamic content loading, sidebar toggle, search/filter functionality.'),
        ('Font Awesome', '6.4.0 (CDN)', 'Icon library used throughout the interface for navigation icons, stat cards, and buttons.'),
        ('Apache Web Server', 'XAMPP', 'Local server environment for running PHP and serving the web application.'),
        ('Session Management', 'PHP Sessions', 'Used to maintain authenticated state for both students and administrators across pages.'),
    ]
)

# ===================== CHAPTER 3: OBJECT OF THE PROJECT =====================
add_page_break()
add_para('Chapter 3', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
add_para('OBJECT OF THE PROJECT', bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('7', bold=True, size=12, align=WD_ALIGN_PARAGRAPH.RIGHT)

add_page_break()
add_body('The primary objectives of the ICC Companion project are:')

objectives = [
    'To provide students with a dedicated online portal to view their attendance records with real-time progress tracking and automatic eligibility calculations.',
    'To display exam timetables for Sessional and Final exams with countdown timers, ensuring students never miss an examination.',
    'To provide a centralized announcements feed for college notices, events, and holidays with department/semester targeting.',
    'To implement a Lost & Found portal where students can browse items and report new lost items.',
    'To provide access to academic resources including digital class routines and exam schedules in PDF/image formats.',
    'To enable college administrators to perform full CRUD operations on student profiles through a Student Information System.',
    'To provide a Smart Attendance Marker with a checkbox-based interface for marking daily attendance for entire classes.',
    'To enable administrators to manage the academic calendar by scheduling exams across departments and semesters.',
    'To provide a Global Communications module for posting, editing, and deleting announcements targeted at specific departments or semesters.',
    'To implement a Lost & Found Manager for reviewing reported items, managing listings, and marking items as claimed.',
    'To provide a Dynamic File Manager for uploading and updating class routines and exam schedules.',
    'To ensure system security through session-based authentication, input sanitization, and SQL injection prevention via prepared statements.',
]

for obj in objectives:
    add_bullet(obj)

# ===================== CHAPTER 4: SCOPE OF THE PROJECT =====================
add_page_break()
add_para('Chapter 4', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
add_para('SCOPE OF THE PROJECT', bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('9', bold=True, size=12, align=WD_ALIGN_PARAGRAPH.RIGHT)

add_page_break()
add_body('ICC Companion is scoped to serve the campus management needs of Icon Commerce College. The system serves two types of users \u2014 students and administrators \u2014 through separate, secure portals.')

p = doc.add_paragraph()
run = p.add_run('4.1 What is In Scope:')
run.bold = True
run.font.size = Pt(12)
run.font.name = 'Times New Roman'

in_scope = [
    'Student login using roll number and date of birth with session-based authentication.',
    'Student dashboard with attendance progress bars and eligibility calculations (classes you can miss / classes needed).',
    'Exam timetable display with Sessional and Final exam schedules and countdown timers.',
    'Centralized announcements feed for college notices and events.',
    'Lost & Found browsing and reporting functionality for students.',
    'Academic resources access including class routines and exam schedules.',
    'Admin login with username and password authentication.',
    'Admin dashboard with quick access to all management modules.',
    'Student Information System (SIS) with full CRUD operations for student profiles.',
    'Smart Attendance Marker with checkbox interface for quick attendance recording.',
    'Exam Controller for scheduling exams across departments and semesters.',
    'Global Communications module for posting, editing, and deleting announcements.',
    'Lost & Found Manager for reviewing, managing, and claiming items.',
    'Dynamic File Manager for uploading and managing class routines and exam schedules.',
    'Role-based admin access (super-admin, staff, faculty) with different permission levels.',
]
for item in in_scope:
    add_bullet(item)

p = doc.add_paragraph()
run = p.add_run('4.2 What is Out of Scope:')
run.bold = True
run.font.size = Pt(12)
run.font.name = 'Times New Roman'

out_scope = [
    'The system does not currently send automated email or SMS notifications.',
    'The system is designed for a single college and does not support multi-campus configurations.',
    'No companion mobile application exists \u2014 the system is browser-based only (mobile-responsive).',
    'No real-time chat feature is implemented.',
    'No fee management or payment gateway integration is included.',
    'No online examination or quiz functionality is implemented.',
]
for item in out_scope:
    add_bullet(item)

# ===================== CHAPTER 5: SYSTEM ANALYSIS =====================
add_page_break()
add_para('Chapter 5', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
add_para('SYSTEM ANALYSIS', bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('12', bold=True, size=12, align=WD_ALIGN_PARAGRAPH.RIGHT)

add_page_break()
add_heading_numbered('5.1 Existing System', level=2)
add_body('In most colleges, campus information and academic data are currently managed through one or more of the following informal methods:')
add_bullet('Students physically visit notice boards to check exam schedules, class routines, and announcements.')
add_bullet('Attendance records are maintained in registers or disconnected spreadsheets that are not accessible to students.')
add_bullet('Lost & Found items are managed through physical notice boards with no centralized tracking.')
add_bullet('Academic resources are distributed through email or printed handouts without a centralized repository.')
add_bullet('Student records are managed through standalone software or paper files that require manual updates.')

add_body('These approaches have clear shortcomings \u2014 information can be missed, there is no real-time access for students, there is no consolidated view for administrators, and recurring issues cannot be identified from aggregate data.')

add_heading_numbered('5.2 Proposed System', level=2)
add_body('The proposed ICC Companion system replaces the fragmented approach with a unified web-based platform. Key improvements over the existing approach include:')
add_bullet('All academic data is stored digitally in a MySQL database with permanent audit trails.')
add_bullet('Students can view attendance, timetables, and announcements 24/7 from any device with a browser.')
add_bullet('Attendance is calculated automatically with visual progress bars and eligibility indicators.')
add_bullet('Administrators have a consolidated dashboard for managing all aspects of campus operations.')
add_bullet('Lost & Found items are tracked digitally with categories and status indicators.')
add_bullet('Academic resources are stored and organized in a centralized file management system.')

add_heading_numbered('5.3 Feasibility Study', level=2)

p = doc.add_paragraph()
run = p.add_run('Technical Feasibility')
run.bold = True
run.font.size = Pt(12)
run.font.name = 'Times New Roman'

add_body('The system is built using well-established and freely available technologies \u2014 PHP, MySQL, HTML5, CSS3, and JavaScript \u2014 that can be hosted on any standard Apache/XAMPP server. No proprietary software or special hardware is required, making it technically feasible for any college with a basic server setup.')

p = doc.add_paragraph()
run = p.add_run('Economic Feasibility')
run.bold = True
run.font.size = Pt(12)
run.font.name = 'Times New Roman'

add_body('All technologies used (PHP, MySQL, Apache) are open-source and free of cost. The system requires only a standard shared or local server, resulting in minimal operational cost. This makes the system highly economically feasible for educational institutions.')

p = doc.add_paragraph()
run = p.add_run('Operational Feasibility')
run.bold = True
run.font.size = Pt(12)
run.font.name = 'Times New Roman'

add_body('The system is designed with a clean, intuitive interface for both students and administrators. Students can easily log in and navigate through their dashboard. Administrators can manage all operations without specialized technical training, making the system fully operationally feasible.')

# ===================== CHAPTER 6: SYSTEM DESIGN =====================
add_page_break()
add_para('Chapter 6', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
add_para('SYSTEM DESIGN', bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('15', bold=True, size=12, align=WD_ALIGN_PARAGRAPH.RIGHT)

add_page_break()
add_heading_numbered('6.1 System Architecture', level=2)
add_body('The system follows a three-tier client-server architecture: a Presentation Layer (HTML/CSS/JavaScript in the browser), an Application Layer (PHP running on Apache), and a Data Layer (MySQL database). The student and admin portals share the same database but use independent authentication mechanisms.')

add_para('')
add_para('[System Architecture Diagram]', align=WD_ALIGN_PARAGRAPH.CENTER)

add_para('')
p = doc.add_paragraph()
run = p.add_run('Figure 6.1 \u2014 System Architecture Diagram')
run.italic = True
run.font.size = Pt(11)
run.font.name = 'Times New Roman'
p.alignment = WD_ALIGN_PARAGRAPH.CENTER

add_page_break()
add_heading_numbered('6.2 Data Flow Diagram \u2014 Level 0 (Context Diagram)', level=2)
add_body('The Level 0 DFD represents the system as a single process with two external entities \u2014 the Student and the Administrator \u2014 showing the high-level flow of data in and out of the system.')

add_para('[DFD Level 0: Context Diagram]', align=WD_ALIGN_PARAGRAPH.CENTER)
p = doc.add_paragraph()
run = p.add_run('Figure 6.2 \u2014 DFD Level 0: Context Diagram')
run.italic = True
run.font.size = Pt(11)
run.font.name = 'Times New Roman'
p.alignment = WD_ALIGN_PARAGRAPH.CENTER

add_page_break()
add_heading_numbered('6.3 Data Flow Diagram \u2014 Level 1 (Detailed)', level=2)
add_body('The Level 1 DFD breaks the system into major processes: Student Authentication, Attendance Viewing, Timetable Viewing, Announcement Browsing, Lost & Found Management, Admin Authentication, Student Management, Attendance Marking, Exam Scheduling, Announcement Management, and File Management \u2014 each connected to the relevant data stores.')

add_para('[DFD Level 1: Detailed Process Flow]', align=WD_ALIGN_PARAGRAPH.CENTER)
p = doc.add_paragraph()
run = p.add_run('Figure 6.3 \u2014 DFD Level 1: Detailed Process Flow')
run.italic = True
run.font.size = Pt(11)
run.font.name = 'Times New Roman'
p.alignment = WD_ALIGN_PARAGRAPH.CENTER

add_heading_numbered('6.4 Use Case Diagram', level=2)
add_body('The Use Case Diagram shows all the actions available to each actor (Student and Administrator) and the boundary of the system.')

add_para('[Use Case Diagram]', align=WD_ALIGN_PARAGRAPH.CENTER)
p = doc.add_paragraph()
run = p.add_run('Figure 6.4 \u2014 Use Case Diagram')
run.italic = True
run.font.size = Pt(11)
run.font.name = 'Times New Roman'
p.alignment = WD_ALIGN_PARAGRAPH.CENTER

add_page_break()
add_heading_numbered('6.5 Entity-Relationship (ER) Diagram', level=2)
add_body('The ER Diagram shows the database entities and their relationships. The central entities include students, departments, subjects, attendance, exams, lost_found, announcements, class_routines, and admins. Students are linked to departments and attendance records. Subjects are linked to departments. Attendance links students to subjects with date and status.')

add_para('[Entity-Relationship (ER) Diagram]', align=WD_ALIGN_PARAGRAPH.CENTER)
p = doc.add_paragraph()
run = p.add_run('Figure 6.5 \u2014 Entity-Relationship (ER) Diagram')
run.italic = True
run.font.size = Pt(11)
run.font.name = 'Times New Roman'
p.alignment = WD_ALIGN_PARAGRAPH.CENTER

# ===================== CHAPTER 7: DATABASE DESIGN =====================
add_page_break()
add_para('Chapter 7', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
add_para('DATABASE DESIGN', bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('21', bold=True, size=12, align=WD_ALIGN_PARAGRAPH.RIGHT)

add_page_break()
add_body('The database is named campus_portal and consists of multiple tables. All tables are in MySQL with proper data types, primary keys, unique constraints, and foreign key relationships where applicable.')

add_para('Table 1: departments', bold=True, size=12)
add_table(
    ['Field Name', 'Data Type', 'Constraint', 'Description'],
    [
        ('dept_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique department ID'),
        ('dept_code', 'VARCHAR(10)', 'UNIQUE, NOT NULL', 'Department code (e.g., BCA, BBA)'),
        ('dept_name', 'VARCHAR(100)', 'NOT NULL', 'Full department name'),
        ('created_at', 'TIMESTAMP', 'DEFAULT NOW()', 'Creation timestamp'),
    ]
)

add_para('Table 2: subjects', bold=True, size=12)
add_table(
    ['Field Name', 'Data Type', 'Constraint', 'Description'],
    [
        ('subject_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique subject ID'),
        ('subject_code', 'VARCHAR(20)', 'NOT NULL', 'Subject code'),
        ('subject_name', 'VARCHAR(100)', 'NOT NULL', 'Subject name'),
        ('dept_code', 'VARCHAR(10)', 'FK \u2192 departments(dept_code)', 'Department offering the subject'),
        ('semester', 'INT', 'NOT NULL', 'Semester number'),
        ('created_at', 'TIMESTAMP', 'DEFAULT NOW()', 'Creation timestamp'),
    ]
)

add_page_break()
add_para('Table 3: students', bold=True, size=12)
add_table(
    ['Field Name', 'Data Type', 'Constraint', 'Description'],
    [
        ('student_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique student record ID'),
        ('roll_number', 'VARCHAR(20)', 'UNIQUE, NOT NULL', 'Roll number (used for login)'),
        ('full_name', 'VARCHAR(100)', 'NOT NULL', 'Full name of the student'),
        ('email', 'VARCHAR(100)', 'NULL', 'Email address'),
        ('dob', 'DATE', 'NOT NULL', 'Date of birth (used as password)'),
        ('dept_code', 'VARCHAR(10)', 'FK \u2192 departments(dept_code)', 'Student\'s department'),
        ('semester', 'INT', 'NOT NULL', 'Current semester'),
        ('created_at', 'TIMESTAMP', 'DEFAULT NOW()', 'Registration timestamp'),
    ]
)

add_para('Table 4: admins', bold=True, size=12)
add_table(
    ['Field Name', 'Data Type', 'Constraint', 'Description'],
    [
        ('admin_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique admin record ID'),
        ('username', 'VARCHAR(50)', 'UNIQUE, NOT NULL', 'Admin username for login'),
        ('password', 'VARCHAR(255)', 'NOT NULL', 'Hashed password'),
        ('role', 'VARCHAR(20)', 'DEFAULT \'staff\'', 'Admin role (super-admin/staff/faculty)'),
        ('created_at', 'TIMESTAMP', 'DEFAULT NOW()', 'Account creation timestamp'),
    ]
)

add_para('Table 5: attendance', bold=True, size=12)
add_table(
    ['Field Name', 'Data Type', 'Constraint', 'Description'],
    [
        ('attendance_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique attendance record ID'),
        ('roll_number', 'VARCHAR(20)', 'FK \u2192 students(roll_number)', 'Student roll number'),
        ('subject_id', 'INT', 'FK \u2192 subjects(subject_id)', 'Subject for attendance'),
        ('attendance_date', 'DATE', 'NOT NULL', 'Date of class'),
        ('status', 'ENUM(\'Present\',\'Absent\')', 'NOT NULL', 'Attendance status'),
        ('created_at', 'TIMESTAMP', 'DEFAULT NOW()', 'Record creation timestamp'),
        ('UNIQUE', '(roll_number, subject_id, attendance_date)', '\u2014', 'Prevents duplicate entries'),
    ]
)

add_page_break()
add_para('Table 6: exams', bold=True, size=12)
add_table(
    ['Field Name', 'Data Type', 'Constraint', 'Description'],
    [
        ('exam_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique exam record ID'),
        ('subject_id', 'INT', 'FK \u2192 subjects(subject_id)', 'Subject for exam'),
        ('exam_date', 'DATE', 'NOT NULL', 'Date of examination'),
        ('exam_type', 'VARCHAR(20)', 'NOT NULL', 'Sessional / Final'),
        ('start_time', 'TIME', 'NULL', 'Exam start time'),
        ('end_time', 'TIME', 'NULL', 'Exam end time'),
        ('created_at', 'TIMESTAMP', 'DEFAULT NOW()', 'Creation timestamp'),
    ]
)

add_para('Table 7: lost_found', bold=True, size=12)
add_table(
    ['Field Name', 'Data Type', 'Constraint', 'Description'],
    [
        ('item_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique item ID'),
        ('title', 'VARCHAR(255)', 'NOT NULL', 'Item title'),
        ('description', 'TEXT', 'NULL', 'Item description'),
        ('item_type', 'ENUM(\'Lost\',\'Found\')', 'NOT NULL', 'Lost or Found'),
        ('status', 'VARCHAR(20)', 'DEFAULT \'Pending\'', 'Pending / Claimed'),
        ('reported_by', 'VARCHAR(100)', 'NULL', 'Name of reporter'),
        ('image_url', 'VARCHAR(255)', 'NULL', 'Item image path'),
        ('created_at', 'TIMESTAMP', 'DEFAULT NOW()', 'Submission timestamp'),
    ]
)

add_para('Table 8: announcements', bold=True, size=12)
add_table(
    ['Field Name', 'Data Type', 'Constraint', 'Description'],
    [
        ('announcement_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique announcement ID'),
        ('title', 'VARCHAR(255)', 'NOT NULL', 'Announcement title'),
        ('content', 'TEXT', 'NOT NULL', 'Announcement content'),
        ('priority', 'ENUM(\'High\',\'Medium\',\'Low\')', 'DEFAULT \'Medium\'', 'Priority level'),
        ('target_dept', 'VARCHAR(10)', 'NULL', 'Target department (null = all)'),
        ('target_semester', 'INT', 'NULL', 'Target semester (null = all)'),
        ('image_url', 'VARCHAR(255)', 'NULL', 'Announcement image'),
        ('created_at', 'TIMESTAMP', 'DEFAULT NOW()', 'Posting timestamp'),
    ]
)

add_page_break()
add_para('Table 9: class_routines', bold=True, size=12)
add_table(
    ['Field Name', 'Data Type', 'Constraint', 'Description'],
    [
        ('routine_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique routine ID'),
        ('dept_code', 'VARCHAR(10)', 'FK \u2192 departments(dept_code)', 'Department'),
        ('semester', 'INT', 'NOT NULL', 'Semester'),
        ('file_url', 'VARCHAR(255)', 'NOT NULL', 'Routine file path'),
        ('created_at', 'TIMESTAMP', 'DEFAULT NOW()', 'Upload timestamp'),
    ]
)

add_para('Table 10: exam_schedules', bold=True, size=12)
add_table(
    ['Field Name', 'Data Type', 'Constraint', 'Description'],
    [
        ('schedule_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique schedule ID'),
        ('dept_code', 'VARCHAR(10)', 'FK \u2192 departments(dept_code)', 'Department'),
        ('semester', 'INT', 'NOT NULL', 'Semester'),
        ('schedule_type', 'VARCHAR(20)', 'UNIQUE', 'Sessional / Final / Comprehensive'),
        ('file_url', 'VARCHAR(255)', 'NOT NULL', 'Schedule file path'),
        ('created_at', 'TIMESTAMP', 'DEFAULT NOW()', 'Upload timestamp'),
    ]
)

add_para('Table 11: resources', bold=True, size=12)
add_table(
    ['Field Name', 'Data Type', 'Constraint', 'Description'],
    [
        ('resource_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique resource ID'),
        ('title', 'VARCHAR(255)', 'NOT NULL', 'Resource title'),
        ('resource_type', 'ENUM(...)', 'NOT NULL', 'syllabus/book/material/link/text/others'),
        ('dept_code', 'VARCHAR(10)', 'FK', 'Department'),
        ('subject_id', 'INT', 'FK', 'Subject (optional)'),
        ('file_url', 'VARCHAR(255)', 'NULL', 'File path or external URL'),
        ('created_at', 'TIMESTAMP', 'DEFAULT NOW()', 'Upload timestamp'),
    ]
)

add_para('Table 12: faculty_subjects', bold=True, size=12)
add_table(
    ['Field Name', 'Data Type', 'Constraint', 'Description'],
    [
        ('assignment_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique assignment ID'),
        ('admin_id', 'INT', 'FK \u2192 admins(admin_id)', 'Faculty/admin assigned'),
        ('subject_id', 'INT', 'FK \u2192 subjects(subject_id)', 'Subject assigned'),
        ('created_at', 'TIMESTAMP', 'DEFAULT NOW()', 'Assignment timestamp'),
    ]
)

# ===================== CHAPTER 8: IMPLEMENTATION/WORKING =====================
add_page_break()
add_para('Chapter 8', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
add_para('IMPLEMENTATION / WORKING', bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('25', bold=True, size=12, align=WD_ALIGN_PARAGRAPH.RIGHT)

add_page_break()
add_body('This chapter explains the step-by-step working of the system as it operates in practice. The system is divided into a Student Portal and an Admin Portal, each with distinct functionalities.')

add_heading_numbered('8.1 Login Page (index.php)', level=2)
add_body('The login page serves as the entry point for both students and administrators. Students log in using their roll number and date of birth. The system uses a prepared statement to retrieve the student record by roll_number, then verifies the submitted DOB against the stored value. On success, a PHP session is created with student details, and the user is redirected to the Student Dashboard.')

add_heading_numbered('8.2 Student Dashboard (student/dashboard.php)', level=2)
add_body('The student dashboard is the central hub for the student portal. It displays attendance statistics with visual progress bars showing total classes held, classes attended, attendance percentage, classes that can be missed, and classes needed to maintain minimum attendance. The dashboard also shows upcoming exams with countdown timers, recent announcements, and quick links to all student modules.')

add_page_break()
add_heading_numbered('8.3 Attendance Tracker (student/attendance.php)', level=2)
add_body('This page displays detailed attendance records for the logged-in student, organized by subject. Each subject shows a progress bar with the attendance percentage, the number of classes attended versus total classes, and dynamic indicators such as "Classes you can miss" or "Classes needed" to maintain the minimum attendance requirement. The data is queried from the attendance table using JOINs with the subjects table, filtered by the student\'s roll number.')

add_heading_numbered('8.4 Exam Timetable (student/exams.php)', level=2)
add_body('Students can view their exam schedules on this page. The timetable displays Sessional and Final examinations with subject names, exam dates, and start/end times. Each exam entry includes a countdown timer showing the remaining days until the exam. Data is fetched from the exams table joined with subjects and filtered by the student\'s department and semester.')

add_heading_numbered('8.5 Announcements (student/announcements.php)', level=2)
add_body('This page provides a centralized feed of college announcements, notices, and events. Announcements are displayed with their priority level (High, Medium, Low) indicated by color-coded badges. Students can view announcements targeted at their department and semester, as well as general announcements. The data is retrieved from the announcements table with optional image attachments.')

add_heading_numbered('8.6 Lost & Found (student/lost_found.php)', level=2)
add_body('Students can browse items reported as lost or found on campus. The page displays items with their title, description, category type (Lost/Found), current status, and any attached images. Students can also report new lost items by filling out a form with item details and optionally uploading an image. The data is managed through the lost_found table.')

add_heading_numbered('8.7 Academic Resources (student/resources.php)', level=2)
add_body('This page provides access to digital academic resources including class routines and exam schedules in PDF/image formats. Students can view and download class routines for their department and semester, as well as exam schedules. Files are stored in the uploads/routines/ and uploads/resources/ directories and linked through the class_routines and exam_schedules tables.')

add_page_break()
add_heading_numbered('8.8 Admin Login (admin-login.php)', level=2)
add_body('Administrators log in with a username and password. The system queries the admins table using a prepared statement and verifies the password. On success, an admin session is created with role information, and the admin is redirected to the Admin Dashboard based on their role (super-admin, staff, or faculty).')

add_heading_numbered('8.9 Admin Dashboard (admin/dashboard.php)', level=2)
add_body('The admin dashboard provides a comprehensive overview of campus operations. It displays quick statistics including total students, total subjects, and recent activities. The dashboard provides navigation cards linking to all admin modules: Student Management, Attendance Marker, Exam Controller, Announcements, Lost & Found Manager, and File Manager.')

add_heading_numbered('8.10 Student Information System (admin/students.php)', level=2)
add_body('This module provides full CRUD (Create, Read, Update, Delete) operations for student profiles. Administrators can add new students with their roll number, name, email, DOB, department, and semester. They can view a searchable list of all students, edit existing student records, and delete student accounts. All operations are performed using prepared statements for security.')

add_heading_numbered('8.11 Smart Attendance Marker (admin/attendance.php)', level=2)
add_body('The Smart Attendance Marker provides a quick, checkbox-based interface for marking daily attendance. The admin selects the department, semester, subject, and date. The system then displays a list of all enrolled students with checkboxes. The admin can mark all as Present or Absent with a single click, or mark individually. On submission, the system uses a database transaction to first delete any existing records for that date/subject combination, then insert fresh records, ensuring data consistency.')

add_heading_numbered('8.12 Exam Controller (admin/exams.php)', level=2)
add_body('Administrators can manage the academic calendar by scheduling exams across different departments and semesters. The module allows adding new exam entries with subject, exam date, exam type (Sessional/Final), start time, and end time. Existing exams can be edited or deleted. Data is stored in the exams table and displayed on the student exam timetable.')

add_page_break()
add_heading_numbered('8.13 Global Communications (admin/announcements.php)', level=2)
add_body('This module enables administrators to post, edit, and delete announcements. Announcements can be targeted at specific departments and semesters, or made visible to all students. Each announcement can have a priority level and an optional image attachment. The module uses the announcements table and supports file uploads to the uploads/announcements/ directory.')

add_heading_numbered('8.14 Lost & Found Manager (admin/lost_found.php)', level=2)
add_body('Administrators can review all reported Lost & Found items, manage listings, and mark items as "Claimed". The interface shows all items with their type, status, reporter details, and images. Items can be filtered by type (Lost/Found) or status (Pending/Claimed).')

add_heading_numbered('8.15 Dynamic File Manager (admin/routines.php)', level=2)
add_body('This module allows administrators to upload and update class routines and exam schedules. Routines and schedules are organized by department and semester, and can be uploaded as PDF or image files. Existing files can be replaced when updated. Files are stored in the uploads/routines/ directory and linked through the database.')

add_heading_numbered('8.16 Security Implementation', level=2)
add_body('Security is implemented at multiple levels across the system:')
add_bullet('Session-based authentication: PHP sessions maintain user state and protect all authenticated pages. The requireLogin() and requireAdminLogin() functions redirect unauthenticated users to the login page.')
add_bullet('SQL injection prevention: All database queries use MySQLi prepared statements with bind_param() to separate SQL logic from user data.')
add_bullet('Input sanitization: All user inputs are sanitized using trim(), stripslashes(), htmlspecialchars(), and mysqli_real_escape_string() where appropriate.')
add_bullet('Password security: Student passwords are their date of birth (stored securely). Admin passwords are hashed using PHP\'s password_hash().')
add_bullet('File upload validation: Uploaded files are validated for type and renamed using uniqid() to prevent path traversal attacks.')

# ===================== CHAPTER 9: SAMPLE SCREENSHOTS =====================
add_page_break()
add_para('Chapter 9', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
add_para('SAMPLE SCREENSHOTS', bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('30', bold=True, size=12, align=WD_ALIGN_PARAGRAPH.RIGHT)

add_page_break()
add_body('The following screenshots illustrate the key pages and functionalities of ICC Companion. Please insert the actual screenshots at the indicated positions before final submission.')

p = doc.add_paragraph()
run = p.add_run('9.1 Public Pages')
run.bold = True
run.font.size = Pt(12)
run.font.name = 'Times New Roman'

add_para('[STUDENT LOGIN PAGE]', align=WD_ALIGN_PARAGRAPH.CENTER)
add_para('[Insert screenshot of student login page here]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)

add_page_break()
p = doc.add_paragraph()
run = p.add_run('9.2 Student Portal')
run.bold = True
run.font.size = Pt(12)
run.font.name = 'Times New Roman'

add_para('[STUDENT DASHBOARD]', align=WD_ALIGN_PARAGRAPH.CENTER)
add_para('[Insert screenshot of student dashboard with attendance stats here]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)

add_page_break()
add_para('[ATTENDANCE TRACKER]', align=WD_ALIGN_PARAGRAPH.CENTER)
add_para('[Insert screenshot of attendance tracker with progress bars here]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)

add_page_break()
add_para('[EXAM TIMETABLE]', align=WD_ALIGN_PARAGRAPH.CENTER)
add_para('[Insert screenshot of exam timetable with countdown timers here]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)

add_page_break()
add_para('[ANNOUNCEMENTS PAGE]', align=WD_ALIGN_PARAGRAPH.CENTER)
add_para('[Insert screenshot of announcements feed here]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)

add_page_break()
add_para('[LOST & FOUND PAGE]', align=WD_ALIGN_PARAGRAPH.CENTER)
add_para('[Insert screenshot of Lost & Found listing here]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)

add_page_break()
p = doc.add_paragraph()
run = p.add_run('9.3 Admin Portal')
run.bold = True
run.font.size = Pt(12)
run.font.name = 'Times New Roman'

add_para('[ADMIN LOGIN PAGE]', align=WD_ALIGN_PARAGRAPH.CENTER)
add_para('[Insert screenshot of admin login page here]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)

add_page_break()
add_para('[ADMIN DASHBOARD]', align=WD_ALIGN_PARAGRAPH.CENTER)
add_para('[Insert screenshot of admin dashboard here]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)

add_page_break()
add_para('[STUDENT MANAGEMENT PAGE]', align=WD_ALIGN_PARAGRAPH.CENTER)
add_para('[Insert screenshot of student list management here]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)

add_page_break()
add_para('[ATTENDANCE MARKER PAGE]', align=WD_ALIGN_PARAGRAPH.CENTER)
add_para('[Insert screenshot of attendance marking interface here]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)

add_page_break()
add_para('[EXAM CONTROLLER PAGE]', align=WD_ALIGN_PARAGRAPH.CENTER)
add_para('[Insert screenshot of exam scheduling here]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)

add_page_break()
add_para('[ANNOUNCEMENT MANAGEMENT PAGE]', align=WD_ALIGN_PARAGRAPH.CENTER)
add_para('[Insert screenshot of announcement posting here]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)

# ===================== CHAPTER 10: ADVANTAGES & LIMITATIONS =====================
add_page_break()
add_para('Chapter 10', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
add_para('ADVANTAGES AND LIMITATIONS', bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('39', bold=True, size=12, align=WD_ALIGN_PARAGRAPH.RIGHT)

add_page_break()
add_heading_numbered('10.1 Advantages', level=2)

advantages = [
    ('Centralized Platform', 'All campus services \u2014 attendance, exams, announcements, Lost & Found, and resources \u2014 are available from a single portal, eliminating the need for multiple disconnected systems.'),
    ('Real-Time Attendance Tracking', 'Students can view their attendance with visual progress bars and automatic calculations of eligibility, enabling them to take proactive steps to maintain required attendance.'),
    ('Transparency', 'Students have 24/7 access to exam timetables, announcements, and academic resources, eliminating reliance on physical notice boards.'),
    ('Priority-Based Announcements', 'The three-level priority system (High, Medium, Low) ensures that critical notices are prominently visible to students.'),
    ('Efficient Attendance Marking', 'Administrators can mark attendance for an entire class with a single click, significantly reducing the time spent on daily attendance recording.'),
    ('Comprehensive Student Management', 'Full CRUD operations on student profiles give administrators complete control over the student database.'),
    ('File Attachment Support', 'Announcements and Lost & Found items can include images, making communications more informative and verifiable.'),
    ('Role-Based Access Control', 'Three admin roles (super-admin, staff, faculty) provide appropriate access levels for different administrative needs.'),
    ('Secure System', 'Prepared statements, input sanitization, and session-based authentication make the system resistant to common web vulnerabilities.'),
    ('Responsive Design', 'The mobile-first responsive interface ensures accessibility on smartphones, tablets, and desktop computers.'),
    ('Centralized File Management', 'Class routines, exam schedules, and academic resources are stored and organized in a single, easily accessible repository.'),
]

for title, desc in advantages:
    p = doc.add_paragraph()
    run = p.add_run(title + ': ')
    run.bold = True
    run.font.size = Pt(12)
    run.font.name = 'Times New Roman'
    run2 = p.add_run(desc)
    run2.font.size = Pt(12)
    run2.font.name = 'Times New Roman'
    p.paragraph_format.space_after = Pt(4)

add_page_break()
add_heading_numbered('10.2 Limitations', level=2)

limitations = [
    'No Automated Notifications: The system does not send email or SMS notifications to students when attendance is marked, exams are scheduled, or announcements are posted.',
    'Browser-Based Only: The system has no companion mobile application. Students and admins must use a web browser to access the portal, though it is mobile-responsive.',
    'No Real-Time Updates: Attendance and exam data updates require a page refresh. There is no real-time push mechanism using WebSockets or similar technology.',
    'Single Institution: The system is designed for a single college and does not support multi-campus or multi-branch configurations out of the box.',
    'No Fee Management: The system does not include any fee management, payment processing, or financial reporting functionality.',
    'No Online Examinations: The system only schedules and displays exam timetables but does not conduct online exams or quizzes.',
    'Limited Reporting: While the system provides attendance statistics, it does not include a comprehensive reporting module with graphical charts and exportable analytics.',
]

for lim in limitations:
    add_bullet(lim)

# ===================== CHAPTER 11: FUTURE ENHANCEMENTS =====================
add_page_break()
add_para('Chapter 11', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
add_para('FUTURE ENHANCEMENTS', bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('42', bold=True, size=12, align=WD_ALIGN_PARAGRAPH.RIGHT)

add_page_break()
add_body('The following enhancements are realistic and directly tied to the current state of the project:')

enhancements = [
    'Email and SMS Notifications: Integrate PHPMailer or an SMTP service to send automated email notifications to students when attendance is marked, exams are scheduled, or announcements are posted. SMS integration via Twilio or Fast2SMS can also be added using the phone numbers already stored in the student records.',
    'Mobile Application: Develop a companion Android or iOS application using React Native or Flutter, allowing students to access attendance, timetables, and announcements from their smartphones with push notification support.',
    'Real-Time Updates: Implement AJAX-based polling or WebSocket communication so that dashboard statistics and notifications update without requiring a full page refresh.',
    'Graphical Analytics Dashboard: Add visual statistics using Chart.js or similar libraries to display bar charts and pie charts of attendance trends, exam performance, and announcement engagement.',
    'Online Examination Module: Develop an integrated online examination system allowing faculty to conduct quizzes and tests with automatic grading and result compilation.',
    'Fee Management Module: Add a comprehensive fee management system with payment gateway integration, fee receipt generation, and due date tracking.',
    'Department-Wise Admin Routing: Enhance the role system to automatically route attendance and exam management to department-specific administrators.',
    'Multi-Campus Support: Extend the architecture to support multiple college campuses or branches with centralized or distributed administration.',
    'Parent/Guardian Portal: Create a separate portal for parents or guardians to monitor their ward\'s attendance, exam performance, and college communications.',
    'Library Management: Integrate a library management module with book catalog, issue/return tracking, and fine calculation functionality.',
    'Comprehensive Report Export: Add PDF export functionality for all reports and data tables using a library like FPDF or TCPDF.',
    'Two-Factor Authentication: Implement two-factor authentication for admin accounts to enhance security for sensitive operations.',
]

for i, enh in enumerate(enhancements, 1):
    p = doc.add_paragraph()
    run = p.add_run(f'{i}. ')
    run.bold = True
    run.font.size = Pt(12)
    run.font.name = 'Times New Roman'
    run2 = p.add_run(enh)
    run2.font.size = Pt(12)
    run2.font.name = 'Times New Roman'
    p.paragraph_format.space_after = Pt(6)

# ===================== CHAPTER 12: CONCLUSION =====================
add_page_break()
add_para('Chapter 12', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
add_para('CONCLUSION', bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('45', bold=True, size=12, align=WD_ALIGN_PARAGRAPH.RIGHT)

add_page_break()
add_body('ICC Companion was developed to address a real and common challenge faced by educational institutions \u2014 the lack of an integrated, transparent, and efficient platform for managing campus-wide academic and administrative processes. The system successfully replaces fragmented manual processes with a unified, fully functional web-based campus portal.')

add_body('The project has been implemented using PHP, MySQL, HTML5, CSS3, and JavaScript \u2014 all freely available and widely supported technologies. The dual-portal architecture (separate portals for students and administrators), comprehensive 12-table relational database design, visual attendance tracking with eligibility calculations, exam timetable with countdown timers, centralized announcement system, Lost & Found portal, academic resource management, and role-based admin access collectively make this a complete and practical solution for college campus management.')

add_body('From a security perspective, the system implements session-based authentication, SQL injection prevention through prepared statements, input sanitization, and role-based access control \u2014 ensuring that the application is secure for production use.')

add_body('From a user experience standpoint, the mobile-first responsive design ensures that students can access the system from any device, while the intuitive interface requires minimal training for both students and administrators.')

add_body('The project fulfils all stated objectives and provides a solid foundation that can be extended with future enhancements such as mobile applications, real-time notifications, online examinations, and fee management. It demonstrates the practical application of web development concepts learned during the BCA programme and represents a meaningful contribution to improving academic administration at Icon Commerce College.')

# ===================== REFERENCES =====================
add_page_break()
add_para('REFERENCES', bold=True, size=18, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24)
add_body('The following resources were referenced during the development and documentation of this project:')

references = [
    'PHP Manual \u2014 Official PHP Documentation. Available at: https://www.php.net/manual/en/',
    'MySQL Reference Manual \u2014 MySQL 5.7 Documentation. Available at: https://dev.mysql.com/doc/refman/5.7/en/',
    'W3Schools \u2014 HTML, CSS, JavaScript Reference and Tutorials. Available at: https://www.w3schools.com/',
    'MDN Web Docs \u2014 JavaScript Reference. Mozilla Developer Network. Available at: https://developer.mozilla.org/en-US/docs/Web/JavaScript',
    'Font Awesome \u2014 Icon Library Documentation. Available at: https://fontawesome.com/docs',
    'OWASP Foundation \u2014 Web Application Security Guide. Available at: https://owasp.org/',
    'PHP: The Right Way \u2014 Best Practices for PHP Development. Available at: https://phptherightway.com/',
    'Silberschatz, A., Korth, H. F., & Sudarshan, S. \u2014 Database System Concepts, 7th Edition. McGraw-Hill Education.',
    'Bootstrap \u2014 Responsive Web Development Framework. Available at: https://getbootstrap.com/',
]

for i, ref in enumerate(references, 1):
    p = doc.add_paragraph()
    run = p.add_run(f'{i}. {ref}')
    run.font.size = Pt(12)
    run.font.name = 'Times New Roman'
    p.paragraph_format.space_after = Pt(6)

# Save
output_path = r'C:\xampp\htdocs\ICC_Companion\temp\ppt_and_report\my_report\PROJECT_REPORT.docx'
doc.save(output_path)
print(f'Report saved to: {output_path}')