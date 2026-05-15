"""Edit sajeeb.docx reference file to become ICC Companion report."""
from docx import Document
from docx.shared import Pt
import os

src = r'C:\xampp\htdocs\ICC_Companion\temp\ppt_and_report\report_reference\sajeeb.docx'
out = r'C:\xampp\htdocs\ICC_Companion\temp\ppt_and_report\my_report\PROJECT_REPORT.docx'

doc = Document(src)

def set_text(para, text, size=12):
    """Clear paragraph and set new text while preserving style."""
    for run in para.runs:
        run.text = ''
    if para.runs:
        para.runs[0].text = text
        para.runs[0].font.name = 'Times New Roman'
        para.runs[0].font.size = Pt(size)
    else:
        run = para.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(size)

def prepend_text(para, new_text, size=12):
    """Prepend text to existing paragraph content."""
    if para.runs:
        para.runs[0].text = new_text + para.runs[0].text
        para.runs[0].font.name = 'Times New Roman'
        para.runs[0].font.size = Pt(size)

def clear_para(para):
    """Clear all text from paragraph."""
    for run in para.runs:
        run.text = ''

def table_cell(table_idx, row_idx, col_idx):
    doc.tables[table_idx].rows[row_idx].cells[col_idx]

# ===== COVER PAGE =====
# P2: Project title - clear ALL runs including any leftover quotes
para = doc.paragraphs[2]
for r in para.runs:
    r.text = ''
for r in para.runs:
    if r.text == '':
        r.text = '\u201cICC COMPANION\u201d'
        r.font.name = 'Times New Roman'
        r.font.size = Pt(22)
        break
# Also fix P0 subtitle
set_text(doc.paragraphs[0], 'A PROJECT REPORT ON', size=18)

# Fix P4 text
set_text(doc.paragraphs[4], 
    'A Project Report submitted in partial fulfilment of the requirements for the degree of Bachelor of Computer Application')

# Cover table - Table 0 - CLEAR ALL and rebuild
t0 = doc.tables[0]

# Row 0 Col 0: Name of Guide - clear all paragraphs
cell0 = t0.rows[0].cells[0]
for p in cell0.paragraphs:
    for r in p.runs:
        r.text = ''
cell0.paragraphs[0].clear()
r0 = cell0.paragraphs[0].add_run('Name of the Guide:')
r0.bold = True
r0.font.name = 'Times New Roman'
r0.font.size = Pt(12)
r1 = cell0.add_paragraph('Urbimala Hazarika, Asst. Prof')
for r in r1.runs: r.font.name = 'Times New Roman'; r.font.size = Pt(12)
r2 = cell0.add_paragraph('')
r2b = r2.add_run('Department:')
r2b.bold = True
r2b.font.name = 'Times New Roman'
r2b.font.size = Pt(12)
r3 = cell0.add_paragraph('Bachelor of Computer Application')
for r in r3.runs: r.font.name = 'Times New Roman'; r.font.size = Pt(12)
r4 = cell0.add_paragraph('ICON Commerce College')
for r in r4.runs: r.font.name = 'Times New Roman'; r.font.size = Pt(12)
r5 = cell0.add_paragraph('Guwahati \u2013 781003')
for r in r5.runs: r.font.name = 'Times New Roman'; r.font.size = Pt(12)

# Row 0 Col 1: Submitted By - clear all paragraphs
cell1 = t0.rows[0].cells[1]
for p in cell1.paragraphs:
    for r in p.runs:
        r.text = ''
cell1.paragraphs[0].clear()
s0 = cell1.paragraphs[0].add_run('Submitted By:')
s0.bold = True
s0.font.name = 'Times New Roman'
s0.font.size = Pt(12)
s1 = cell1.add_paragraph('Ankita Chetri')
for r in s1.runs: r.font.name = 'Times New Roman'; r.font.size = Pt(12)
s2 = cell1.add_paragraph('Roll No: UT-231-049-0012')
for r in s2.runs: r.font.name = 'Times New Roman'; r.font.size = Pt(12)
s3 = cell1.add_paragraph('Registration No: 23084898')
for r in s3.runs: r.font.name = 'Times New Roman'; r.font.size = Pt(12)
s4 = cell1.add_paragraph('BCA 6th Semester (FYUGP)')
s4b = s4.add_run('')
s4b.font.name = 'Times New Roman'
s4b.font.size = Pt(12)
s5 = cell1.add_paragraph('ICON Commerce College')
for r in s5.runs: r.font.name = 'Times New Roman'; r.font.size = Pt(12)

# ===== CERTIFICATE =====
# P19: Certificate text
set_text(doc.paragraphs[19],
    'This is to certify that the project entitled "ICC COMPANION" has been submitted by Ankita Chetri '
    '(Roll No: UT-231-049-0012, Registration No: 23084898) in partial fulfilment of the requirements '
    'for the degree of Bachelor of Computer Applications (BCA), 6th Semester, at Icon Commerce College, '
    'Gauhati University, during the Academic Session 2025\u201326.')

set_text(doc.paragraphs[21],
    'This is an authentic work carried out by her under my supervision and guidance. The project has '
    'not been submitted to any other university or institution for the award of any degree or diploma.')

set_text(doc.paragraphs[40],
    'Name of the Guide: Urbimala Hazarika, Asst. Prof\nDepartment: Bachelor of Computer Application\nInstitution: Icon Commerce College')

set_text(doc.paragraphs[41],
    'Guwahati \u2013 781021')

set_text(doc.paragraphs[42],
    'Signature of the Guide: ____________________')

# ===== DECLARATION =====
set_text(doc.paragraphs[49],
    'I hereby declare that the project report \u201cICC Companion\u201d, submitted in partial fulfilment '
    'of the requirement for the degree of Bachelor of Computer Application (BCA) in Icon Commerce College, '
    'under Gauhati University, is my original work and has not been submitted for the award of any other '
    'degree, diploma, fellowship or any other similar titles.')

set_text(doc.paragraphs[54],
    'Place: Guwahati\t\tNAME: ANKITA CHETRI\nROLL NO: UT-231-049-0012')

set_text(doc.paragraphs[55],
    'REGISTRATION NO: 23084898\nDEPARTMENT: BCA 6TH SEMESTER\nICON COMMERCE COLLEGE')

# ===== ACKNOWLEDGEMENT =====
set_text(doc.paragraphs[59],
    'I would like to express my sincere gratitude to my project guide and mentor Urbimala Hazarika '
    'for her invaluable guidance, encouragement, and constructive feedback throughout the development '
    'of this project. Her insights and timely advice have been instrumental in shaping this work.')

set_text(doc.paragraphs[61],
    'I am grateful to Dr. Mandira Saha, Principal of Icon Commerce College, and Tridib Kr. Handique, '
    'Co-Ordinator of the BCA Department, for providing the necessary resources and permission to '
    'undertake this project. I also extend my thanks to the entire BCA faculty for their continuous support.')

clear_para(doc.paragraphs[63])
clear_para(doc.paragraphs[65])
doc.paragraphs[63].add_run('I would like to thank my family and friends for their unwavering encouragement and understanding during the course of this project.').font.name = 'Times New Roman'

set_text(doc.paragraphs[67],
    'Place: Guwahati\t\tName: Ankita Chetri')

set_text(doc.paragraphs[68],
    'Date: ____________________\t\tRoll No: UT-231-049-0012')

set_text(doc.paragraphs[69],
    'Registration No: 23084898')

set_text(doc.paragraphs[70],
    'BCA 6th Semester, Icon Commerce College')

# ===== ABSTRACT =====
set_text(doc.paragraphs[74],
    'ICC Companion is a web-based campus portal developed for ICON Commerce College using PHP, MySQL, '
    'HTML5, CSS3, and JavaScript. The system provides a unified digital platform where students can '
    'access attendance records, exam timetables, class routines, academic resources, college announcements, '
    'and a Lost & Found portal. Administrators can manage student records, mark attendance, schedule '
    'examinations, post announcements, manage Lost & Found items, upload class routines, and publish '
    'academic resources through a role-based admin panel.')

set_text(doc.paragraphs[76],
    'The system employs a MySQL database with twelve interconnected tables and uses PHP server-side '
    'logic with prepared statements for database security. The frontend uses vanilla JavaScript with '
    'the Fetch API for asynchronous JSON data exchange. The system supports three admin roles \u2014 '
    'Principal (super-admin), HOD (dept-admin), and Faculty \u2014 each with appropriate access restrictions.')

clear_para(doc.paragraphs[77])
clear_para(doc.paragraphs[78])
clear_para(doc.paragraphs[80])

doc.paragraphs[77].add_run(
    'Students log in using their roll number and date of birth to view attendance with visual progress '
    'bars, exam timetables with countdown indicators, class routines, announcements, and academic resources.'
).font.name = 'Times New Roman'

doc.paragraphs[78].add_run(
    'The admin panel provides tools for student record management, attendance marking via checkboxes, '
    'exam scheduling, announcement posting, Lost & Found management, class routine uploads, and '
    'academic resource publishing.'
).font.name = 'Times New Roman'

set_text(doc.paragraphs[80],
    'The project was developed using the XAMPP server environment and follows a mobile-first responsive '
    'design approach for accessibility across devices.')

# ===== FIX CHAPTER 2 HEADING: REQUIREMENT SPECIFICATION -> OBJECTIVES =====
set_text(doc.paragraphs[150], 'OBJECTIVES OF THE PROJECT')

# ===== FIX CONTENTS TABLE =====
t1 = doc.tables[1]
contents_data = [
    ('SECTION', 'PAGE NO.'),
    ('Chapter 1: Introduction', '1-2'),
    ('    1.1 Background', '1'),
    ('    1.2 Problem Statement', '1-2'),
    ('    1.3 Proposed Solution', '2'),
    ('Chapter 2: Objectives of the Project', '3-4'),
    ('Chapter 3: Scope of the Project', '5-6'),
    ('    3.1 In Scope', '5'),
    ('    3.2 Out of Scope', '6'),
    ('Chapter 4: System Analysis', '7-8'),
    ('    4.1 Existing System', '7'),
    ('    4.2 Proposed System', '7'),
    ('    4.3 Feasibility Study', '8'),
    ('Chapter 5: System Design', '9-10'),
    ('    5.1 System Architecture', '9'),
    ('    5.2 Data Flow Diagram', '9'),
    ('    5.3 ER Diagram', '10'),
    ('Chapter 6: Database Design', '11-14'),
    ('Chapter 7: Technology Used', '15-16'),
    ('Chapter 8: Implementation / Working', '17-21'),
    ('Chapter 9: Screenshots', '22-24'),
    ('Chapter 10: Advantages & Limitations', '25-26'),
    ('    10.1 Advantages', '25'),
    ('    10.2 Limitations', '26'),
    ('Chapter 11: Future Enhancements', '27-28'),
    ('Chapter 12: Conclusion', '29-30'),
    ('Bibliography', '31'),
]
for ri, (sec, pg) in enumerate(contents_data):
    if ri < len(t1.rows):
        t1.rows[ri].cells[0].paragraphs[0].clear()
        t1.rows[ri].cells[0].paragraphs[0].add_run(sec).font.name = 'Times New Roman'
        t1.rows[ri].cells[1].paragraphs[0].clear()
        t1.rows[ri].cells[1].paragraphs[0].add_run(pg).font.name = 'Times New Roman'

# ===== ADD SEPARATE TECHNOLOGY USED CHAPTER (Ch7) =====
# The reference's Ch2 has tech content at P157-P173
# We need to mark these as part of Tech chapter
# We'll keep the tech content where it is, but also add a heading reference

# P157: Change "Technologies Used" heading
set_text(doc.paragraphs[157], 'Technologies Used')

# ===== CHAPTER 1: INTRODUCTION =====
set_text(doc.paragraphs[100],
    'ICC Companion was developed to address the need for an integrated digital campus platform at '
    'ICON Commerce College. The system provides a single portal where students can access academic '
    'data, view attendance records, check exam schedules, read class routines, browse announcements, '
    'use the Lost & Found portal, and download academic resources.')

set_text(doc.paragraphs[102],
    'With the increasing adoption of web technologies in education, a centralized campus portal can '
    'streamline these processes by providing a single platform for students and administrators. '
    'ICON Commerce College, affiliated with Gauhati University, offers BCA, BBA, BA, and B.COM '
    'programmes across six semesters.')

# Problem statement
set_text(doc.paragraphs[106],
    'The absence of a centralized digital platform in the college leads to specific challenges:')

bullets_1_2 = [
    'Attendance records are maintained manually, giving students no real-time visibility into their attendance status.',
    'Exam schedules and class routines are shared through printed notices or verbal announcements that can be missed.',
    'College announcements and important notices lack a permanent, searchable archive.',
    'The Lost & Found process relies on physical notice boards with no centralized tracking.',
    'Administrators lack a consolidated view of student data, attendance patterns, and academic schedules.',
    'Academic resources such as syllabi and study materials are distributed through email or printed copies without a central repository.',
]
for i, bidx in enumerate(range(108, 114)):
    set_text(doc.paragraphs[bidx], bullets_1_2[i])

# Proposed solution
set_text(doc.paragraphs[116],
    'ICC Companion is a web-based campus portal developed using PHP and MySQL. Students log in using '
    'their roll number and date of birth to access attendance records with visual progress bars, '
    'view exam timetables with countdown timers, browse class routines, read college announcements, '
    'use the Lost & Found portal, and download academic resources. Administrators access a separate '
    'management panel where they can perform CRUD operations on student records, mark attendance '
    'through a checkbox interface, schedule examinations, post targeted announcements, manage '
    'Lost & Found items, upload class routines, and publish academic resources.')

# ===== CHAPTER 2: REQUIREMENT SPECIFICATION =====
t2 = doc.tables[2]
# Hardware requirements table
hw_data = [
    ('Component', 'Minimum Specification'),
    ('Processor', 'Intel Core i3 or equivalent'),
    ('RAM', '4 GB or higher'),
    ('Storage', '20 GB available disk space'),
    ('Network', 'Internet connection / local network for XAMPP'),
]
for ri, (c0, c1) in enumerate(hw_data):
    t2.rows[ri].cells[0].paragraphs[0].clear()
    t2.rows[ri].cells[0].paragraphs[0].add_run(c0).font.name = 'Times New Roman'
    t2.rows[ri].cells[1].paragraphs[0].clear()
    t2.rows[ri].cells[1].paragraphs[0].add_run(c1).font.name = 'Times New Roman'

# Technologies table - Table 3
tech_data = [
    ('Technology', 'Version / Detail', 'Role in Project'),
    ('PHP', '7.4+', 'Server-side scripting \u2014 form processing, session management, database interaction, file uploads, and authentication.'),
    ('MySQL', '5.7+', 'Relational database \u2014 stores all data across 12 tables including students, attendance, exams, announcements, and resources.'),
    ('mysqli (PHP Extension)', '\u2014', 'Database connectivity with prepared statements for SQL injection prevention.'),
    ('HTML5', '\u2014', 'Semantic structure for all web pages \u2014 login, dashboards, forms, tables, and portals.'),
    ('CSS3', '\u2014', 'Responsive styling, layout grid, sidebar navigation, cards, badges, and mobile-first design.'),
    ('JavaScript (Vanilla)', '\u2014', 'Client-side logic: form validation, Fetch API calls, DOM manipulation, search/filter, dynamic content rendering.'),
    ('Font Awesome 6.4.0', 'CDN', 'Icon library for navigation icons, stat cards, and action buttons throughout the interface.'),
    ('Apache Web Server', 'XAMPP', 'Local server environment for running PHP and serving the web application.'),
    ('Session Management', 'PHP Sessions', 'Maintaining authenticated state for both students and administrators across pages.'),
]
t3 = doc.tables[3]
t3.rows[0].cells[0].paragraphs[0].clear()
t3.rows[0].cells[0].paragraphs[0].add_run(tech_data[0][0])
t3.rows[0].cells[1].paragraphs[0].clear()
t3.rows[0].cells[1].paragraphs[0].add_run(tech_data[0][1])
t3.rows[0].cells[2].paragraphs[0].clear()
t3.rows[0].cells[2].paragraphs[0].add_run(tech_data[0][2])
for ri in range(1, len(tech_data)):
    for ci in range(3):
        cell = t3.rows[ri].cells[ci]
        cell.paragraphs[0].clear()
        cell.paragraphs[0].add_run(tech_data[ri][ci]).font.name = 'Times New Roman'

# Tech list items (P161-P173)
tech_items = [
    'PHP \u2014 Server-side scripting for form processing, session management, and database operations.',
    'MySQL \u2014 Relational database management system for storing students, attendance, exams, announcements, and resources.',
    'mysqli extension \u2014 PHP extension used for database connectivity with prepared statements.',
    'HTML5 / CSS3 \u2014 Structure and responsive styling of the web interface.',
    'JavaScript (Vanilla) \u2014 Client-side validation, Fetch API, dynamic UI interactions, and DOM manipulation.',
    'Font Awesome 6.4.0 \u2014 Icon library loaded via CDN for UI icons throughout the application.',
    'Session Management \u2014 PHP sessions used to authenticate and maintain logged-in state for both students and admins.',
]
for i, bidx in enumerate(range(161, 168, 2)):
    set_text(doc.paragraphs[bidx], tech_items[i])
# Clear remaining tech items that don't apply
for bidx in range(169, 174, 2):
    clear_para(doc.paragraphs[bidx])

# ===== CHAPTER 3: OBJECTIVES =====
set_text(doc.paragraphs[204],
    'The primary objectives of the ICC Companion project are:')

objectives = [
    'To provide students with a secure login portal using roll number and date of birth.',
    'To display attendance records with subject-wise progress bars and dynamic eligibility indicators.',
    'To present exam timetables with Sessional and Final sections, countdown indicators, and inline schedule files.',
    'To allow students to view class routines as embedded PDFs or images for their department and semester.',
    'To provide a centralized announcements feed with priority badges and target audience filtering.',
    'To implement a Lost & Found portal for browsing items with type and category filters.',
    'To provide access to academic resources including syllabi, books, study materials, links, and text content.',
    'To enable CRUD operations on student records with search and filter capabilities.',
    'To provide a smart attendance marking interface with checkbox selection and database transactions.',
    'To allow administrators to schedule examinations with subject, date, time, room, and exam type.',
    'To provide tools for posting, editing, and deleting announcements with priority and targeting.',
    'To implement role-based access control with three admin levels: Principal, HOD, and Faculty.',
]
for i, bidx in enumerate(range(206, 218)):
    set_text(doc.paragraphs[bidx], objectives[i])

# ===== CHAPTER 4: SCOPE =====
set_text(doc.paragraphs[243],
    'ICC Companion is designed to serve the campus management needs of ICON Commerce College. '
    'The system supports two categories of users \u2014 students and administrators \u2014 through '
    'separate, secure portals with role-based access control.')

# In Scope items (P248-P259)
in_scope = [
    'Student login using roll number and date of birth with session-based authentication.',
    'Student dashboard displaying overall attendance percentage, upcoming exams count, and announcements count.',
    'Subject-wise attendance tracking with progress bars, percentages, and status indicators (Safe/Warning/Shortage).',
    'Exam timetable viewing with subject names, dates, times, rooms, and countdown indicators.',
    'Class routine viewing with inline PDF and image file display for the student\u2019s department and semester.',
    'Centralized announcements feed with priority badges (High/Medium/Low) and target audience display.',
    'Lost & Found browsing with filters for item type and category.',
    'Academic resources browsing with search input and resource type filter.',
    'Admin login with role-based tabs (Faculty, HOD, Principal) and session authentication.',
    'Admin CRUD operations for student records with department, semester filters, and search.',
    'Attendance marking through a checkbox-based interface with select-all/deselect-all and transaction-based saving.',
    'Exam scheduling with subject, date, time, room, and exam type; schedule file upload for Sessional and Final.',
]
for i, bidx in enumerate(range(248, 260)):
    set_text(doc.paragraphs[bidx], in_scope[i])

# Out of Scope items (P263-P267)
out_scope = [
    'The system does not send automated email or SMS notifications.',
    'The system is designed for a single college and does not support multi-campus configurations.',
    'No companion mobile application exists \u2014 the system is browser-based only (mobile-responsive).',
    'No real-time chat or messaging feature is implemented.',
    'No fee management or payment gateway integration exists.',
]
for i, bidx in enumerate(range(263, 268)):
    set_text(doc.paragraphs[bidx], out_scope[i])

# ===== CHAPTER 5: SYSTEM ANALYSIS =====
# Existing system
set_text(doc.paragraphs[295],
    'Currently, campus information at ICON Commerce College is managed through traditional methods:')

existing_items = [
    'Attendance is recorded in registers or spreadsheets not accessible to students in real time.',
    'Exam schedules and class routines are posted on physical notice boards that can be missed.',
    'Announcements are made verbally or through printed circulars with no permanent archive.',
    'Lost & Found items are managed informally through word-of-mouth or physical boards.',
    'Academic resources are distributed through email or as printed handouts without a central repository.',
]
for i, bidx in enumerate(range(297, 302)):
    set_text(doc.paragraphs[bidx], existing_items[i])

# Proposed system
set_text(doc.paragraphs[303],
    'ICC Companion replaces these fragmented methods with a unified web-based platform:')

proposed_items = [
    'All data is stored digitally in a MySQL database with permanent records and audit trails.',
    'Students can access attendance, timetables, routines, announcements, and resources 24/7 from any device.',
    'Attendance is calculated automatically with visual progress bars and eligibility indicators.',
    'Admins have a centralized dashboard for managing students, attendance, exams, and announcements.',
    'Lost & Found items are tracked digitally with categories, images, and claim status.',
    'Academic resources are organized by department and semester in a central repository.',
]
for i, bidx in enumerate(range(304, 310)):
    set_text(doc.paragraphs[bidx], proposed_items[i])

# Feasibility
set_text(doc.paragraphs[312],
    'The system uses PHP, MySQL, HTML5, CSS3, and JavaScript \u2014 all freely available technologies '
    'that can be hosted on any standard Apache server. No proprietary software is required.')

set_text(doc.paragraphs[316],
    'All technologies used are open-source and free of cost. The system can be deployed on a standard '
    'XAMPP setup with minimal operational cost.')

set_text(doc.paragraphs[319],
    'The system has an intuitive interface. Students can log in and navigate easily without training. '
    'Administrators can manage all operations through the dashboard without specialized technical knowledge.')

# ===== CHAPTER 6: SYSTEM DESIGN =====
set_text(doc.paragraphs[347],
    'The system follows a three-tier architecture. The Presentation Layer consists of HTML, CSS, and '
    'JavaScript running in the browser. The Application Layer comprises PHP scripts on the Apache server '
    'handling business logic, authentication, and database interaction. The Data Layer is the MySQL '
    'database storing all application data. Communication occurs through JSON-based API calls using the Fetch API.')

set_text(doc.paragraphs[351], 'Figure 6.1 \u2014 System Architecture Diagram')

set_text(doc.paragraphs[354],
    'The Level 0 DFD shows the system as a single process with two external entities \u2014 Student '
    'and Administrator \u2014 illustrating the high-level data flow.')

set_text(doc.paragraphs[357], 'Figure 6.2 \u2014 DFD Level 0: Context Diagram')

set_text(doc.paragraphs[360],
    'The Level 1 DFD breaks the system into major processes: Student Authentication, Attendance Viewing, '
    'Exam Timetable Viewing, Announcement Browsing, Lost & Found Management, Resource Management, '
    'Admin Authentication, Student Management, Attendance Marking, Exam Scheduling, and Announcement Management.')

set_text(doc.paragraphs[363], 'Figure 6.3 \u2014 DFD Level 1: Detailed Process Flow')

set_text(doc.paragraphs[368],
    'The Use Case Diagram shows all actions available to each actor (Student and Administrator) and the '
    'system boundary.')

set_text(doc.paragraphs[372], 'Figure 6.4 \u2014 Use Case Diagram')

set_text(doc.paragraphs[375],
    'The ER Diagram shows the database entities and their relationships. The central entities include '
    'students, departments, subjects, attendance, exams, lost_found, announcements, class_routines, '
    'resources, and admins. Students are linked to departments and attendance records. Subjects belong '
    'to departments. Attendance connects students to subjects with date and status.')

set_text(doc.paragraphs[377], 'Figure 6.5 \u2014 Entity-Relationship (ER) Diagram')

# ===== CHAPTER 7: DATABASE DESIGN =====
set_text(doc.paragraphs[403],
    'The database is named campus_portal and consists of twelve tables. All tables use MySQL with '
    'proper data types, primary keys, foreign keys, and unique constraints.')

# Database tables - Tables 4,5,6,7,8 need to be replaced
# These are: users->students, admins->admins, categories->departments, complaints->subjects, complaint_responses->attendance
# etc. But since the number of tables is different (5 vs 12), we can't just edit cell text.
# Let me replace the content of these tables with ICC Companion tables.

# Table 4: Replace users table with departments table
t4 = doc.tables[4]
dept_header = ['Field Name', 'Data Type', 'Constraint', 'Description']
dept_data = [
    ('dept_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique department ID'),
    ('dept_code', 'VARCHAR(10)', 'UNIQUE, NOT NULL', 'Department code (BCA, BBA, etc.)'),
    ('dept_name', 'VARCHAR(100)', 'NOT NULL', 'Full department name'),
    ('max_semesters', 'INT', 'DEFAULT 6', 'Number of semesters'),
    ('', '', '', ''),
    ('', '', '', ''),
    ('', '', '', ''),
    ('', '', '', ''),
    ('', '', '', ''),
]
for ri, row in enumerate(t4.rows):
    for ci in range(4):
        p = row.cells[ci].paragraphs[0]
        p.clear()
        val = (dept_header if ri == 0 else dept_data[ri-1])[ci] if ri <= len(dept_data) else ''
        p.add_run(val).font.name = 'Times New Roman'

# Update heading for table
set_text(doc.paragraphs[405], 'Table 1: departments')

# Table 5: Replace admins table
t5 = doc.tables[5]
admin_header = ['Field Name', 'Data Type', 'Constraint', 'Description']
admin_data = [
    ('admin_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique admin ID'),
    ('username', 'VARCHAR(50)', 'UNIQUE, NOT NULL', 'Admin login username'),
    ('password', 'VARCHAR(255)', 'NOT NULL', 'Login password'),
    ('name', 'VARCHAR(100)', 'NOT NULL', 'Admin full name'),
    ('role', 'VARCHAR(50)', "DEFAULT 'faculty'", 'super-admin/dept-admin/faculty'),
    ('assigned_dept', 'VARCHAR(10)', "DEFAULT 'all'", 'Department scope'),
    ('', '', '', ''),
]
for ri, row in enumerate(t5.rows):
    for ci in range(4):
        p = row.cells[ci].paragraphs[0]
        p.clear()
        val = (admin_header if ri == 0 else admin_data[ri-1])[ci] if ri <= len(admin_data) else ''
        p.add_run(val).font.name = 'Times New Roman'

set_text(doc.paragraphs[408], 'Table 2: admins')

# Table 6: Replace categories table with subjects
t6 = doc.tables[6]
subj_header = ['Field Name', 'Data Type', 'Constraint', 'Description']
subj_data = [
    ('subject_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique subject ID'),
    ('subject_code', 'VARCHAR(20)', 'NOT NULL', 'Subject code'),
    ('subject_name', 'VARCHAR(100)', 'NOT NULL', 'Subject name'),
    ('dept_code', 'VARCHAR(10)', 'FK \u2192 departments', 'Parent department'),
    ('', '', '', ''),
]
for ri, row in enumerate(t6.rows):
    for ci in range(4):
        p = row.cells[ci].paragraphs[0]
        p.clear()
        val = (subj_header if ri == 0 else subj_data[ri-1])[ci] if ri <= len(subj_data) else ''
        p.add_run(val).font.name = 'Times New Roman'

set_text(doc.paragraphs[411], 'Table 3: subjects')

# Table 7: Replace complaints table with students
t7 = doc.tables[7]
stu_header = ['Field Name', 'Data Type', 'Constraint', 'Description']
stu_data = [
    ('student_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique student ID'),
    ('roll_number', 'VARCHAR(20)', 'UNIQUE, NOT NULL', 'Roll number (login)'),
    ('name', 'VARCHAR(100)', 'NOT NULL', 'Student full name'),
    ('dob', 'DATE', 'NOT NULL', 'Date of birth (password)'),
    ('email', 'VARCHAR(100)', '', 'Email address'),
    ('phone', 'VARCHAR(15)', '', 'Contact number'),
    ('dept_code', 'VARCHAR(10)', 'FK \u2192 departments', 'Department'),
    ('semester', 'INT', 'NOT NULL', 'Current semester'),
    ('created_at', 'TIMESTAMP', 'DEFAULT NOW()', 'Registration timestamp'),
    ('', '', '', ''),
    ('', '', '', ''),
    ('', '', '', ''),
]
for ri, row in enumerate(t7.rows):
    for ci in range(4):
        p = row.cells[ci].paragraphs[0]
        p.clear()
        val = (stu_header if ri == 0 else stu_data[ri-1])[ci] if ri <= len(stu_data) else ''
        p.add_run(val).font.name = 'Times New Roman'

set_text(doc.paragraphs[414], 'Table 4: students')

# Table 8: Replace complaint_responses with attendance
t8 = doc.tables[8]
att_header = ['Field Name', 'Data Type', 'Constraint', 'Description']
att_data = [
    ('attendance_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique attendance ID'),
    ('roll_number', 'VARCHAR(20)', 'FK \u2192 students', 'Student roll number'),
    ('subject_id', 'INT', 'FK \u2192 subjects', 'Subject attended'),
    ('attendance_date', 'DATE', 'NOT NULL', 'Date of class'),
    ('status', "ENUM('present','absent')", 'NOT NULL', 'Attendance status'),
    ('UNIQUE', '(roll, subject, date)', '', 'Prevents duplicates'),
]
for ri, row in enumerate(t8.rows):
    for ci in range(4):
        p = row.cells[ci].paragraphs[0]
        p.clear()
        val = (att_header if ri == 0 else att_data[ri-1])[ci] if ri <= len(att_data) else ''
        p.add_run(val).font.name = 'Times New Roman'

set_text(doc.paragraphs[419], 'Table 5: attendance')

# Remove reference to "Default categories pre-loaded" since we now have subjects
clear_para(doc.paragraphs[414])  # This was about default categories

# ===== CHAPTER 8: IMPLEMENTATION =====
set_text(doc.paragraphs[447],
    'The system is divided into two portals \u2014 Student Portal and Admin Portal \u2014 each with '
    'distinct functionalities and separate authentication mechanisms.')

impl_sections = {
    450: '8.1 Home Page (index.html)',
    452: '8.2 Student Login (student-login.html)',
    455: '8.3 Student Dashboard (student/dashboard.html)',
    458: '8.4 My Subjects (student/subjects.html)',
    461: '8.5 Academic Resources (student/resources.html)',
    464: '8.6 My Attendance (student/attendance.html)',
    467: '8.7 Exam Timetable (student/exams.html)',
    470: '8.8 Class Routine (student/routines.html)',
    473: '8.9 Lost & Found (student/lost-found.html)',
    476: '8.10 Announcements (student/announcements.html)',
    479: '8.11 Admin Login (admin-login.html)',
    482: '8.12 Admin Dashboard (admin/dashboard.html)',
    485: '8.13 Manage Students (admin/students.html)',
    488: '8.14 Attendance Management (admin/attendance.html)',
    491: '8.15 Manage Exams (admin/exams.html)',
    494: '8.16 Security Implementation',
}

impl_content = {
    450: 'The public landing page displays college branding, a hero section, and feature cards. '
         'Two buttons direct users to Student Login or Admin Login. No authentication required.',

    452: 'Students log in with roll number and date of birth. A POST request is sent to '
         'api/student-login.php which queries the students table using a prepared statement. '
         'On success, student details are stored in sessionStorage and the user is redirected to the dashboard.',

    455: 'The dashboard displays a welcome card with student details, three stat cards showing '
         'attendance percentage, upcoming exams count, and announcements count, a quick access menu, '
         'and the latest announcements fetched from the API.',

    458: 'This page displays subjects for the student\'s department and semester. Data comes from '
         'api/get-subjects.php. Each card shows subject code, name, and semester info.',

    461: 'Resources are filtered by department and semester. Types include syllabus, book, material, '
         'link, and text. Each resource has download, view link, or read text actions. Search and type filters available.',

    464: 'Subject-wise attendance with progress bars showing percentage. Overall percentage shown at top. '
         'Each subject shows classes attended/total, colored bar (green/orange/red), and "can miss X more" message.',

    467: 'Exams split into Sessional and Final sections. Each entry shows date, subject, time, room, '
         'and countdown badge. Schedule files can be uploaded as PDF or image for inline viewing.',

    470: 'Latest class routine displayed for the student\'s dept and semester. PDFs embedded via iframe, '
         'images shown directly, other files show download link.',

    473: 'Browse Lost & Found items with filters for type (Lost/Found) and category. Each card shows icon/image, '
         'type badge, title, location, date, description, and contact info.',

    476: 'Announcements displayed in descending date order. Priority-coded left border (red=High). '
         'Each card shows title, description, target, date, and attachment/link buttons.',

    479: 'Admins login with username and password via three role tabs (Faculty, HOD, Principal). '
         'API validates role matches selected tab. Session stores role, assigned dept, and semester.',

    482: 'Welcome banner with name and role badge. Four stat cards: students, exams, lost items, announcements. '
         'Quick actions menu. Students by department section. Role-based visibility for admin modules.',

    485: 'CRUD operations for student records with department/semester filters and search. '
         'Faculty-level admins can only view. Add/edit modal with roll, name, DOB, dept, sem, phone, email fields.',

    488: 'Two tabs: Mark Attendance and View Records. Mark: select dept, sem, subject, date \u2192 checkbox list. '
         'Save uses database transaction. View: student-wise or all-students overview with percentages.',

    491: 'Two sections: Sessional and Final. Add/edit/delete exams with date, subject, time, room. '
         'Upload schedule files (PDF/image) per exam type, department, and semester.',

    494: 'Multiple security layers: PHP session authentication, prepared statements for SQL injection prevention, '
         'input sanitization, role-based access control, file upload validation, frontend role enforcement.',
}

# Update heading names
for pidx in impl_sections:
    set_text(doc.paragraphs[pidx], impl_sections[pidx])

# Update content (odd indices after headings)
for pidx, content in impl_content.items():
    content_pidx = pidx + 1
    if content_pidx < len(doc.paragraphs):
        set_text(doc.paragraphs[content_pidx], content)

# Remove remaining complaint-specific headings (My Complaints, View Complaint, etc.)
for bidx in range(496, 518):
    try:
        clear_para(doc.paragraphs[bidx])
    except:
        pass

# ===== CHAPTER 9: SCREENSHOTS =====
# Replace screenshot labels
set_text(doc.paragraphs[521],
    'The following screenshots illustrate the key pages and functionalities of ICC Companion. '
    'Actual screenshots should be inserted at the indicated positions before final submission.')

screenshot_labels = {
    525: '9.1 Public Pages',
    527: 'HOME PAGE',
    551: 'STUDENT LOGIN PAGE',
    554: '9.2 Student Portal',
    555: 'STUDENT DASHBOARD',
    559: 'MY SUBJECTS PAGE',
    562: 'MY ATTENDANCE PAGE',
    565: 'EXAM TIMETABLE PAGE',
    570: 'LOST & FOUND PAGE',
    573: '9.3 Admin Portal',
    575: 'ADMIN LOGIN PAGE',
    594: 'ADMIN DASHBOARD',
    599: 'MANAGE STUDENTS PAGE',
    604: 'ATTENDANCE MANAGEMENT PAGE',
    607: 'MANAGE EXAMS PAGE',
    610: 'MANAGE ANNOUNCEMENTS PAGE',
    613: 'MANAGE FACULTY PAGE',
}

for pidx, text in screenshot_labels.items():
    if pidx < len(doc.paragraphs):
        set_text(doc.paragraphs[pidx], text)

# Clear remaining old screenshot labels
for bidx in range(546, 551):
    try: clear_para(doc.paragraphs[bidx])
    except: pass
for bidx in range(614, 631):
    try: clear_para(doc.paragraphs[bidx])
    except: pass

# ===== CHAPTER 10: ADVANTAGES & LIMITATIONS =====
adv_content = [
    'Centralized Platform: All campus services \u2014 attendance, exams, routines, announcements, Lost & Found, and resources \u2014 are available from a single portal.',
    'Real-Time Attendance Visibility: Students can view subject-wise attendance with progress bars, percentages, and dynamic "can miss" calculations.',
    'Role-Based Admin Access: Three admin levels (Principal, HOD, Faculty) with appropriate permissions ensure secure management.',
    'Efficient Attendance Marking: The checkbox interface with select-all/deselect-all makes attendance marking quick. Database transactions ensure data consistency.',
    'Targeted Announcements: Announcements can be targeted to specific departments and semesters for relevant information delivery.',
    'Centralized Resource Repository: Academic resources are organized by department and semester for easy access from one location.',
    'Mobile-Responsive Design: The interface adapts to different screen sizes for access from smartphones and tablets.',
    'Secure Architecture: Prepared statements prevent SQL injection. Session authentication and role-based access control protect the system.',
    'File Management: Class routines, exam schedules, and resources can be uploaded as PDFs or images and displayed inline.',
    'Lost & Found Tracking: Digital tracking with category classification, images, and claim status management.',
]
for i, bidx in enumerate(range(638, 648)):
    set_text(doc.paragraphs[bidx], adv_content[i])

limitations = [
    'No email or SMS notification system \u2014 students are not automatically notified of updates.',
    'Browser-based only \u2014 no companion mobile application, though the interface is mobile-responsive.',
    'No real-time updates \u2014 page refresh is required to see new data; no WebSocket or AJAX polling.',
    'Single institution scope \u2014 designed for ICON Commerce College only, not multi-campus ready.',
    'No fee management or payment processing functionality is integrated.',
    'No online examination or quiz module is included.',
    'Admin passwords are stored as plain text in the database (not hashed with bcrypt).',
]
for i, bidx in enumerate(range(650, 657)):
    set_text(doc.paragraphs[bidx], limitations[i])

# ===== CHAPTER 11: FUTURE ENHANCEMENTS =====
enhancements = [
    'Email and SMS Notifications: Integrate PHPMailer or an SMS gateway to send automated alerts to students when attendance is marked or announcements are posted.',
    'Password Hashing: Implement bcrypt hashing for admin passwords using PHP\'s password_hash() and password_verify() functions.',
    'Mobile Application: Develop a companion Android/iOS app using React Native or Flutter with push notification support.',
    'Real-Time Updates: Implement AJAX polling or WebSocket communication to update dashboard data without manual page refresh.',
    'Graphical Analytics: Add Chart.js or similar library for visual charts of attendance trends and department statistics.',
    'Online Examination Module: Add a quiz/exam system with automatic grading and result compilation.',
    'Complaint Escalation System: Add automatic escalation for unresolved issues based on time thresholds.',
    'Student Feedback and Rating: Allow students to rate resolution quality and provide feedback on services.',
    'Full PDF Export: Add server-side PDF generation for reports and attendance records.',
]
for i, bidx in enumerate(range(678, 687)):
    set_text(doc.paragraphs[bidx], enhancements[i])

# ===== CHAPTER 12: CONCLUSION =====
set_text(doc.paragraphs[714],
    'ICC Companion was developed to address the need for an integrated digital campus management '
    'platform at ICON Commerce College. The system successfully replaces fragmented manual processes '
    'with a unified web-based portal serving both students and administrators.')

set_text(doc.paragraphs[716],
    'The project was implemented using PHP, MySQL, HTML5, CSS3, and JavaScript \u2014 all freely '
    'available technologies. The dual-portal architecture provides separate interfaces for students '
    'and administrators. The twelve-table relational database supports attendance tracking, exam '
    'scheduling, class routine management, announcement distribution, Lost & Found tracking, and '
    'academic resource management.')

set_text(doc.paragraphs[718],
    'From a security perspective, the system implements prepared statements for SQL injection '
    'prevention and session-based authentication for access control. The role-based admin system '
    'ensures users only access functions appropriate for their role.')

set_text(doc.paragraphs[720],
    'The project fulfils the stated objectives and provides a solid foundation for future extensions '
    'such as email notifications, mobile applications, and online examination modules.')

# ===== REFERENCES =====
refs = [
    'PHP Manual. PHP Documentation Group. Available at: https://www.php.net/manual/en/',
    'MySQL Reference Manual. Oracle Corporation. Available at: https://dev.mysql.com/doc/',
    'MDN Web Docs. Mozilla Developer Network. Available at: https://developer.mozilla.org/en-US/docs/Web/JavaScript',
    'W3Schools Online Web Tutorials. Available at: https://www.w3schools.com/',
    'Font Awesome Documentation. Fonticons, Inc. Available at: https://fontawesome.com/docs',
    'OWASP Foundation. Web Application Security Guide. Available at: https://owasp.org/',
    'PHP: The Right Way \u2014 Best Practices for PHP Development. Available at: https://phptherightway.com/',
    'Silberschatz, A., Korth, H. F., & Sudarshan, S. \u2014 Database System Concepts, 7th Edition. McGraw-Hill Education.',
]
for i, bidx in enumerate(range(726, 734)):
    if bidx < len(doc.paragraphs):
        set_text(doc.paragraphs[bidx], refs[i])

# Save
os.makedirs(os.path.dirname(out), exist_ok=True)
doc.save(out)
print(f"Report saved to: {out}")
print(f"Total paragraphs: {len(doc.paragraphs)}, Tables: {len(doc.tables)}")
