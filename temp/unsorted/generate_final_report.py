#!/usr/bin/env python3
"""Generate ICC Companion Project Report for Ankita Chetri"""

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import nsdecls
from docx.oxml import parse_xml

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

def add_heading_custom(text, level=1):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.color.rgb = RGBColor(0, 0, 0)
        run.font.name = 'Times New Roman'
    return h

def add_page_break():
    doc.add_page_break()

def add_para(text, bold=False, italic=False, size=12, align=None, space_after=6, space_before=0):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(space_before)
    if align:
        p.alignment = align
    run = p.add_run(text)
    run.font.size = Pt(size)
    run.font.name = 'Times New Roman'
    run.bold = bold
    run.italic = italic
    return p

def add_body(text, italic=False, align=None):
    p = doc.add_paragraph(text)
    p.paragraph_format.first_line_indent = Cm(1.27)
    p.paragraph_format.space_after = Pt(6)
    p.alignment = align if align else WD_ALIGN_PARAGRAPH.JUSTIFY
    for run in p.runs:
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        if italic:
            run.italic = True
    return p

def add_bullet(text):
    p = doc.add_paragraph(text, style='List Bullet')
    p.paragraph_format.space_after = Pt(3)
    for run in p.runs:
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
    return p

def add_table_custom(headers, data):
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
    doc.add_paragraph()
    return table

# =================== COVER PAGE ===================
add_para('', size=12, space_after=40)

# Logo placeholders
add_para('[Insert College Logo Here]', italic=True, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
add_para('[Insert University Logo Here]', italic=True, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=30)

add_para('A PROJECT REPORT ON', bold=True, size=18, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=20)
add_para('"ICC COMPANION"', bold=True, size=22, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=8)
add_para('(Icon Commerce College Campus Portal)', size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('A Project Report submitted in partial fulfilment of the requirements for the degree of')
run.font.size = Pt(12)
run.font.name = 'Times New Roman'

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('Bachelor of Computer Application (BCA)')
run.bold = True
run.font.size = Pt(14)
run.font.name = 'Times New Roman'

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('Under Gauhati University')
run.bold = True
run.font.size = Pt(13)
run.font.name = 'Times New Roman'

add_para('', size=12, space_after=20)

# Info table
t = doc.add_table(rows=5, cols=2)
t.alignment = WD_TABLE_ALIGNMENT.CENTER
info = [
    ('Name of the Guide:', 'Urbimala Hazarika, Asst. Prof'),
    ('Department:', 'Bachelor of Computer Application'),
    ('Institution:', 'ICON Commerce College, Guwahati-781003'),
    ('Submitted By:', 'Ankita Chetri'),
    ('Roll No:', 'UT-231-049-0012'),
]
for i, (k, v) in enumerate(info):
    cell0 = t.rows[i].cells[0]
    cell1 = t.rows[i].cells[1]
    p0 = cell0.paragraphs[0]
    r0 = p0.add_run(k)
    r0.bold = True if i < 3 else False
    r0.font.size = Pt(12)
    r0.font.name = 'Times New Roman'
    p1 = cell1.paragraphs[0]
    r1 = p1.add_run(v)
    r1.font.size = Pt(12)
    r1.font.name = 'Times New Roman'

add_para('', size=12, space_after=12)
add_para('Registration No: 23084898', size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
add_para('BCA 6th Semester (FYUGP)', bold=True, size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('Academic Session 2025\u20132026', size=12, align=WD_ALIGN_PARAGRAPH.CENTER)

# =================== CERTIFICATE ===================
add_page_break()
add_para('CERTIFICATE', bold=True, size=18, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24)

add_body('This is to certify that the project entitled "ICC COMPANION" has been submitted by Ankita Chetri (Roll No: UT-231-049-0012, Registration No: 23084898) in partial fulfilment of the requirements for the degree of Bachelor of Computer Applications (BCA), 6th Semester, at Icon Commerce College, Gauhati University, during the Academic Session 2025\u20132026.')

add_body('This is an authentic work carried out by her under my supervision and guidance. The project has not been submitted to any other university or institution for the award of any degree or diploma.')

add_para('', space_after=12)
add_para('Date: ____________________', size=12, space_after=24)
add_para('Name of the Guide: Urbimala Hazarika', size=12, space_after=6)
add_para('Designation: Assistant Professor', size=12, space_after=6)
add_para('Department: Bachelor of Computer Application', size=12, space_after=6)
add_para('Institution: Icon Commerce College, Guwahati \u2013 781021', size=12, space_after=24)
add_para('Signature of the Guide: ____________________', size=12)

# =================== DECLARATION ===================
add_page_break()
add_para('DECLARATION', bold=True, size=18, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24)

add_body('I hereby declare that the project report \u201cICC Companion\u201d, submitted in partial fulfilment of the requirement for the degree of Bachelor of Computer Application (BCA) in Icon Commerce College, under Gauhati University, is my original work and has not been submitted for the award of any other degree, diploma, fellowship or any other similar titles.')

add_para('', space_after=12)
add_para('Date: ____________________', size=12, space_after=6)
add_para('Signature: ________________', size=12, space_after=24)
add_para('Place: Guwahati', size=12, space_after=6)
add_para('NAME: ANKITA CHETRI', bold=True, size=12, space_after=6)
add_para('ROLL NO: UT-231-049-0012', size=12, space_after=6)
add_para('REGISTRATION NO: 23084898', size=12, space_after=6)
add_para('DEPARTMENT: BCA 6TH SEMESTER', size=12, space_after=6)
add_para('ICON COMMERCE COLLEGE', size=12)

# =================== ACKNOWLEDGEMENT ===================
add_page_break()
add_para('ACKNOWLEDGEMENT', bold=True, size=18, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24)

add_body('I would like to express my sincere gratitude to my project guide and mentor Urbimala Hazarika for her invaluable guidance, encouragement, and constructive feedback throughout the development of this project. Her insights and timely advice have been instrumental in shaping this work.')

add_body('I am grateful to Dr. Mandira Saha, Principal of Icon Commerce College, and Tridib Kr. Handique, Co-Ordinator of the BCA Department, for providing the necessary resources and permission to undertake this project. I also extend my thanks to the entire BCA faculty for their continuous support.')

add_body('I would like to thank my family and friends for their unwavering encouragement and understanding during the course of this project.')

add_para('', space_after=12)
add_para('Place: Guwahati', size=12, space_after=6)
add_para('Date: ____________________', size=12, space_after=6)
add_para('Ankita Chetri', bold=True, size=12, space_after=6)
add_para('Roll No: UT-231-049-0012', size=12, space_after=6)
add_para('BCA 6th Semester, Icon Commerce College', size=12)

# =================== ABSTRACT ===================
add_page_break()
add_para('ABSTRACT', bold=True, size=18, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24)

add_body('ICC Companion is a web-based campus portal developed for ICON Commerce College using PHP, MySQL, HTML5, CSS3, and JavaScript. The system provides a unified digital platform where students can access attendance records, exam timetables, class routines, academic resources, college announcements, and a Lost & Found portal. Administrators can manage student records, mark attendance, schedule examinations, post announcements, manage Lost & Found items, upload class routines, and publish academic resources through a role-based admin panel.')

add_body('The system employs a MySQL database with twelve interconnected tables and uses PHP for server-side logic with prepared statements for database security. The frontend is built with vanilla JavaScript using the Fetch API for asynchronous data exchange in JSON format. The system supports three admin roles \u2014 Principal (super-admin), HOD (dept-admin), and Faculty \u2014 each with appropriate access restrictions.')

add_body('The project was developed using the XAMPP server environment and follows a mobile-first responsive design approach for accessibility across devices.')

# =================== TABLE OF CONTENTS ===================
add_page_break()
add_para('TABLE OF CONTENTS', bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24)

toc_items = [
    ('Chapter 1: Introduction', 1),
    ('    1.1 Background', 1),
    ('    1.2 Problem Statement', 2),
    ('    1.3 Proposed Solution', 2),
    ('Chapter 2: Objectives of the Project', 3),
    ('Chapter 3: Scope of the Project', 4),
    ('Chapter 4: System Analysis', 5),
    ('    4.1 Existing System', 5),
    ('    4.2 Proposed System', 6),
    ('    4.3 Feasibility Study', 6),
    ('Chapter 5: System Design', 7),
    ('    5.1 System Architecture', 7),
    ('    5.2 Data Flow Diagram', 8),
    ('    5.3 Entity-Relationship Diagram', 8),
    ('Chapter 6: Database Design', 9),
    ('Chapter 7: Technology Used', 12),
    ('Chapter 8: Implementation / Working', 13),
    ('Chapter 9: Screenshots', 18),
    ('Chapter 10: Advantages & Limitations', 22),
    ('Chapter 11: Future Enhancements', 24),
    ('Chapter 12: Conclusion', 25),
    ('Bibliography', 26),
]

for item, page in toc_items:
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    is_chapter = not item.startswith('    ')
    run = p.add_run(item)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run.bold = is_chapter

# =================== CHAPTER 1: INTRODUCTION ===================
add_page_break()
add_para('Chapter 1', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
add_para('INTRODUCTION', bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=16)

add_heading_custom('1.1 Background', level=2)
add_body('In educational institutions, students interact with numerous administrative processes daily \u2014 checking attendance, accessing exam schedules, viewing class routines, reading announcements, and managing academic resources. Traditionally, many of these activities rely on physical notice boards, paper records, or informal communication channels, which can be inefficient and difficult to track.')

add_body('With the increasing adoption of web technologies in education, a centralized campus portal can streamline these processes by providing a single platform for students and administrators. ICON Commerce College, affiliated with Gauhati University, offers BCA, BBA, BA, and B.COM programmes across six semesters. The need for an integrated digital platform to serve students and staff across these departments motivated this project.')

add_heading_custom('1.2 Problem Statement', level=2)
add_body('The lack of a centralized digital platform in the college leads to specific challenges:')
add_bullet('Attendance records are maintained manually, giving students no real-time visibility into their attendance status.')
add_bullet('Exam schedules and class routines are shared through printed notices or verbal announcements, which can be missed.')
add_bullet('College announcements and important notices lack a permanent, searchable archive.')
add_bullet('The Lost & Found process relies on physical boards with no centralized tracking.')
add_bullet('Administrators lack a consolidated view of student data, attendance patterns, and academic schedules.')
add_bullet('Academic resources such as syllabi and study materials are distributed through email or printed copies without a central repository.')

add_heading_custom('1.3 Proposed Solution', level=2)
add_body('ICC Companion is a web-based campus portal developed using PHP and MySQL. Students log in using their roll number and date of birth to access attendance records with visual progress bars, view exam timetables with countdown timers, browse class routines, read college announcements, use the Lost & Found portal, and download academic resources.')

add_body('Administrators access a separate management panel where they can perform CRUD operations on student records, mark attendance through a checkbox interface, schedule examinations, post targeted announcements, manage Lost & Found items, upload class routines, and publish academic resources. The system implements role-based access control with three admin levels \u2014 Principal, HOD, and Faculty \u2014 each with appropriate permissions.')

# =================== CHAPTER 2: OBJECTIVES ===================
add_page_break()
add_para('Chapter 2', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
add_para('OBJECTIVES OF THE PROJECT', bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=16)

add_body('The following objectives were identified for the ICC Companion project:')

objectives = [
    'To provide students with a dedicated login portal using roll number and date of birth for secure access.',
    'To display attendance records with subject-wise progress bars, overall percentage, and dynamic indicators such as classes that can be missed.',
    'To present exam timetables with separate Sessional and Final sections, including subject names, dates, times, rooms, and countdown indicators.',
    'To allow students to view class routines as uploaded PDF or image files for their specific department and semester.',
    'To provide a centralized announcements feed with priority indicators (High/Medium/Low) and target audience filtering.',
    'To implement a Lost & Found portal where students can browse items by type and category.',
    'To provide access to academic resources including syllabi, books, study materials, links, and text content, filterable by department and semester.',
    'To enable administrators to manage student records with full CRUD operations, search, and department/semester filtering.',
    'To provide a smart attendance marking interface with checkbox selection, select-all/deselect-all, and database transaction-based saving.',
    'To allow administrators to schedule examinations with subject, date, time, room, and type (Sessional/Final).',
    'To provide administrators with tools to post, edit, and delete announcements with priority levels, targeting, and file attachments.',
    'To implement role-based access control with three admin roles: super-admin (Principal), dept-admin (HOD), and faculty.',
]

for obj in objectives:
    add_bullet(obj)

# =================== CHAPTER 3: SCOPE ===================
add_page_break()
add_para('Chapter 3', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
add_para('SCOPE OF THE PROJECT', bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=16)

add_body('ICC Companion is designed to serve the campus management needs of ICON Commerce College. The system supports two categories of users \u2014 students and administrators \u2014 through separate, secure portals.')

add_heading_custom('3.1 In Scope', level=2)
in_scope = [
    'Student login using roll number and date of birth.',
    'Student dashboard displaying attendance percentage, upcoming exams count, and announcement count.',
    'Subject-wise attendance tracking with progress bars and attendance status (Safe/Warning/Shortage).',
    'Exam timetable viewing with countdown days for upcoming exams.',
    'Class routine viewing with inline PDF and image display.',
    'Centralized announcements feed with priority badges and target audience display.',
    'Lost & Found browsing with filters for item type and category.',
    'Academic resources browsing with search and type filters.',
    'Admin CRUD operations for student records with department and semester filters.',
    'Attendance marking through a checkbox-based interface with database transaction support.',
    'Exam scheduling with subject, date, time, room, and exam type fields.',
    'Announcement management with posting, editing, deletion, priority setting, and file attachments.',
    'Class routine management with upload, editing, and deletion.',
    'Lost & Found management with item addition, editing, deletion, and claim marking.',
    'Academic resource management with file upload, link, and text content support.',
    'Department management (super-admin only) with CRUD operations.',
    'Faculty management (super-admin only) with role assignment and subject assignments.',
    'Role-based access control with three admin levels.',
]
for item in in_scope:
    add_bullet(item)

add_heading_custom('3.2 Out of Scope', level=2)
out_scope = [
    'Automated email or SMS notifications are not implemented.',
    'The system is designed for a single college and does not support multi-campus configurations.',
    'No companion mobile application is available \u2014 the system is browser-based only (though mobile-responsive).',
    'No real-time chat or messaging feature is included.',
    'No fee management or payment gateway integration exists.',
    'No online examination or quiz functionality is provided.',
]
for item in out_scope:
    add_bullet(item)

# =================== CHAPTER 4: SYSTEM ANALYSIS ===================
add_page_break()
add_para('Chapter 4', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
add_para('SYSTEM ANALYSIS', bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=16)

add_heading_custom('4.1 Existing System', level=2)
add_body('Currently, campus information at ICON Commerce College is managed through traditional methods. Attendance is recorded in registers or spreadsheets not accessible to students in real time. Exam schedules and class routines are posted on physical notice boards. Announcements are made verbally or through printed circulars. Lost & Found items are managed informally. Academic resources are distributed through email or as printed handouts.')

add_body('These approaches have limitations: students cannot access information remotely, there is no permanent searchable archive, administrators lack consolidated views, and tracking historical data is difficult.')

add_heading_custom('4.2 Proposed System', level=2)
add_body('ICC Companion replaces these fragmented methods with a unified web-based platform. All data is stored in a MySQL database with permanent records. Students can access attendance, timetables, routines, announcements, and resources 24/7 from any device with a browser. Administrators have a centralized dashboard for managing all aspects of campus operations.')

add_heading_custom('4.3 Feasibility Study', level=2)

p = doc.add_paragraph()
run = p.add_run('Technical Feasibility: ')
run.bold = True
run.font.size = Pt(12)
run.font.name = 'Times New Roman'
run2 = p.add_run('The system uses PHP, MySQL, HTML5, CSS3, and JavaScript \u2014 all freely available technologies that can be hosted on any standard Apache server. No proprietary software is required.')
run2.font.size = Pt(12)
run2.font.name = 'Times New Roman'

p = doc.add_paragraph()
run = p.add_run('Economic Feasibility: ')
run.bold = True
run.font.size = Pt(12)
run.font.name = 'Times New Roman'
run2 = p.add_run('All technologies used are open-source and free. The system can be deployed on a standard XAMPP setup with minimal operational cost.')
run2.font.size = Pt(12)
run2.font.name = 'Times New Roman'

p = doc.add_paragraph()
run = p.add_run('Operational Feasibility: ')
run.bold = True
run.font.size = Pt(12)
run.font.name = 'Times New Roman'
run2 = p.add_run('The system has an intuitive interface. Students can log in and navigate easily. Administrators can manage operations without specialized technical training.')
run2.font.size = Pt(12)
run2.font.name = 'Times New Roman'

# =================== CHAPTER 5: SYSTEM DESIGN ===================
add_page_break()
add_para('Chapter 5', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
add_para('SYSTEM DESIGN', bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=16)

add_heading_custom('5.1 System Architecture', level=2)
add_body('The system follows a three-tier architecture. The Presentation Layer consists of HTML, CSS, and JavaScript running in the browser. The Application Layer comprises PHP scripts on the Apache server that handle business logic, authentication, and database interaction. The Data Layer is the MySQL database that stores all application data. Communication between the frontend and backend occurs through JSON-based API calls using the Fetch API.')

add_body('[Insert System Architecture Diagram Here]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)

add_heading_custom('5.2 Data Flow Diagram', level=2)
add_body('The Data Flow Diagram illustrates how data moves between external entities (Students and Administrators), the system processes, and the data stores. At Level 0, the system is shown as a single process with two external entities. At Level 1, the system is broken into major processes: Student Authentication, Attendance Management, Exam Timetable Viewing, Announcement Management, Lost & Found Management, Resource Management, and Admin Operations.')

add_body('[Insert DFD Level 0 Diagram Here]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)
add_body('[Insert DFD Level 1 Diagram Here]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)

add_heading_custom('5.3 Entity-Relationship Diagram', level=2)
add_body('The ER Diagram represents the database entities and their relationships. The central entities in the system are students, departments, subjects, attendance, exams, lost_found, announcements, class_routines, resources, admins, exam_schedules, and faculty_subjects. Students are linked to departments and attendance records. Subjects belong to departments. Attendance records connect students to subjects with date and status. Exams are linked to subjects. Announcements and class routines are associated with departments and semesters.')

add_body('[Insert ER Diagram Here]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)

# =================== CHAPTER 6: DATABASE DESIGN ===================
add_page_break()
add_para('Chapter 6', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
add_para('DATABASE DESIGN', bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=16)

add_body('The system uses a MySQL database named campus_portal with twelve tables. The design enforces referential integrity through foreign key constraints and prevents duplicate records through unique key constraints where applicable.')

add_para('Table 1: departments', bold=True, size=12, space_before=6)
add_table_custom(
    ['Field', 'Type', 'Constraints', 'Description'],
    [
        ('dept_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique department identifier'),
        ('dept_code', 'VARCHAR(10)', 'UNIQUE, NOT NULL', 'Short code (BCA, BBA, etc.)'),
        ('dept_name', 'VARCHAR(100)', 'NOT NULL', 'Full department name'),
        ('max_semesters', 'INT', 'DEFAULT 6', 'Number of semesters'),
    ]
)

add_para('Table 2: subjects', bold=True, size=12, space_before=6)
add_table_custom(
    ['Field', 'Type', 'Constraints', 'Description'],
    [
        ('subject_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique subject identifier'),
        ('subject_code', 'VARCHAR(20)', 'NOT NULL', 'Subject code'),
        ('subject_name', 'VARCHAR(100)', 'NOT NULL', 'Subject name'),
        ('dept_code', 'VARCHAR(10)', 'FK \u2192 departments', 'Parent department'),
        ('semester', 'INT', 'NOT NULL', 'Semester number'),
    ]
)

add_para('Table 3: students', bold=True, size=12, space_before=6)
add_table_custom(
    ['Field', 'Type', 'Constraints', 'Description'],
    [
        ('student_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique identifier'),
        ('roll_number', 'VARCHAR(20)', 'UNIQUE, NOT NULL', 'Login credential'),
        ('name', 'VARCHAR(100)', 'NOT NULL', 'Student full name'),
        ('dob', 'DATE', 'NOT NULL', 'Date of birth (password)'),
        ('email', 'VARCHAR(100)', '', 'Email address'),
        ('phone', 'VARCHAR(15)', '', 'Contact number'),
        ('dept_code', 'VARCHAR(10)', 'FK \u2192 departments', 'Department'),
        ('semester', 'INT', 'NOT NULL', 'Current semester'),
        ('created_at', 'TIMESTAMP', 'DEFAULT NOW()', 'Registration timestamp'),
    ]
)

add_para('Table 4: admins', bold=True, size=12, space_before=6)
add_table_custom(
    ['Field', 'Type', 'Constraints', 'Description'],
    [
        ('admin_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique identifier'),
        ('username', 'VARCHAR(50)', 'UNIQUE, NOT NULL', 'Login username'),
        ('password', 'VARCHAR(255)', 'NOT NULL', 'Login password'),
        ('name', 'VARCHAR(100)', 'NOT NULL', 'Admin full name'),
        ('role', 'VARCHAR(50)', 'DEFAULT \'admin\'', 'super-admin/dept-admin/faculty'),
        ('assigned_dept', 'VARCHAR(10)', 'DEFAULT \'all\'', 'Department scope'),
        ('assigned_semester', 'VARCHAR(10)', 'DEFAULT \'all\'', 'Semester scope'),
    ]
)

add_para('Table 5: attendance', bold=True, size=12, space_before=6)
add_table_custom(
    ['Field', 'Type', 'Constraints', 'Description'],
    [
        ('attendance_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique identifier'),
        ('roll_number', 'VARCHAR(20)', 'FK \u2192 students', 'Student identifier'),
        ('subject_id', 'INT', 'FK \u2192 subjects', 'Subject identifier'),
        ('attendance_date', 'DATE', 'NOT NULL', 'Date of class'),
        ('status', 'ENUM(\'present\',\'absent\')', 'NOT NULL', 'Attendance status'),
        ('marked_by', 'VARCHAR(50)', '', 'Admin who marked'),
        ('created_at', 'TIMESTAMP', 'DEFAULT NOW()', 'Record timestamp'),
    ]
)
add_body('Unique constraint on (roll_number, subject_id, attendance_date) prevents duplicate entries.')

add_para('Table 6: exams', bold=True, size=12, space_before=6)
add_table_custom(
    ['Field', 'Type', 'Constraints', 'Description'],
    [
        ('exam_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique identifier'),
        ('subject_id', 'INT', 'FK \u2192 subjects', 'Exam subject'),
        ('exam_date', 'DATE', 'NOT NULL', 'Date of examination'),
        ('start_time', 'TIME', 'NOT NULL', 'Start time'),
        ('end_time', 'TIME', 'NOT NULL', 'End time'),
        ('room', 'VARCHAR(50)', '', 'Exam room'),
        ('exam_type', 'ENUM(\'sessional\',\'final\')', 'DEFAULT \'final\'', 'Type of exam'),
        ('attachment_url', 'VARCHAR(255)', '', 'Schedule file link'),
    ]
)

add_para('Table 7: lost_found', bold=True, size=12, space_before=6)
add_table_custom(
    ['Field', 'Type', 'Constraints', 'Description'],
    [
        ('item_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique identifier'),
        ('title', 'VARCHAR(100)', 'NOT NULL', 'Item title'),
        ('description', 'TEXT', '', 'Item description'),
        ('category', 'ENUM(...)', 'DEFAULT \'other\'', 'id-card/phone/wallet/books/electronics/other'),
        ('item_type', 'ENUM(\'lost\',\'found\')', 'NOT NULL', 'Lost or Found'),
        ('location', 'VARCHAR(100)', '', 'Where found/lost'),
        ('item_date', 'DATE', '', 'Date of incident'),
        ('contact_info', 'VARCHAR(100)', '', 'Contact details'),
        ('image_url', 'VARCHAR(255)', '', 'Item image path'),
        ('status', 'ENUM(\'active\',\'claimed\')', 'DEFAULT \'active\'', 'Current status'),
        ('posted_by', 'VARCHAR(50)', '', 'Who reported'),
        ('created_at', 'TIMESTAMP', 'DEFAULT NOW()', 'Submission timestamp'),
    ]
)

add_para('Table 8: announcements', bold=True, size=12, space_before=6)
add_table_custom(
    ['Field', 'Type', 'Constraints', 'Description'],
    [
        ('announcement_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique identifier'),
        ('title', 'VARCHAR(200)', 'NOT NULL', 'Announcement title'),
        ('description', 'TEXT', 'NOT NULL', 'Announcement content'),
        ('attachment_url', 'VARCHAR(255)', '', 'File attachment'),
        ('link_url', 'VARCHAR(255)', '', 'External link'),
        ('priority', 'ENUM(\'high\',\'medium\',\'low\')', 'DEFAULT \'medium\'', 'Priority level'),
        ('target_dept', 'VARCHAR(50)', 'DEFAULT \'all\'', 'Target department'),
        ('target_semester', 'VARCHAR(20)', 'DEFAULT \'all\'', 'Target semester'),
        ('posted_by', 'VARCHAR(50)', '', 'Posted by'),
        ('created_at', 'TIMESTAMP', 'DEFAULT NOW()', 'Posting timestamp'),
    ]
)

add_para('Table 9: class_routines', bold=True, size=12, space_before=6)
add_table_custom(
    ['Field', 'Type', 'Constraints', 'Description'],
    [
        ('routine_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique identifier'),
        ('title', 'VARCHAR(200)', 'NOT NULL', 'Routine title'),
        ('file_url', 'VARCHAR(255)', 'NOT NULL', 'PDF/image file path'),
        ('dept_code', 'VARCHAR(10)', 'NOT NULL', 'Department'),
        ('semester', 'VARCHAR(10)', 'NOT NULL', 'Semester'),
        ('created_at', 'TIMESTAMP', 'DEFAULT NOW()', 'Upload timestamp'),
    ]
)

add_para('Table 10: exam_schedules', bold=True, size=12, space_before=6)
add_table_custom(
    ['Field', 'Type', 'Constraints', 'Description'],
    [
        ('schedule_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique identifier'),
        ('schedule_type', 'ENUM(\'sessional\',\'final\')', 'NOT NULL', 'Sessional or Final'),
        ('file_url', 'VARCHAR(255)', 'NOT NULL', 'PDF/image file path'),
        ('dept_code', 'VARCHAR(10)', 'NOT NULL', 'Department'),
        ('semester', 'VARCHAR(10)', 'NOT NULL', 'Semester'),
        ('created_at', 'TIMESTAMP', 'DEFAULT NOW()', 'Upload timestamp'),
    ]
)

add_para('Table 11: resources', bold=True, size=12, space_before=6)
add_table_custom(
    ['Field', 'Type', 'Constraints', 'Description'],
    [
        ('resource_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique identifier'),
        ('title', 'VARCHAR(200)', 'NOT NULL', 'Resource title'),
        ('description', 'TEXT', '', 'Short description'),
        ('resource_type', 'ENUM(...)', 'NOT NULL', 'syllabus/book/material/link/text/others'),
        ('file_url', 'VARCHAR(255)', '', 'Uploaded file path'),
        ('link_url', 'TEXT', '', 'External URL'),
        ('content_text', 'TEXT', '', 'Inline text content'),
        ('dept_code', 'VARCHAR(10)', 'FK \u2192 departments', 'Department'),
        ('semester', 'VARCHAR(10)', 'NOT NULL', 'Semester'),
        ('subject_id', 'INT', 'FK \u2192 subjects', 'Related subject'),
        ('posted_by', 'VARCHAR(50)', '', 'Who uploaded'),
        ('created_at', 'TIMESTAMP', 'DEFAULT NOW()', 'Upload timestamp'),
    ]
)

add_para('Table 12: faculty_subjects', bold=True, size=12, space_before=6)
add_table_custom(
    ['Field', 'Type', 'Constraints', 'Description'],
    [
        ('assignment_id', 'INT', 'PK, AUTO_INCREMENT', 'Unique identifier'),
        ('admin_id', 'INT', 'FK \u2192 admins', 'Faculty identifier'),
        ('subject_id', 'INT', 'FK \u2192 subjects', 'Assigned subject'),
        ('created_at', 'TIMESTAMP', 'DEFAULT NOW()', 'Assignment timestamp'),
    ]
)

# =================== CHAPTER 7: TECHNOLOGY USED ===================
add_page_break()
add_para('Chapter 7', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
add_para('TECHNOLOGY USED', bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=16)

add_table_custom(
    ['Technology', 'Purpose in Project'],
    [
        ('PHP 7.4+', 'Server-side scripting for form processing, session management, database interaction, file uploads, and authentication.'),
        ('MySQL 5.7+', 'Relational database storing all application data across 12 tables.'),
        ('HTML5', 'Semantic structure for all web pages \u2014 login, dashboards, forms, tables, and portals.'),
        ('CSS3', 'Responsive styling, layout grid, sidebar navigation, cards, badges, and mobile-first design.'),
        ('Vanilla JavaScript', 'Client-side logic: form validation, Fetch API calls, DOM manipulation, search/filter, dynamic content rendering.'),
        ('MySQLi Extension', 'Database connectivity with prepared statements for SQL injection prevention.'),
        ('PHP Sessions', 'Maintaining authenticated state for both students and administrators.'),
        ('Apache (XAMPP)', 'Web server environment for running PHP and serving the application.'),
        ('Font Awesome 6.4.0', 'Icon library for navigation icons, stat cards, and action buttons.'),
        ('Google Fonts (Outfit)', 'Custom typography for enhanced visual appearance (admin panel).'),
    ]
)

# =================== CHAPTER 8: IMPLEMENTATION ===================
add_page_break()
add_para('Chapter 8', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
add_para('IMPLEMENTATION / WORKING', bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=16)

add_body('The system is divided into two portals \u2014 Student Portal and Admin Portal \u2014 each with distinct functionalities and authentication mechanisms.')

add_heading_custom('8.1 Home Page (index.html)', level=2)
add_body('The public landing page displays the college branding, a hero section describing the portal, and feature cards highlighting key functionalities. Two call-to-action buttons direct users to the Student Login or Admin Login page. This page does not require authentication.')

add_heading_custom('8.2 Student Login (student-login.html)', level=2)
add_body('Students log in by entering their roll number and date of birth. The form sends a POST request to api/student-login.php. The PHP script queries the students table using a prepared statement, verifies the credentials, and returns the student data in JSON format. On success, the frontend stores the student details in sessionStorage and redirects to the student dashboard.')

add_heading_custom('8.3 Student Dashboard (student/dashboard.html)', level=2)
add_body('The dashboard is the central hub. It displays a welcome card with student details (name, roll number, department, semester). Three stat cards show overall attendance percentage, number of upcoming exams, and total announcements \u2014 all fetched via separate API calls. A quick access menu provides links to all student modules. The latest three announcements are displayed at the bottom.')

add_heading_custom('8.4 My Subjects (student/subjects.html)', level=2)
add_body('This page displays the list of subjects for the student\'s department and semester. Data is fetched from api/get-subjects.php with dept and semester parameters. Each subject card shows the subject code, name, and department/semester info.')

add_heading_custom('8.5 Academic Resources (student/resources.html)', level=2)
add_body('Students can browse resources filtered by their department and semester. Resources can be of type syllabus, book, study material, link, or text. Each resource card displays a download button for files, a link button for URLs, or a read button for inline text content. A search input and type filter allow further refinement.')

add_heading_custom('8.6 My Attendance (student/attendance.html)', level=2)
add_body('Attendance is displayed subject-wise with progress bars showing the percentage for each subject. The overall attendance percentage is calculated and displayed at the top. Each subject card shows the number of classes attended out of total, a color-coded progress bar (green for Safe >= 75%, orange for Warning >= 65%, red for Shortage < 65%), and a dynamic message indicating how many more classes can be missed or that more classes need to be attended.')

add_heading_custom('8.7 Exam Timetable (student/exams.html)', level=2)
add_body('Exams are organized into two sections \u2014 Sessional and Final. Each exam entry shows the date, subject name, time range, room location, and a countdown badge (days remaining, "Today!", or "Done"). If a schedule file (PDF or image) has been uploaded, it is displayed at the top of the relevant section with inline preview.')

add_heading_custom('8.8 Class Routine (student/routines.html)', level=2)
add_body('The latest class routine for the student\'s department and semester is displayed. PDF files are embedded inline using an iframe, images are displayed directly, and other file types show a download link. The title and last update date are shown at the top.')

add_heading_custom('8.9 Lost & Found (student/lost-found.html)', level=2)
add_body('Students can browse Lost & Found items with filters for item type (Lost/Found) and category (ID Cards, Phones, Wallets, Books, Electronics, Other). Each item card displays a category icon or uploaded image, type badge, title, location, date, description, and contact information.')

add_heading_custom('8.10 Announcements (student/announcements.html)', level=2)
add_body('Announcements are displayed in descending order by date. Each announcement card has a color-coded left border based on priority (High = red, Medium = blue) and a priority badge (Urgent for High, Important for Medium). The title, description, target department/semester, date, and any attachment or link are displayed.')

add_page_break()
add_heading_custom('8.11 Admin Login (admin-login.html)', level=2)
add_body('Admins log in using username and password. Three role tabs (Faculty, HOD, Principal) allow the user to select their role. The form sends a POST request to api/admin-login.php, which validates credentials and checks that the user\'s role matches the selected tab. On success, admin details including role, assigned department, and assigned semester are stored in sessionStorage.')

add_heading_custom('8.12 Admin Dashboard (admin/dashboard.html)', level=2)
add_body('The admin dashboard displays a welcome banner with the admin\'s name and role badge (Principal/HOD/Faculty). Four stat cards show total students, upcoming exams, active Lost & Found items, and total announcements. A quick actions menu links to all admin modules. A "Students by Department" section shows the distribution of students across departments. Role-based visibility hides Principal-only modules (Staff Management, Departments) from non-Principal users.')

add_heading_custom('8.13 Manage Students (admin/students.html)', level=2)
add_body('Administrators can view, add, edit, and delete student records. Filters allow narrowing by department and semester. A search input filters by roll number or name. The add/edit form includes fields for roll number, name, date of birth, department, semester, phone, and email. Faculty-level admins can only view student data without edit or delete options.')

add_heading_custom('8.14 Attendance Management (admin/attendance.html)', level=2)
add_body('This module has two tabs: Mark Attendance and View Records. To mark attendance, the admin selects the department, semester, subject, and date. A list of enrolled students is displayed with checkboxes. The admin can select or deselect all students with one click, or mark individually. On save, the system sends attendance data as a JSON array to api/save-attendance.php, which uses a database transaction to delete existing records for that date/subject and insert fresh ones. The View Records tab shows attendance summaries by student or for all students.')

add_heading_custom('8.15 Manage Exams (admin/exams.html)', level=2)
add_body('Exams are managed in two sections: Sessional and Final. Administrators can add, edit, and delete exam entries with fields for date, subject, time, and room. Schedule files (PDF/images) can be uploaded for each exam type and department/semester combination. Uploaded schedules are displayed with view and delete options.')

add_heading_custom('8.16 Manage Announcements (admin/announcements.html)', level=2)
add_body('Administrators can post, edit, and delete announcements. Each announcement includes a title, description, priority level (High/Medium/Low), target department, target semester, optional file attachment, and optional external link. Posted announcements are displayed in a table with edit and delete buttons.')

add_heading_custom('8.17 Manage Class Routines (admin/routines.html)', level=2)
add_body('Administrators can upload, edit, and delete class routines. Each routine entry has a title, department, semester, and file (PDF or image). Uploaded routines are displayed in a table with view, edit, and delete options.')

add_heading_custom('8.18 Manage Lost & Found (admin/lost-found.html)', level=2)
add_body('Administrators can add, edit, and delete Lost & Found items. Each item includes title, type (Lost/Found), category, date, location, description, contact info, and optional image. Items can be marked as "Claimed" with one click. The table displays all items with their current status.')

add_heading_custom('8.19 Manage Resources (admin/resources.html)', level=2)
add_body('Administrators can add, edit, and delete academic resources. Resources can be file-based (syllabus, book, material, others), link-based, or text-based. The form dynamically shows the appropriate input fields based on the selected resource type. Filters for department, semester, and type allow easy navigation.')

add_heading_custom('8.20 Manage Faculty (admin/staff.html)', level=2)
add_body('Available only to super-admin (Principal). Administrators can add, edit, and delete faculty accounts. Each faculty member has a username, password, name, role (Faculty/HOD/Principal), assigned department, and assigned semester. Faculty members can also be assigned specific subjects through a subject assignment modal.')

add_heading_custom('8.21 Manage Departments (admin/departments.html)', level=2)
add_body('Available only to super-admin (Principal). Administrators can add, edit, and delete departments. Each department has a code (e.g., BCA), full name, and maximum semester count.')

add_heading_custom('8.22 Security Implementation', level=2)
add_body('Security is implemented at multiple levels:')
add_bullet('Session-based authentication using PHP sessions for backend and sessionStorage for frontend.')
add_bullet('SQL injection prevention through MySQLi prepared statements with bind_param() across all database queries.')
add_bullet('Input sanitization using trim(), stripslashes(), and htmlspecialchars().')
add_bullet('Role-based access control with three admin levels \u2014 each page enforces the appropriate permissions.')
add_bullet('Frontend role enforcement: admin sidebar and action buttons are conditionally shown/hidden based on role.')
add_bullet('File upload validation: uploaded files are validated for accepted types and renamed using uniqid().')

# =================== CHAPTER 9: SCREENSHOTS ===================
add_page_break()
add_para('Chapter 9', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
add_para('SCREENSHOTS', bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=16)

add_body('The following screenshots illustrate the key pages and functionalities of ICC Companion. Actual screenshots should be inserted at the indicated positions.')

add_para('[Screenshot: Home Page \u2014 Public landing page with hero section and feature cards]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('[Screenshot: Student Login Page \u2014 Login form with roll number and date of birth fields]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('[Screenshot: Student Dashboard \u2014 Welcome card, stat cards, and quick access menu]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('[Screenshot: My Subjects Page \u2014 Subject cards with code, name, and semester]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('[Screenshot: Attendance Page \u2014 Subject-wise progress bars with attendance status]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('[Screenshot: Exam Timetable Page \u2014 Sessional and Final exam listings with countdown badges]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('[Screenshot: Class Routine Page \u2014 Inline PDF/image display of class timetable]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('[Screenshot: Lost & Found Page \u2014 Item cards with type badges and filter options]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('[Screenshot: Announcements Page \u2014 Priority-coded announcement cards with details]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('[Screenshot: Academic Resources Page \u2014 Resource cards with type badges and action buttons]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('[Screenshot: Admin Login Page \u2013 Role tabs (Faculty/HOD/Principal) and login form]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('[Screenshot: Admin Dashboard \u2014 Welcome banner, stat cards, and quick actions]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('[Screenshot: Manage Students Page \u2014 Student table with filters and add/edit modal]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('[Screenshot: Mark Attendance Page \u2014 Checkbox list with select/deselect options]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('[Screenshot: Manage Exams Page \u2014 Sessional and Final sections with add/edit forms]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('[Screenshot: Post Announcement Page \u2014 Announcement form with priority and target fields]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('[Screenshot: Manage Faculty Page \u2014 Faculty table with subject assignment modal]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_para('[Screenshot: Manage Departments Page \u2014 Department list with add/edit form]', italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)

# =================== CHAPTER 10: ADVANTAGES & LIMITATIONS ===================
add_page_break()
add_para('Chapter 10', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
add_para('ADVANTAGES AND LIMITATIONS', bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=16)

add_heading_custom('10.1 Advantages', level=2)
advantages = [
    ('Centralized Platform: ', 'All campus services \u2014 attendance, exams, routines, announcements, Lost & Found, and resources \u2014 are available from a single portal.'),
    ('Real-Time Attendance Visibility: ', 'Students can view subject-wise attendance with progress bars, percentages, and dynamic "can miss" calculations.'),
    ('Role-Based Admin Access: ', 'Three admin levels (Principal, HOD, Faculty) with appropriate permissions ensure secure and organized management.'),
    ('Efficient Attendance Marking: ', 'The checkbox-based interface with select-all/deselect-all makes attendance marking quick. Database transactions ensure data consistency.'),
    ('Targeted Announcements: ', 'Announcements can be targeted to specific departments and semesters, ensuring relevant information reaches the right audience.'),
    ('Centralized Resource Repository: ', 'Academic resources including syllabi, books, and study materials are organized by department and semester for easy access.'),
    ('Mobile-Responsive Design: ', 'The interface adapts to different screen sizes, allowing access from smartphones and tablets.'),
    ('Secure Architecture: ', 'Prepared statements prevent SQL injection. Session-based authentication protects pages. Role-based access control limits unauthorized actions.'),
    ('File Management: ', 'Class routines, exam schedules, and academic resources can be uploaded as PDFs or images and displayed inline.'),
    ('Lost & Found Tracking: ', 'Digital tracking of Lost & Found items with category classification and claim status management.'),
]
for title, desc in advantages:
    p = doc.add_paragraph()
    run = p.add_run(title)
    run.bold = True
    run.font.size = Pt(12)
    run.font.name = 'Times New Roman'
    run2 = p.add_run(desc)
    run2.font.size = Pt(12)
    run2.font.name = 'Times New Roman'
    p.paragraph_format.space_after = Pt(4)

add_heading_custom('10.2 Limitations', level=2)
limitations = [
    'No email or SMS notification system \u2014 students are not automatically notified when attendance is marked or announcements are posted.',
    'Browser-based only \u2014 no companion mobile application, though the interface is mobile-responsive.',
    'No real-time updates \u2014 data requires a page refresh; no WebSocket or AJAX polling for live updates.',
    'Single institution scope \u2014 designed for ICON Commerce College only, not multi-campus ready.',
    'No fee management or payment processing functionality.',
    'No online examination or quiz module.',
    'Admin passwords are stored as plain text in the database (not hashed).',
]
for lim in limitations:
    add_bullet(lim)

# =================== CHAPTER 11: FUTURE ENHANCEMENTS ===================
add_page_break()
add_para('Chapter 11', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
add_para('FUTURE ENHANCEMENTS', bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=16)

enhancements = [
    'Email and SMS Notifications: Integrate PHPMailer or an SMS gateway to send automated alerts to students when attendance is marked, exams are scheduled, or announcements are posted.',
    'Password Hashing: Implement bcrypt password hashing for admin accounts using PHP\'s password_hash() and password_verify() functions.',
    'Mobile Application: Develop a companion Android/iOS app using React Native or Flutter with push notification support.',
    'Real-Time Updates: Implement AJAX polling or WebSocket communication to update dashboard data without page refresh.',
    'Graphical Analytics: Add Chart.js or similar for visual charts of attendance trends and department statistics.',
    'Online Examination Module: Add a quiz/exam system with automatic grading and result compilation.',
    'Fee Management: Integrate a fee payment module with payment gateway support and receipt generation.',
    'Multi-Campus Support: Extend the architecture to manage multiple college campuses from a single installation.',
    'Parent/Guardian Portal: Create a separate portal for parents to monitor their ward\'s attendance and academic progress.',
    'Two-Factor Authentication: Add OTP-based two-factor authentication for admin accounts.',
    'PDF Report Export: Add server-side PDF generation for attendance reports using a library like FPDF or TCPDF.',
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

# =================== CHAPTER 12: CONCLUSION ===================
add_page_break()
add_para('Chapter 12', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
add_para('CONCLUSION', bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=16)

add_body('ICC Companion was developed to address the need for an integrated, digital campus management platform at ICON Commerce College. The system successfully replaces fragmented manual processes with a unified web-based portal that serves both students and administrators.')

add_body('The project was implemented using PHP, MySQL, HTML5, CSS3, and JavaScript \u2014 all freely available technologies. The dual-portal architecture provides separate interfaces for students and administrators. The twelve-table relational database design supports all required functionalities including attendance tracking, exam scheduling, class routine management, announcement distribution, Lost & Found tracking, and academic resource management.')

add_body('From a security perspective, the system implements prepared statements for SQL injection prevention and session-based authentication for access control. The role-based admin system ensures that users only have access to functions appropriate for their role.')

add_body('The project fulfils the stated objectives and provides a practical solution for college campus management. It can be extended with future enhancements such as email notifications, mobile applications, and online examination modules.')

# =================== BIBLIOGRAPHY ===================
add_page_break()
add_para('BIBLIOGRAPHY', bold=True, size=18, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24)

refs = [
    'PHP Manual. PHP Documentation Group. Available at: https://www.php.net/manual/en/',
    'MySQL Reference Manual. Oracle Corporation. Available at: https://dev.mysql.com/doc/',
    'MDN Web Docs. Mozilla Developer Network. Available at: https://developer.mozilla.org/en-US/docs/Web/JavaScript',
    'W3Schools Online Web Tutorials. Available at: https://www.w3schools.com/',
    'Font Awesome Documentation. Fonticons, Inc. Available at: https://fontawesome.com/docs',
    'OWASP Foundation. Web Application Security Guide. Available at: https://owasp.org/',
]
for i, ref in enumerate(refs, 1):
    p = doc.add_paragraph()
    run = p.add_run(f'{i}. {ref}')
    run.font.size = Pt(12)
    run.font.name = 'Times New Roman'
    p.paragraph_format.space_after = Pt(6)

# Save
output_path = r'C:\xampp\htdocs\ICC_Companion\temp\ppt_and_report\my_report\PROJECT_REPORT.docx'
doc.save(output_path)
print(f'Report saved to: {output_path}')
