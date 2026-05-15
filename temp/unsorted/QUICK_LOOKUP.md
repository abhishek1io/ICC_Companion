# ICC Companion – Quick Lookup Cheatsheet

---

## 🔐 Login Credentials
| Portal | Field 1 | Field 2 |
|--------|---------|---------|
| Student | Roll Number | Date of Birth |
| Admin | Username | Password |

**Default Accounts:**
| Username | Password | Role |
|----------|----------|------|
| `admin` | `admin123` | super-admin |
| `staff` | `staff123` | staff |

---

## 👥 Roles
| Role | Scope |
|------|-------|
| `super-admin` | All depts, all sems, manage staff |
| `staff` | Assigned dept + semester |
| `faculty` | Assigned subjects only |

---

## 🗄️ Tables at a Glance
| Table | PK | Key FKs |
|-------|----|---------|
| `departments` | `dept_id` | — |
| `subjects` | `subject_id` | `dept_code` |
| `students` | `student_id` | `dept_code` |
| `admins` | `admin_id` | — |
| `attendance` | `attendance_id` | `roll_number`, `subject_id` |
| `exams` | `exam_id` | `subject_id` |
| `lost_found` | `item_id` | — |
| `announcements` | `announcement_id` | — |
| `class_routines` | `routine_id` | — |
| `exam_schedules` | `schedule_id` | — |
| `resources` | `resource_id` | `dept_code`, `subject_id` |
| `faculty_subjects` | `assignment_id` | `admin_id`, `subject_id` |

---

## 🔑 Key Unique Constraints
| Table | Unique Column(s) |
|-------|-----------------|
| `departments` | `dept_code` |
| `students` | `roll_number` |
| `admins` | `username` |
| `attendance` | `(roll_number, subject_id, attendance_date)` |
| `exam_schedules` | `schedule_type` |

---

## 📡 API Pattern
```
GET  api/get-{resource}.php?param=value  → fetch data
POST api/add-{resource}.php              → insert
POST api/update-{resource}.php           → update
POST api/delete-{resource}.php           → delete
```
All responses: `{ "success": bool, "message": "...", "data": [...] }`

---

## 📁 Departments
`BCA` · `BBA` · `BA` · `BCOM` — Semesters 1–6

---

## 📂 Upload Paths
| Type | Path |
|------|------|
| Resources | `uploads/resources/` |
| Routines | `uploads/routines/` |

---

## 🗂️ Resource Types
`syllabus` · `book` · `material` · `link` · `text` · `others`

---

## ⚡ Attendance Save Flow
1. Admin selects Dept → Sem → Subject → Date
2. POST to `save-attendance.php` with JSON array
3. API deletes old rows for that date+subject (transaction)
4. Inserts fresh rows → commits

---

## 🖥️ Tech Stack
`HTML` + `Vanilla JS` + `Vanilla CSS` → `PHP` (MySQLi) → `MySQL` (XAMPP)
