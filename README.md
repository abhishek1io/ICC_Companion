# ICC Companion - ICON COMMERCE COLLEGE
## Setup Guide for XAMPP

---

## 📋 What You Need

1. **XAMPP** - Download from: https://www.apachefriends.org/
2. **Web Browser** - Chrome, Firefox, or Edge

---

## 🚀 Step-by-Step Setup Instructions

### Step 1: Install XAMPP

1. Download XAMPP from the official website
2. Run the installer
3. Install with default settings (Apache + MySQL + PHP)
4. Installation folder: `C:\xampp`

---

### Step 2: Copy Project Files

1. Copy the entire `campus-portal` folder
2. Paste it inside: `C:\xampp\htdocs\`
3. Your folder structure should be:
   ```
   C:\xampp\htdocs\campus-portal\
   ├── index.html
   ├── student-login.html
   ├── admin-login.html
   ├── css\
   ├── js\
   ├── api\
   ├── student\
   ├── admin\
   └── database\
   ```

---

### Step 3: Start XAMPP

1. Open **XAMPP Control Panel**
2. Click **Start** next to **Apache** (for web server)
3. Click **Start** next to **MySQL** (for database)
4. Both should show "Running" in green

---

### Step 4: Create Database

1. Open your browser
2. Go to: `http://localhost/phpmyadmin`
3. Click on **"Import"** tab at the top
4. Click **"Choose File"** button
5. Select: `campus-portal/database/campus_portal.sql`
6. Click **"Go"** button at the bottom

**If successful, you'll see:**
- A new database called `campus_portal`
- Tables like: students, admins, attendance, exams, etc.

---

### Step 5: Test the Application

1. Open browser
2. Go to: `http://localhost/campus-portal`
3. You should see the ICC Companion home page!

---

## 🔐 Login Credentials

### Student Login
| Roll Number | Date of Birth |
|-------------|---------------|
| BCA23001    | 2004-05-15    |
| BCA23002    | 2004-08-22    |
| BBA23001    | 2004-04-25    |
| BCOM23001   | 2004-09-12    |

### Admin Login
| Username | Password |
|----------|----------|
| admin    | admin123 |
| staff    | staff123 |

---

## 📁 Project Structure

```
campus-portal/
│
├── index.html              ← Home page (choose login type)
├── student-login.html      ← Student login
├── admin-login.html        ← Admin login
│
├── student/                ← Student pages (view only)
│   ├── dashboard.html      ← Student home
│   ├── attendance.html     ← View attendance
│   ├── exams.html          ← Exam timetable
│   ├── lost-found.html     ← Browse lost & found
│   └── announcements.html  ← View notices
│
├── admin/                  ← Admin pages (full control)
│   ├── dashboard.html      ← Admin home
│   ├── students.html       ← Add/Edit/Delete students
│   ├── attendance.html     ← Mark attendance
│   ├── exams.html          ← Manage exams
│   ├── lost-found.html     ← Manage lost & found
│   └── announcements.html  ← Post announcements
│
├── api/                    ← PHP backend files
│   ├── config.php          ← Database connection
│   └── *.php               ← Various API endpoints
│
├── css/
│   └── style.css           ← All styles
│
├── js/
│   └── main.js             ← Common JavaScript
│
└── database/
    └── campus_portal.sql   ← Database setup script
```

---

## 🎯 Features Overview

### Student Side (View Only)
- ✅ Login with Roll Number + DOB
- ✅ View attendance with percentages
- ✅ View exam timetable
- ✅ Browse lost & found items
- ✅ Read announcements

### Admin Side (Full Control)
- ✅ Add/Edit/Delete students
- ✅ Mark attendance (easy checkbox system)
- ✅ Manage exam schedule
- ✅ Post/Manage lost & found items
- ✅ Post/Delete announcements

---

## ❓ Troubleshooting

### "Database connection failed"
- Make sure MySQL is running in XAMPP
- Check if database `campus_portal` exists in phpMyAdmin

### "404 Page Not Found"
- Check if files are in `C:\xampp\htdocs\campus-portal\`
- Make sure Apache is running

### "Login not working"
- Check roll number format (e.g., BCA23001)
- Date format must be YYYY-MM-DD

---

## 📝 Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: PHP
- **Database**: MySQL
- **Server**: Apache (via XAMPP)

---

## 🎓 Project By

**ICON COMMERCE COLLEGE**  
BCA Final Year Project - ICC Companion

---

*For any issues, re-import the database SQL file and restart XAMPP.*
