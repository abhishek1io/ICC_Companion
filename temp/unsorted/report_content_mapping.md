# ICC Companion Report — Content Mapping Guide

> **Reference:** `temp/ppt_and_report/report_reference/refrence_sajeeb.docx` (College Complaint Management System by Sajib Biswas)  
> **Target:** `ICC_Companion` — Campus Portal for ICON Commerce College  
> **Purpose:** Map reference doc structure → actual codebase content with table/image/diagram replacements

---

## Chapter 1: INTRODUCTION

### Replace "Complaint Management" → "Campus Portal (ICC Companion)"

**1.1 Background** — Replace with:
> The ICC Companion is a comprehensive campus management portal developed for ICON Commerce College, Guwahati. It digitizes academic administration — subject management, attendance tracking, exam scheduling, class routines, resource sharing, announcements, and lost & found services. Previously, these functions were handled through manual registers, notice boards, and word-of-mouth. The portal provides a centralized, role-based digital platform.

**1.2 Problem Statement** — Replace problems with campus-relevant issues:
- Attendance records maintained on paper registers — easily lost, no real-time visibility
- Exam timetables posted on physical notice boards — students miss updates
- Academic resources (syllabi, notes) distributed via email — no central repository
- Lost & found items managed informally — no structured claim process
- No single dashboard for administrators to monitor campus operations

**1.3 Proposed Solution** — Replace with:
> ICC Companion is a web-based application using PHP + MySQL (REST API) + HTML/CSS/JS frontend. Three-tier architecture: Student Portal (8 features), Admin Portal (11 management modules), Role-Based Access (Faculty/HOD/Principal). All data stored in MySQL with 12 relational tables.

---

## Chapter 2: REQUIREMENT SPECIFICATION

### 2.1 Hardware Requirements — Table Replacement

Replace refrence_sajeeb.docx table with:

| Component | Minimum Requirement |
|-----------|-------------------|
| Server | Intel Core i3 / 8 GB RAM / 256 GB SSD |
| Client | Any device with a web browser (smartphone, tablet, desktop) |
| Network | Standard LAN / Wi-Fi (no internet required for local deployment) |
| Operating System | Windows 10+ / Linux / macOS (server); Any OS (client) |
| Software | XAMPP 8.x / WAMP 3.x (Apache + PHP 8.x + MySQL 8.x) |

### 2.2 Technologies Used — Table Replacement

Replace refrence_sajeeb.docx table with:

| Technology | Version | Purpose |
|-----------|---------|---------|
| HTML5 | — | Structure of 21+ web pages |
| CSS3 | — | Responsive styling (741 lines) |
| JavaScript | ES6 | Client-side logic, dynamic interactions (362 lines) |
| PHP | 8.x | REST API backend (39 API endpoints) |
| MySQL | 8.x | Relational database (12 tables) |
| Apache | 2.4+ | Web server (via XAMPP/WAMP) |
| Font Awesome | 6.x | UI icons (loaded via CDN) |
| Google Fonts | Outfit | Typography |

---

## Chapter 3: OBJECT OF THE PROJECT

Replace objectives with ICC Companion focus:

1. Provide students with a single dashboard to access subjects, attendance, resources, exams, routines, announcements, and lost & found.
2. Enable attendance marking via checkbox interface with per-subject tracking and minimum-attendance alerts (75% threshold).
3. Centralize exam timetable and class routine files for each department and semester.
4. Allow sharing of academic resources (syllabi, notes, books, links) by type, department, and semester.
5. Implement role-based admin access: Faculty (limited), HOD (department scope), Principal (full scope).
6. Manage lost & found items with photo upload, category tagging, and claim workflow.
7. Post announcements with priority levels, target filtering, and file/link attachments.
8. Ensure security through session-based authentication and SQL injection prevention.

---

## Chapter 4: SCOPE OF THE PROJECT

### 4.1 In Scope
- Student authentication via Roll Number + Date of Birth
- Subject listing by department + semester
- Academic resource library (syllabus/book/material/link/text)
- Per-subject attendance tracking with progress bars and color-coded alerts
- Exam timetable management and schedule file uploads
- Class routine file management
- Lost & found item posting, browsing, and claiming
- Announcement system with priority levels and targeting
- 3-tier admin roles: Faculty, HOD, Principal
- Department management (super-admin)
- Faculty management with subject assignments

### 4.2 Out of Scope
- Fee management / payment system
- Student registration (admin-created only)
- Online class / video conferencing
- Messaging / chat between students and faculty
- Grade / mark management
- Library book issuing system
- Real-time attendance (QR/biometric integration)
- Mobile app (browser-based only)

---

## Chapter 5: SYSTEM ANALYSIS

### 5.1 Existing System
Replace with:
> At ICON Commerce College, academic management was handled through physical registers (attendance), notice boards (timetables, announcements), paper forms (lost & found), and email/WhatsApp (resource sharing). No centralized digital platform existed.

### 5.2 Proposed System
Replace with the ICC Companion portal features — digital attendance tracking, online exam schedules, centralized resource library, structured lost & found workflow, targeted announcements, role-based admin access.

### 5.3 Feasibility Study
- **Technical:** Built on XAMPP stack (PHP + MySQL + Apache) — no proprietary software needed
- **Economic:** All technologies open-source; runs on existing college server infrastructure
- **Operational:** Clean UI — students need basic browser skills; admins need no technical training

---

## Chapter 6: SYSTEM DESIGN

### Diagrams to Insert (from `temp/ppt_and_report/my_report/Diagram/`)

| Figure | File | Path |
|--------|------|------|
| 6.1 System Architecture Diagram | `system_architecture.png` | `temp/ppt_and_report/my_report/Diagram/system_architecture.png` |
| 6.2 DFD Level 0 (Context Diagram) | `dfd_level0.png` | `temp/ppt_and_report/my_report/Diagram/dfd_level0.png` |
| 6.3 DFD Level 1 (Detailed Process Flow) | `dfd_level1.png` | `temp/ppt_and_report/my_report/Diagram/dfd_level1.png` |
| 6.4 Use Case Diagram | `use_case_diagram.png` | `temp/ppt_and_report/my_report/Diagram/use_case_diagram.png` |
| 6.5 Entity-Relationship (ER) Diagram | `er_diagram.png` | `temp/ppt_and_report/my_report/Diagram/er_diagram.png` |

These diagrams already exist in the `temp/ppt_and_report/my_report/Diagram/` directory.

---

## Chapter 7: DATABASE DESIGN

### Database: `campus_portal` — 12 Tables

#### Table: `departments`
| Column | Type | Constraints |
|--------|------|-------------|
| dept_id | INT | PRIMARY KEY, AUTO_INCREMENT |
| dept_code | VARCHAR(20) | UNIQUE, NOT NULL |
| dept_name | VARCHAR(100) | NOT NULL |
| max_semesters | INT | NOT NULL |

#### Table: `subjects`
| Column | Type | Constraints |
|--------|------|-------------|
| subject_id | INT | PRIMARY KEY, AUTO_INCREMENT |
| subject_code | VARCHAR(20) | NOT NULL |
| subject_name | VARCHAR(100) | NOT NULL |
| dept_code | VARCHAR(20) | FOREIGN KEY → departments |
| semester | INT | NOT NULL |

#### Table: `students`
| Column | Type | Constraints |
|--------|------|-------------|
| student_id | INT | PRIMARY KEY, AUTO_INCREMENT |
| roll_number | VARCHAR(50) | UNIQUE, NOT NULL |
| name | VARCHAR(100) | NOT NULL |
| dob | DATE | NOT NULL |
| email | VARCHAR(100) | — |
| phone | VARCHAR(20) | — |
| dept_code | VARCHAR(20) | FOREIGN KEY → departments |
| semester | INT | NOT NULL |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |

#### Table: `admins`
| Column | Type | Constraints |
|--------|------|-------------|
| admin_id | INT | PRIMARY KEY, AUTO_INCREMENT |
| username | VARCHAR(50) | UNIQUE, NOT NULL |
| password | VARCHAR(255) | NOT NULL (hashed) |
| name | VARCHAR(100) | NOT NULL |
| role | ENUM('faculty','hod','principal') | NOT NULL |
| assigned_dept | VARCHAR(20) | FOREIGN KEY → departments |
| assigned_semester | INT | — |

#### Table: `attendance`
| Column | Type | Constraints |
|--------|------|-------------|
| attendance_id | INT | PRIMARY KEY, AUTO_INCREMENT |
| roll_number | VARCHAR(50) | FOREIGN KEY → students |
| subject_id | INT | FOREIGN KEY → subjects |
| attendance_date | DATE | NOT NULL |
| status | ENUM('present','absent') | NOT NULL |
| marked_by | INT | FOREIGN KEY → admins |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |
| UNIQUE(roll_number, subject_id, attendance_date) | | |

#### Table: `exams`
| Column | Type | Constraints |
|--------|------|-------------|
| exam_id | INT | PRIMARY KEY, AUTO_INCREMENT |
| subject_id | INT | FOREIGN KEY → subjects |
| exam_date | DATE | NOT NULL |
| start_time | TIME | NOT NULL |
| end_time | TIME | NOT NULL |
| room | VARCHAR(50) | — |
| exam_type | ENUM('sessional','final') | NOT NULL |

#### Table: `class_routines`
| Column | Type | Constraints |
|--------|------|-------------|
| routine_id | INT | PRIMARY KEY, AUTO_INCREMENT |
| title | VARCHAR(200) | NOT NULL |
| file_url | VARCHAR(500) | NOT NULL |
| dept_code | VARCHAR(20) | FOREIGN KEY → departments |
| semester | INT | NOT NULL |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |

#### Table: `exam_schedules`
| Column | Type | Constraints |
|--------|------|-------------|
| schedule_id | INT | PRIMARY KEY, AUTO_INCREMENT |
| schedule_type | ENUM('sessional','final') | UNIQUE |
| file_url | VARCHAR(500) | NOT NULL |
| dept_code | VARCHAR(20) | FOREIGN KEY → departments |
| semester | INT | NOT NULL |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |

#### Table: `resources`
| Column | Type | Constraints |
|--------|------|-------------|
| resource_id | INT | PRIMARY KEY, AUTO_INCREMENT |
| title | VARCHAR(200) | NOT NULL |
| description | TEXT | — |
| resource_type | ENUM('syllabus','book','material','link','text','others') | NOT NULL |
| file_url | VARCHAR(500) | — |
| link_url | VARCHAR(500) | — |
| content_text | TEXT | — |
| dept_code | VARCHAR(20) | FOREIGN KEY → departments |
| semester | INT | — |
| subject_id | INT | FOREIGN KEY → subjects |
| posted_by | INT | FOREIGN KEY → admins |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |

#### Table: `lost_found`
| Column | Type | Constraints |
|--------|------|-------------|
| item_id | INT | PRIMARY KEY, AUTO_INCREMENT |
| title | VARCHAR(200) | NOT NULL |
| description | TEXT | NOT NULL |
| category | ENUM('id-card','phone','wallet','books','electronics','other') | NOT NULL |
| item_type | ENUM('lost','found') | NOT NULL |
| location | VARCHAR(200) | — |
| item_date | DATE | — |
| contact_info | VARCHAR(200) | — |
| image_url | VARCHAR(500) | — |
| status | ENUM('active','claimed') | DEFAULT 'active' |
| posted_by | INT | FOREIGN KEY → admins |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |

#### Table: `announcements`
| Column | Type | Constraints |
|--------|------|-------------|
| announcement_id | INT | PRIMARY KEY, AUTO_INCREMENT |
| title | VARCHAR(200) | NOT NULL |
| description | TEXT | NOT NULL |
| attachment_url | VARCHAR(500) | — |
| link_url | VARCHAR(500) | — |
| priority | ENUM('high','medium','low') | DEFAULT 'medium' |
| target_dept | VARCHAR(20) | FOREIGN KEY → departments |
| target_semester | INT | — |
| posted_by | INT | FOREIGN KEY → admins |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |

#### Table: `faculty_subjects`
| Column | Type | Constraints |
|--------|------|-------------|
| faculty_id | INT | FOREIGN KEY → admins |
| subject_id | INT | FOREIGN KEY → subjects |
| PRIMARY KEY(faculty_id, subject_id) | | |

---

## Chapter 8: IMPLEMENTATION / WORKING

Replace all complaint-management descriptions with ICC Companion workflows:

### 8.1 Home Page (`index.html`)
Landing page with hero section, feature cards (8 features), links to Student Login and Admin Login.

### 8.2 Student Login (`student-login.html`)
Student enters Roll Number and Date of Birth. POST to `api/student-login.php`. Session stored in sessionStorage. Redirects to `student/dashboard.html`.

### 8.3 Admin Login (`admin-login.html`)
Three tabs: Faculty, HOD, Principal. Login type stored in hidden field. POST to `api/admin-login.php`. Role-based session created.

### 8.4 Student Dashboard (`student/dashboard.html`)
Welcome card with student info. Stats: Overall Attendance %, Upcoming Exams, Announcements. Quick Access menu (7 cards). Latest announcements feed.

### 8.5 Student: Subjects (`student/subjects.html`)
Displays subjects for student's department + semester. Fetched from `get-subjects.php`.

### 8.6 Student: Resources (`student/resources.html`)
Search + filter by type. Resource cards with download/view options. File, link, and text content types supported.

### 8.7 Student: Attendance (`student/attendance.html`)
Overall attendance % card. Subject-wise cards with progress bars. Color-coded: green (≥75%), orange (≥65% warning), red (<65% shortage). "Can miss X more" indicator.

### 8.8 Student: Exams (`student/exams.html`)
Sessional (yellow) and Final (red) sections. Schedule file display (images inline, PDF embed). Exam list with date, time, room. Days remaining countdown.

### 8.9 Student: Routines (`student/routines.html`)
Latest class routine file for dept+sem. Images inline, PDF via iframe, others as download links.

### 8.10 Student: Lost & Found (`student/lost-found.html`)
Filter by type (Lost/Found) and category. Item cards with image, title, location, date, description, contact info. Red/green type badges.

### 8.11 Student: Announcements (`student/announcements.html`)
Full announcement list with priority badges (high/medium/low). Target dept/sem filtering. Attachment and external link support.

### 8.12 Admin Dashboard (`admin/dashboard.html`)
Welcome banner with role badge. Stats: Students, Exams, Lost/Found, Announcements. Quick Actions menu. Students by Department breakdown.

### 8.13 Admin: Staff Management (`admin/staff.html`)
Super-admin only. Staff table with roles and assignments. Add/Edit modal. Subject assignment with checkboxes.

### 8.14 Admin: Departments (`admin/departments.html`)
Super-admin only. CRUD for departments (code, name, max semesters).

### 8.15 Admin: Students (`admin/students.html`)
Student table with filters and search. Add/Edit modal. Faculty role has read-only access.

### 8.16 Admin: Subjects (`admin/subjects.html`)
Subject CRUD with dept/sem filters.

### 8.17 Admin: Resources (`admin/resources.html`)
Resource CRUD with dept/sem/type filters. File upload, link input, text content.

### 8.18 Admin: Attendance (`admin/attendance.html`)
Two tabs: Mark Attendance (checkbox list per subject/date), View Records (student-wise summary with progress bars, monthly filters).

### 8.19 Admin: Exams (`admin/exams.html`)
Sessional + Final sections. Schedule file upload per dept/sem. Exam CRUD with date, time, room.

### 8.20 Admin: Routines (`admin/routines.html`)
Routine CRUD with file upload (PDF/Image) per dept/sem.

### 8.21 Admin: Lost & Found (`admin/lost-found.html`)
Item CRUD with image upload, category tagging. "Mark Claimed" workflow.

### 8.22 Admin: Announcements (`admin/announcements.html`)
Announcement CRUD with priority, targeting, file/link attachments.

### 8.23 Security Implementation
- Session-based authentication (sessionStorage + PHP session checks)
- Role-based access control (3-tier: faculty/HOD/principal)
- SQL injection prevention via prepared statements (mysqli)
- Password hashing for admin accounts
- Input sanitization on all API endpoints

---

## Chapter 9: SAMPLE SCREENSHOTS

Screenshots located at: `temp/ppt_and_report/my_report/screenshots/`

| Section | Screenshot File |
|---------|----------------|
| Home Page | `screenshot_home.png` |
| Student Login | `screenshot_student_login.png` |
| Student Dashboard | `screenshot_student_dashboard.png` |
| Student: Resources | `screenshot_resources.png` |
| Student: Attendance | `screenshot_attendance.png` |
| Student: Exams | `screenshot_exams.png` |
| Student: Lost & Found | `screenshot_lost_found.png` |
| Student: Announcements | `screenshot_announcements.png` |
| **Admin Login** | `screenshot_admin_login.png` |
| **Admin Dashboard** | `screenshot_admin_dashboard.png` |
| **Admin: Manage Faculty** | `screenshot_manage_faculty.png` |
| **Admin: Manage Departments** | `screenshot_manage_departments.png` |
| **Admin: Manage Students** | `screenshot_manage_students.png` |
| **Admin: Manage Subjects** | `screenshot_subjects.png` |
| **Admin: Manage Resources** | `screenshot_manage_resources.png` |
| **Admin: Manage Attendance** | `screenshot_manage_attendance.png` |
| **Admin: Manage Exams** | `screenshot_manage_exams.png` |
| **Admin: Manage Routines** | `screenshot_manage_routines.png` |
| **Admin: Manage Lost & Found** | `screenshot_manage_lost_found.png` |
| **Admin: Manage Announcements** | `screenshot_manage_announcements.png` |

Place screenshots at labeled locations in Chapter 9 page breaks. Update captions to match ICC Companion page names.

---

## Chapter 10: ADVANTAGES AND LIMITATIONS

### Advantages
- Centralized campus management across all departments and semesters
- Real-time attendance tracking with visual progress indicators
- Organized resource library with multiple content types
- Structured lost & found system with claim workflow
- Targeted announcements with priority levels
- Role-based admin access ensures data security
- All data stored in relational MySQL database with foreign key integrity
- Responsive design works on mobile and desktop browsers

### Limitations
- No student self-registration — admins must create accounts
- Attendance requires manual marking (no QR/biometric integration)
- No real-time attendance push — student must refresh to see updates
- No fee/payment module
- No parent/guardian access portal
- No automated email/SMS notifications
- No grade/marks management
- Single institution — not designed for multi-college deployment

---

## Chapter 11: FUTURE ENHANCEMENTS

1. **Self-Registration Portal** — Allow students to register online with document verification
2. **QR Code Attendance** — Integrate QR scanning for faster attendance marking
3. **Fee Management Module** — Add online fee payment, due tracking, receipt generation
4. **Grade/Marks Management** — Faculty can upload marks, students view grade cards
5. **Parent Portal** — Guardian login to monitor attendance and performance
6. **Email/SMS Notifications** — Auto-alerts for attendance shortage, exam dates, announcements
7. **Real-Time Dashboard Updates** — AJAX polling for live attendance and announcement feeds
8. **Mobile App** — Companion app for Android/iOS with push notifications
9. **Multi-College Support** — Super-admin panel to manage multiple institutions
10. **Analytics Dashboard** — Charts for attendance trends, exam performance, lost & found patterns

---

## Chapter 12: CONCLUSION

Replace with:
> The ICC Companion campus portal was developed to digitize academic administration at ICON Commerce College, Guwahati. Built with PHP, MySQL, HTML5, CSS3, and JavaScript, the system serves students (8 self-service features), faculty (attendance marking, resource sharing), HODs (department oversight), and principals (full administrative control). All 12 database tables are in 3NF with foreign key relationships. The project fulfills all stated objectives and provides a practical platform that can be extended with future enhancements.

## REFERENCE

Replace references with:
1. PHP Manual — https://www.php.net/manual/en/
2. MySQL Reference Manual — https://dev.mysql.com/doc/refman/8.0/en/
3. W3Schools HTML/CSS/JS Tutorials — https://www.w3schools.com/
4. MDN Web Docs — https://developer.mozilla.org/
5. Font Awesome Documentation — https://fontawesome.com/docs
6. OWASP Web Security Guide — https://owasp.org/
7. PHP: The Right Way — https://phptherightway.com/
8. Silberschatz, A., Korth, H.F., & Sudarshan, S. — Database System Concepts, 7th Ed.

---

## Summary: What to Replace Where

| Reference Doc Section | Replace With | File/Tables/Diagrams |
|----------------------|-------------|---------------------|
| Chap 1: Complaint Management | ICC Companion Campus Portal | — |
| Chap 2.1: Hardware Table | Updated hardware spec table | Replace tbl[3] |
| Chap 2.2: Technologies Table | ICC tech stack table | Replace tbl[4] |
| Chap 3: Complaint Objectives | ICC Companion objectives | — |
| Chap 4: Complaint Scope | ICC Companion scope | — |
| Chap 5: Existing/Proposed System | ICC campus workflow | — |
| Chap 6: Diagrams | ICC Companion diagrams | Use `Diagram/system_architecture.png`, `dfd_level0.png`, `dfd_level1.png`, `use_case_diagram.png`, `er_diagram.png` |
| Chap 7: Database Tables 1-5 | 12 tables (campus_portal DB) | Replace tbl[5] through tbl[9] |
| Chap 8: Complaint Implementation | 22 ICC Companion workflows | — |
| Chap 9: Screenshots | 19 ICC Companion screenshots | Use `screenshots/*.png` |
| Chap 10: Complaint Advantages | ICC Companion advantages | — |
| Chap 11: Complaint Future | ICC Companion future plans | — |
| Chap 12: Complaint Conclusion | ICC Companion conclusion | — |

**Diagrams location:** `temp/ppt_and_report/my_report/Diagram/` (5 files)  
**Screenshots location:** `temp/ppt_and_report/my_report/screenshots/` (19+ files)  
**Database SQL:** `database/campus_portal.sql` (12 tables, view, sample data)  
**Source code:** Root (`api/`, `admin/`, `student/`, `js/`, `css/` directories)
