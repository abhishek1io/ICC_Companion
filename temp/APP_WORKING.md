# ICC Companion – Application Working Guide

> **College:** Icon Commerce College (ICC)  
> **Stack:** HTML + Vanilla CSS + JavaScript (Frontend) · PHP (Backend API) · MySQL (Database) · XAMPP (Local Server)

---

## 1. Overview

ICC Companion is a **college campus management portal** built as a multi-role web application. It serves two major user groups:

| Portal | Users | Access Method |
|--------|-------|---------------|
| **Student Portal** | Students | Roll Number + Date of Birth |
| **Admin Portal** | Faculty / Staff / Super-Admin (Principal) | Username + Password |

The app runs on **XAMPP (Apache + MySQL)** locally and can also be deployed on shared web hosting via the `hosting_import.sql` schema.

---

## 2. Architecture (Three-Tier)

```
┌──────────────────────────────────────┐
│          PRESENTATION LAYER          │
│  HTML Pages (admin/ & student/)      │
│  Vanilla CSS + JavaScript (Fetch API)│
└──────────────┬───────────────────────┘
               │ HTTP Requests (fetch/XMLHttpRequest)
               ▼
┌──────────────────────────────────────┐
│          BUSINESS LOGIC LAYER        │
│  PHP API Scripts (api/*.php)         │
│  Session Management + Role Guards    │
└──────────────┬───────────────────────┘
               │ MySQLi Prepared Statements
               ▼
┌──────────────────────────────────────┐
│           DATA LAYER                 │
│  MySQL Database: campus_portal       │
│  11 Tables (see DATABASE_SCHEMA.md)  │
└──────────────────────────────────────┘
```

All PHP API endpoints return **JSON responses** with the shape:
```json
{ "success": true/false, "message": "...", "data": [...] }
```

---

## 3. File / Directory Structure

```
ICC_Companion/
├── index.html              ← Public Landing Page (PWA-enabled)
├── admin-login.html        ← Admin login page
├── student-login.html      ← Student login page
│
├── admin/                  ← Admin Portal pages (11 pages)
│   ├── dashboard.html
│   ├── students.html
│   ├── attendance.html
│   ├── exams.html
│   ├── subjects.html
│   ├── departments.html
│   ├── announcements.html
│   ├── lost-found.html
│   ├── resources.html
│   ├── routines.html
│   └── staff.html          ← Super-Admin only: manage staff accounts
│
├── student/                ← Student Portal pages (8 pages)
│   ├── dashboard.html
│   ├── attendance.html
│   ├── exams.html
│   ├── subjects.html
│   ├── announcements.html
│   ├── lost-found.html
│   ├── resources.html
│   └── routines.html
│
├── api/                    ← 52 PHP backend scripts
│   ├── config.php          ← DB connection + helper functions
│   ├── admin-login.php
│   ├── student-login.php
│   └── [get/add/update/delete]-*.php
│
├── database/
│   ├── campus_portal.sql   ← Full schema + seed data (XAMPP)
│   └── hosting_import.sql  ← Clean schema for web hosting
│
└── uploads/                ← Uploaded files (PDFs, images)
    ├── resources/
    └── routines/
```

---

## 4. Authentication Flow

### 4.1 Student Login (`/api/student-login.php`)
1. Student submits **Roll Number** + **Date of Birth**
2. PHP queries `students` table by roll number
3. Compares the stored `dob` with the submitted value
4. On match → PHP session variables are set:
   - `$_SESSION['student_roll']`
   - `$_SESSION['student_name']`
   - `$_SESSION['student_dept']`
   - `$_SESSION['student_semester']`
5. JavaScript redirects to `student/dashboard.html`
6. All subsequent student API calls are protected by `checkStudentLogin()`

### 4.2 Admin Login (`/api/admin-login.php`)
1. Admin submits **Username** + **Password**
2. PHP queries `admins` table using a prepared statement
3. On match → session variables set:
   - `$_SESSION['admin_id']`
   - `$_SESSION['admin_name']`
   - `$_SESSION['admin_role']` ← determines access level
   - `$_SESSION['assigned_dept']` ← scope limiter for faculty
   - `$_SESSION['assigned_semester']` ← scope limiter for faculty
4. JavaScript reads `role` from response and stores it in `localStorage`
5. Redirects to `admin/dashboard.html`

---

## 5. Role-Based Access Control (RBAC)

Three roles are enforced across the system:

| Role | Who | Permissions |
|------|-----|-------------|
| `super-admin` | Principal / HOD | Full access to all departments, all semesters, can manage staff accounts |
| `staff` | Head of Department | Access to their assigned dept/semester |
| `faculty` | Teacher | Can only mark attendance & upload resources for **assigned subjects** |

### How Scope is Enforced (Backend)
`config.php` provides the `getAdminScope()` helper:
```php
function getAdminScope() {
    $role = $_SESSION['admin_role'];
    if ($role === 'super-admin') {
        return ['dept' => 'all', 'sem' => 'all'];   // Global access
    }
    return [
        'dept' => $_SESSION['assigned_dept'],
        'sem'  => $_SESSION['assigned_semester']
    ];
}
```

For **Faculty** role, the `save-attendance.php` additionally verifies subject ownership via the `faculty_subjects` table before allowing data mutation.

---

## 6. Core Features & How They Work

### 6.1 Attendance Management
- **Admin marks attendance:** Selects Department → Semester → Subject → Date
- The page fetches students via `get-students.php?dept=BCA&semester=5`
- Admin toggles Present/Absent for each student
- On Save → `save-attendance.php` is called with a JSON payload:
  ```json
  { "subject_id": 13, "date": "2026-01-08", "attendance": [
      { "roll_number": "UT-231-049-0001", "status": "present" },
      ...
  ]}
  ```
- The API **deletes the old record for that date+subject**, then inserts fresh rows (idempotent upsert pattern using transactions)
- **Student view:** Calls `get-attendance-summary.php` which returns per-subject stats (total classes, present count, percentage) computed from the `student_attendance_summary` VIEW

### 6.2 Exam Schedule Management
Two separate systems exist:
1. **Per-subject exam entries** (`exams` table) – admin adds date/time/room per subject
2. **Full-schedule PDF upload** (`exam_schedules` table) – admin uploads a single PDF for sessional/final; students download it

### 6.3 Resources Module
Supports **5 resource types:**

| Type | Storage |
|------|---------|
| `syllabus` | File upload (PDF) → `uploads/resources/` |
| `book` | File upload |
| `material` | File upload |
| `link` | External URL stored as text |
| `text` | Rich text stored in `content_text` column |

Upload is handled by `save-resource.php` which validates file extension, generates a unique filename (`res_{type}_{timestamp}_{rand}.ext`), moves the file, then inserts the DB record.

### 6.4 Lost & Found
- Both **students** and **admin** can post items (lost or found)
- Items have: title, description, category, item_type (lost/found), location, date, contact_info, image_url
- Admin can mark an item as **"Claimed"** by entering the claimant's roll number and date
- Students see only items relevant to the college community; admins manage the full list

### 6.5 Announcements
- Admin creates announcements with **priority** (high/medium/low) and targets them to a specific **department** and/or **semester** (or "all")
- Students see only announcements matching their own `dept_code` and `semester` (filtered server-side in `get-announcements.php`)
- Attachments (PDFs) can be linked via URL

### 6.6 Class Routines
- Admin uploads one PDF per Department+Semester combination
- Stored in `uploads/routines/`; the `class_routines` table holds the metadata
- Students filter by their own dept/sem and see a download button for the timetable PDF

### 6.7 Staff Management (Super-Admin Only)
- Accessible at `admin/staff.html`
- Super-admin can **Add / Edit / Delete** staff and faculty accounts
- When creating a faculty account, super-admin assigns a **department and semester** (scope restriction)
- Super-admin can also assign specific **subjects** to a faculty member via `save-faculty-subjects.php`

---

## 7. Frontend-Backend Communication

All frontend pages use the native **Fetch API** (no jQuery, no framework):
```javascript
// Example: Loading students
const res = await fetch(`../api/get-students.php?dept=BCA&semester=5`);
const json = await res.json();
if (json.success) {
    renderStudentList(json.data);
}
```

Session state is maintained via **PHP sessions** server-side. On the client, `localStorage` is used to cache the current user's name and role for display purposes only — all actual permission checks happen in PHP.

---

## 8. PWA (Progressive Web App)

The app includes a `manifest.json` linked from `index.html`, enabling "Add to Home Screen" on mobile devices. This makes ICC Companion installable like a native app without any app store.

---

## 9. Key Design Decisions

| Decision | Reason |
|----------|--------|
| No framework (vanilla JS + PHP) | Lightweight, runs on basic XAMPP/shared hosting |
| Roll Number + DOB login for students | No password management overhead; DOB acts as a secret |
| Transactions in attendance save | Prevents partial writes on network failure |
| Prepared statements throughout | Prevents SQL injection |
| Scope restriction via session | Prevents faculty from accessing other dept's data |
| File upload with random naming | Prevents filename collisions and direct URL guessing |

---

*Generated: 2026-04-28 | ICC Companion – Final Year Project*
