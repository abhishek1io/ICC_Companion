# ICC Companion – Database Schema Documentation

> **Database Name:** `campus_portal`  
> **Engine:** MySQL (InnoDB via XAMPP)  
> **Total Tables:** 11 (+ 1 VIEW)  
> **File:** `database/campus_portal.sql`

---

## Entity Relationship Overview

```
departments ──────────────────┐
     │ (dept_code PK)         │
     │                        │
     ├──► subjects ◄───────── ┤
     │       │ (subject_id)   │
     │       │                │
     │       ├──► attendance  │
     │       ├──► exams       │
     │       ├──► resources   │
     │       └──► faculty_subjects
     │
     ├──► students
     │       │ (roll_number)
     │       └──► attendance
     │
     └──► resources

admins ──► faculty_subjects ──► subjects
```

---

## Table Reference Index

| # | Table | Primary Key | Foreign Keys |
|---|-------|-------------|--------------|
| 1 | `departments` | `dept_id` | — |
| 2 | `subjects` | `subject_id` | `dept_code → departments` |
| 3 | `students` | `student_id` | `dept_code → departments` |
| 4 | `admins` | `admin_id` | — |
| 5 | `attendance` | `attendance_id` | `roll_number → students`, `subject_id → subjects` |
| 6 | `exams` | `exam_id` | `subject_id → subjects` |
| 7 | `lost_found` | `item_id` | — |
| 8 | `announcements` | `announcement_id` | — |
| 9 | `class_routines` | `routine_id` | — |
| 10 | `exam_schedules` | `schedule_id` | — |
| 11 | `resources` | `resource_id` | `dept_code → departments`, `subject_id → subjects` |
| 12 | `faculty_subjects` | `assignment_id` | `admin_id → admins`, `subject_id → subjects` |

---

## Table 1: `departments`

Stores the academic departments offered at ICC.

| Column | Type | Constraint | Description |
|--------|------|------------|-------------|
| `dept_id` | INT | **PK**, AUTO_INCREMENT | Surrogate key |
| `dept_code` | VARCHAR(10) | **UNIQUE**, NOT NULL | Natural key used as FK elsewhere (e.g. `BCA`, `BBA`) |
| `dept_name` | VARCHAR(100) | NOT NULL | Full name of department |

> **Note:** `dept_code` (not `dept_id`) is the FK used by `subjects`, `students`, and `resources` — a deliberate design choice for readability in queries.

**Seed Data:**
| dept_code | dept_name |
|-----------|-----------|
| BCA | Bachelor of Computer Applications |
| BBA | Bachelor of Business Administration |
| BA | Bachelor of Arts |
| BCOM | Bachelor of Commerce |

---

## Table 2: `subjects`

Stores individual course/subject offerings per department and semester.

| Column | Type | Constraint | Description |
|--------|------|------------|-------------|
| `subject_id` | INT | **PK**, AUTO_INCREMENT | Unique subject ID |
| `subject_code` | VARCHAR(20) | NOT NULL | E.g. `BCA501` |
| `subject_name` | VARCHAR(100) | NOT NULL | E.g. `Web Technologies` |
| `dept_code` | VARCHAR(10) | **FK → departments.dept_code** | Links to owning department |
| `semester` | INT | NOT NULL | Semester number (1–6) |

**Relationships:**
- `dept_code` → `departments.dept_code` (Many-to-One)
- Referenced by `attendance`, `exams`, `resources`, `faculty_subjects`

**Index of BCA Subjects (sample):**
| subject_code | subject_name | dept_code | semester |
|-------------|--------------|-----------|---------|
| BCA101 | Computer Fundamentals | BCA | 1 |
| BCA301 | Data Structures | BCA | 3 |
| BCA501 | Web Technologies | BCA | 5 |
| BCA601 | Project Work | BCA | 6 |

---

## Table 3: `students`

Stores enrolled student records. Used for authentication (roll + DOB).

| Column | Type | Constraint | Description |
|--------|------|------------|-------------|
| `student_id` | INT | **PK**, AUTO_INCREMENT | Internal ID |
| `roll_number` | VARCHAR(20) | **UNIQUE**, NOT NULL | Used as login credential & FK in attendance |
| `name` | VARCHAR(100) | NOT NULL | Student full name |
| `dob` | DATE | NOT NULL | Date of birth — **used as password** |
| `email` | VARCHAR(100) | NULL | Optional contact email |
| `phone` | VARCHAR(15) | NULL | Optional phone number |
| `dept_code` | VARCHAR(10) | **FK → departments.dept_code** | Department enrolled in |
| `semester` | INT | NOT NULL | Current semester |
| `created_at` | TIMESTAMP | DEFAULT NOW() | Registration timestamp |

**Roll Number Format:** `UT-{admission_year}-{dept_code_num}-{sequence}`  
Example: `UT-231-049-0001` = Year 2023, BCA dept (049), Student #1

**Relationships:**
- `dept_code` → `departments.dept_code`
- `roll_number` is referenced by `attendance.roll_number`

---

## Table 4: `admins`

Stores admin/faculty/staff accounts used for the Admin Portal.

| Column | Type | Constraint | Description |
|--------|------|------------|-------------|
| `admin_id` | INT | **PK**, AUTO_INCREMENT | Unique admin ID |
| `username` | VARCHAR(50) | **UNIQUE**, NOT NULL | Login username |
| `password` | VARCHAR(255) | NOT NULL | Plain-text password (should be hashed in production) |
| `name` | VARCHAR(100) | NOT NULL | Display name |
| `role` | VARCHAR(50) | DEFAULT `'admin'` | Role: `super-admin`, `staff`, `faculty` |
| `assigned_dept` | VARCHAR(10) | NULL | Department scope (e.g. `BCA`) or `all` |
| `assigned_semester` | VARCHAR(10) | NULL | Semester scope (e.g. `5`) or `all` |

**Role Permissions:**
| role | Dept Scope | Sem Scope | Can Manage Staff |
|------|-----------|-----------|-----------------|
| `super-admin` | ALL | ALL | ✅ Yes |
| `staff` | assigned_dept | assigned_sem | ❌ No |
| `faculty` | assigned subjects only | — | ❌ No |

**Relationships:**
- `admin_id` is referenced by `faculty_subjects.admin_id`

---

## Table 5: `attendance`

Records per-student, per-subject, per-date attendance. This is the most write-intensive table.

| Column | Type | Constraint | Description |
|--------|------|------------|-------------|
| `attendance_id` | INT | **PK**, AUTO_INCREMENT | Surrogate key |
| `roll_number` | VARCHAR(20) | **FK → students.roll_number** | Student identifier |
| `subject_id` | INT | **FK → subjects.subject_id** | Subject being attended |
| `attendance_date` | DATE | NOT NULL | Date of the class |
| `status` | ENUM(`present`,`absent`) | DEFAULT `present` | Attendance status |
| `marked_by` | VARCHAR(50) | NULL | Username of admin who marked it |
| `created_at` | TIMESTAMP | DEFAULT NOW() | When the record was inserted |

**Unique Constraint:**
```sql
UNIQUE KEY unique_attendance (roll_number, subject_id, attendance_date)
```
> Prevents duplicate attendance entries for the same student+subject+date combination.

**Relationships:**
- `roll_number` → `students.roll_number` (Many-to-One)
- `subject_id` → `subjects.subject_id` (Many-to-One)

**How it works:** When admin saves attendance, the API **deletes all rows** for that `subject_id + attendance_date` first, then re-inserts the full set — wrapped in a MySQL transaction for atomicity.

---

## Table 6: `exams`

Stores per-subject exam schedule entries (sessional and final).

| Column | Type | Constraint | Description |
|--------|------|------------|-------------|
| `exam_id` | INT | **PK**, AUTO_INCREMENT | Unique exam entry ID |
| `subject_id` | INT | **FK → subjects.subject_id** | Subject for this exam |
| `exam_date` | DATE | NOT NULL | Date of the exam |
| `start_time` | TIME | NOT NULL | Start time (e.g. `10:00:00`) |
| `end_time` | TIME | NOT NULL | End time (e.g. `13:00:00`) |
| `room` | VARCHAR(50) | NULL | Venue (e.g. `Hall A`, `Lab 101`) |
| `exam_type` | ENUM(`sessional`,`final`) | DEFAULT `final` | Type of exam |
| `attachment_url` | VARCHAR(255) | NULL | Optional PDF/image URL |
| `created_at` | TIMESTAMP | DEFAULT NOW() | Entry creation time |

**Relationships:**
- `subject_id` → `subjects.subject_id` (Many-to-One)

---

## Table 7: `lost_found`

Community lost-and-found board for the college campus.

| Column | Type | Constraint | Description |
|--------|------|------------|-------------|
| `item_id` | INT | **PK**, AUTO_INCREMENT | Unique item ID |
| `title` | VARCHAR(100) | NOT NULL | Short item title |
| `description` | TEXT | NULL | Detailed description |
| `category` | ENUM | DEFAULT `other` | `id-card`, `phone`, `wallet`, `books`, `electronics`, `other` |
| `item_type` | ENUM(`lost`,`found`) | NOT NULL | Whether the item was lost or found |
| `location` | VARCHAR(100) | NULL | Where it was lost/found |
| `item_date` | DATE | NULL | Date of loss/finding |
| `contact_info` | VARCHAR(100) | NULL | How to reach the poster |
| `image_url` | VARCHAR(255) | NULL | Optional photo of item |
| `status` | ENUM(`active`,`claimed`) | DEFAULT `active` | Current status |
| `posted_by` | VARCHAR(50) | NULL | Admin username or student roll number |
| `claimed_by` | VARCHAR(20) | NULL | Roll number of claimer |
| `claimed_date` | DATE | NULL | When it was claimed |
| `created_at` | TIMESTAMP | DEFAULT NOW() | Post creation time |

> **No FKs** — `posted_by` and `claimed_by` are stored as plain strings (usernames/roll numbers) for flexibility (both students and admins can post).

---

## Table 8: `announcements`

Targeted college-wide or department-specific notices.

| Column | Type | Constraint | Description |
|--------|------|------------|-------------|
| `announcement_id` | INT | **PK**, AUTO_INCREMENT | Unique notice ID |
| `title` | VARCHAR(200) | NOT NULL | Announcement heading |
| `description` | TEXT | NOT NULL | Full announcement body |
| `attachment_url` | VARCHAR(255) | NULL | Optional attachment URL |
| `link_url` | VARCHAR(255) | NULL | Optional external link |
| `priority` | ENUM(`high`,`medium`,`low`) | DEFAULT `medium` | Display priority |
| `target_dept` | VARCHAR(50) | DEFAULT `all` | Target department code or `all` |
| `target_semester` | VARCHAR(20) | DEFAULT `all` | Target semester or `all` |
| `posted_by` | VARCHAR(50) | NULL | Admin username who posted |
| `created_at` | TIMESTAMP | DEFAULT NOW() | Post timestamp |

**Filtering Logic:** `get-announcements.php` filters announcements where `target_dept = 'all' OR target_dept = {student_dept}` AND `target_semester = 'all' OR target_semester = {student_semester}`.

---

## Table 9: `class_routines`

Stores uploaded class timetable PDFs (one per dept+semester).

| Column | Type | Constraint | Description |
|--------|------|------------|-------------|
| `routine_id` | INT | **PK**, AUTO_INCREMENT | Unique routine ID |
| `title` | VARCHAR(200) | NOT NULL | Display title |
| `file_url` | VARCHAR(255) | NOT NULL | Path to uploaded PDF (e.g. `uploads/routines/bca_sem5.pdf`) |
| `dept_code` | VARCHAR(10) | NOT NULL | Department this routine is for |
| `semester` | VARCHAR(10) | NOT NULL | Semester this routine covers |
| `created_at` | TIMESTAMP | DEFAULT NOW() | Upload timestamp |

> No foreign key on `dept_code` here — kept loose for flexibility.

---

## Table 10: `exam_schedules`

Stores the master exam schedule PDFs (one per type).

| Column | Type | Constraint | Description |
|--------|------|------------|-------------|
| `schedule_id` | INT | **PK**, AUTO_INCREMENT | Unique ID |
| `schedule_type` | ENUM(`sessional`,`final`) | **UNIQUE**, NOT NULL | Only one PDF per type |
| `file_url` | VARCHAR(255) | NOT NULL | Path to uploaded PDF |
| `created_at` | TIMESTAMP | DEFAULT NOW() | Upload timestamp |

> The `UNIQUE` on `schedule_type` ensures at most one sessional PDF and one final PDF exist at any time.

---

## Table 11: `resources`

Multi-type academic resource library (syllabus, books, links, notes, text).

| Column | Type | Constraint | Description |
|--------|------|------------|-------------|
| `resource_id` | INT | **PK**, AUTO_INCREMENT | Unique resource ID |
| `title` | VARCHAR(200) | NOT NULL | Resource title |
| `description` | TEXT | NULL | Optional summary |
| `resource_type` | ENUM | NOT NULL | `syllabus`, `book`, `material`, `link`, `text`, `others` |
| `file_url` | VARCHAR(255) | NULL | Path if file was uploaded |
| `link_url` | TEXT | NULL | External URL (for type=link) |
| `content_text` | TEXT | NULL | Rich text content (for type=text) |
| `dept_code` | VARCHAR(10) | **FK → departments.dept_code** | Target department |
| `semester` | VARCHAR(10) | NOT NULL | Target semester |
| `subject_id` | INT | **FK → subjects.subject_id** (nullable) | Optional subject association |
| `posted_by` | VARCHAR(50) | NULL | Admin username |
| `created_at` | TIMESTAMP | DEFAULT NOW() | Upload timestamp |

**Relationships:**
- `dept_code` → `departments.dept_code`
- `subject_id` → `subjects.subject_id` (nullable — resource can be general, not tied to a subject)

---

## Table 12: `faculty_subjects` *(implicit — not in initial SQL)*

Links admin/faculty accounts to the specific subjects they are authorized to teach.

| Column | Type | Constraint | Description |
|--------|------|------------|-------------|
| `assignment_id` | INT | **PK**, AUTO_INCREMENT | Unique assignment ID |
| `admin_id` | INT | **FK → admins.admin_id** | The faculty member |
| `subject_id` | INT | **FK → subjects.subject_id** | The assigned subject |

**Purpose:** Enforces fine-grained access control. A `faculty` role admin can only mark attendance and upload resources for subjects listed in their `faculty_subjects` rows. This check is enforced in `save-attendance.php` and `get-resources.php` on every request.

---

## View: `student_attendance_summary`

A pre-computed view that aggregates attendance data for the student portal.

```sql
CREATE VIEW student_attendance_summary AS
SELECT
    s.roll_number,
    s.name,
    s.dept_code,
    s.semester,
    sub.subject_name,
    sub.subject_id,
    COUNT(a.attendance_id)                                           AS total_classes,
    SUM(CASE WHEN a.status = 'present' THEN 1 ELSE 0 END)           AS present_count,
    ROUND(
        (SUM(CASE WHEN a.status = 'present' THEN 1 ELSE 0 END)
         / COUNT(a.attendance_id)) * 100, 1
    )                                                                AS percentage
FROM students s
JOIN subjects sub ON s.dept_code = sub.dept_code AND s.semester = sub.semester
LEFT JOIN attendance a ON s.roll_number = a.roll_number AND sub.subject_id = a.subject_id
GROUP BY s.roll_number, s.name, s.dept_code, s.semester, sub.subject_name, sub.subject_id;
```

**Output per row:** One row per student per subject, showing their attendance percentage. Used in the Student Portal's attendance page.

---

## Foreign Key Relationship Map

```
departments.dept_code (PK/UNIQUE)
    ◄── subjects.dept_code
    ◄── students.dept_code
    ◄── resources.dept_code

subjects.subject_id (PK)
    ◄── attendance.subject_id
    ◄── exams.subject_id
    ◄── resources.subject_id (nullable)
    ◄── faculty_subjects.subject_id

students.roll_number (UNIQUE)
    ◄── attendance.roll_number

admins.admin_id (PK)
    ◄── faculty_subjects.admin_id
```

---

## Unique Constraints Summary

| Table | Unique Key | Purpose |
|-------|-----------|---------|
| `departments` | `dept_code` | Prevents duplicate department codes |
| `subjects` | *(none explicit)* | Relies on PK |
| `students` | `roll_number` | Each student has one roll number |
| `admins` | `username` | Prevents duplicate logins |
| `attendance` | `(roll_number, subject_id, attendance_date)` | One record per student/subject/date |
| `exam_schedules` | `schedule_type` | Max one PDF per exam type |

---

*Generated: 2026-04-28 | ICC Companion – Final Year Project*
