-- =============================================
-- CAMPUS PORTAL - DATABASE SETUP (CLEAN VERSION)
-- FOR HOSTING IMPORT (NO CREATE DATABASE)
-- =============================================

-- =============================================
-- TABLE 1: DEPARTMENTS
-- =============================================
CREATE TABLE departments (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_code VARCHAR(10) NOT NULL UNIQUE,
    dept_name VARCHAR(100) NOT NULL
);

-- Insert departments
INSERT INTO departments (dept_code, dept_name) VALUES
('BCA', 'Bachelor of Computer Applications'),
('BBA', 'Bachelor of Business Administration'),
('BA', 'Bachelor of Arts'),
('BCOM', 'Bachelor of Commerce');

-- =============================================
-- TABLE 2: SUBJECTS
-- =============================================
CREATE TABLE subjects (
    subject_id INT PRIMARY KEY AUTO_INCREMENT,
    subject_code VARCHAR(20) NOT NULL,
    subject_name VARCHAR(100) NOT NULL,
    dept_code VARCHAR(10) NOT NULL,
    semester INT NOT NULL,
    FOREIGN KEY (dept_code) REFERENCES departments(dept_code)
);

-- BCA Subjects (Semester 1-6)
INSERT INTO subjects (subject_code, subject_name, dept_code, semester) VALUES
-- Semester 1
('BCA101', 'Computer Fundamentals', 'BCA', 1),
('BCA102', 'Mathematics I', 'BCA', 1),
('BCA103', 'English Communication', 'BCA', 1),
-- Semester 2
('BCA201', 'Programming in C', 'BCA', 2),
('BCA202', 'Mathematics II', 'BCA', 2),
('BCA203', 'Digital Electronics', 'BCA', 2),
-- Semester 3
('BCA301', 'Data Structures', 'BCA', 3),
('BCA302', 'Database Management', 'BCA', 3),
('BCA303', 'Computer Networks', 'BCA', 3),
-- Semester 4
('BCA401', 'Operating Systems', 'BCA', 4),
('BCA402', 'Java Programming', 'BCA', 4),
('BCA403', 'Software Engineering', 'BCA', 4),
-- Semester 5
('BCA501', 'Web Technologies', 'BCA', 5),
('BCA502', 'Python Programming', 'BCA', 5),
('BCA503', 'Computer Graphics', 'BCA', 5),
-- Semester 6
('BCA601', 'Project Work', 'BCA', 6),
('BCA602', 'Cloud Computing', 'BCA', 6),
('BCA603', 'Cyber Security', 'BCA', 6);

-- BBA Subjects (Sample)
INSERT INTO subjects (subject_code, subject_name, dept_code, semester) VALUES
('BBA101', 'Principles of Management', 'BBA', 1),
('BBA102', 'Business Economics', 'BBA', 1),
('BBA201', 'Financial Accounting', 'BBA', 2),
('BBA301', 'Marketing Management', 'BBA', 3);

-- BA Subjects (Sample)
INSERT INTO subjects (subject_code, subject_name, dept_code, semester) VALUES
('BA101', 'English Literature', 'BA', 1),
('BA102', 'History of India', 'BA', 1),
('BA201', 'Political Science', 'BA', 2);

-- BCOM Subjects (Sample)
INSERT INTO subjects (subject_code, subject_name, dept_code, semester) VALUES
('BCOM101', 'Financial Accounting', 'BCOM', 1),
('BCOM102', 'Business Law', 'BCOM', 1),
('BCOM201', 'Cost Accounting', 'BCOM', 2);

-- =============================================
-- TABLE 3: STUDENTS
-- =============================================
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    roll_number VARCHAR(20) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    dob DATE NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(15),
    dept_code VARCHAR(10) NOT NULL,
    semester INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (dept_code) REFERENCES departments(dept_code)
);

-- Insert 20 sample students
INSERT INTO students (roll_number, name, dob, email, phone, dept_code, semester) VALUES
('BCA23001', 'Rahul Kumar', '2004-05-15', 'rahul@icc.edu', '9876543210', 'BCA', 5),
('BCA23002', 'Priya Sharma', '2004-08-22', 'priya@icc.edu', '9876543211', 'BCA', 5),
('BCA23003', 'Amit Singh', '2004-03-10', 'amit@icc.edu', '9876543212', 'BCA', 5),
('BCA23004', 'Neha Gupta', '2004-11-05', 'neha@icc.edu', '9876543213', 'BCA', 5),
('BCA24001', 'Vikram Patel', '2005-01-20', 'vikram@icc.edu', '9876543214', 'BCA', 3),
('BCA24002', 'Anjali Verma', '2005-07-12', 'anjali@icc.edu', '9876543215', 'BCA', 3),
('BCA25001', 'Rohan Joshi', '2006-02-28', 'rohan@icc.edu', '9876543216', 'BCA', 1),
('BCA25002', 'Sneha Reddy', '2006-09-18', 'sneha@icc.edu', '9876543217', 'BCA', 1),
('BBA23001', 'Arjun Malhotra', '2004-04-25', 'arjun@icc.edu', '9876543218', 'BBA', 5),
('BBA23002', 'Kavya Nair', '2004-06-30', 'kavya@icc.edu', '9876543219', 'BBA', 5),
('BBA24001', 'Sanjay Kapoor', '2005-03-15', 'sanjay@icc.edu', '9876543220', 'BBA', 3),
('BBA25001', 'Divya Sharma', '2006-08-05', 'divya@icc.edu', '9876543221', 'BBA', 1),
('BBA25002', 'Manish Kumar', '2006-12-10', 'manish@icc.edu', '9876543222', 'BBA', 1),
('BA23001', 'Pooja Singh', '2004-02-14', 'pooja@icc.edu', '9876543223', 'BA', 5),
('BA24001', 'Ravi Shankar', '2005-05-22', 'ravi@icc.edu', '9876543224', 'BA', 3),
('BA25001', 'Meera Jain', '2006-07-08', 'meera@icc.edu', '9876543225', 'BA', 1),
('BA25002', 'Karan Thakur', '2006-11-25', 'karan@icc.edu', '9876543226', 'BA', 1),
('BCOM23001', 'Ananya Iyer', '2004-09-12', 'ananya@icc.edu', '9876543227', 'BCOM', 5),
('BCOM24001', 'Suresh Menon', '2005-04-03', 'suresh@icc.edu', '9876543228', 'BCOM', 3),
('BCOM25001', 'Lakshmi Rao', '2006-06-17', 'lakshmi@icc.edu', '9876543229', 'BCOM', 1);

-- =============================================
-- TABLE 4: ADMINS
-- =============================================
CREATE TABLE admins (
    admin_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    name VARCHAR(100) NOT NULL,
    role VARCHAR(50) DEFAULT 'admin'
);

-- Insert default admin
INSERT INTO admins (username, password, name, role) VALUES
('admin', 'admin123', 'Dr. Sharma', 'super-admin'),
('staff', 'staff123', 'Mr. Verma', 'staff');

-- =============================================
-- TABLE 5: ATTENDANCE
-- =============================================
CREATE TABLE attendance (
    attendance_id INT PRIMARY KEY AUTO_INCREMENT,
    roll_number VARCHAR(20) NOT NULL,
    subject_id INT NOT NULL,
    attendance_date DATE NOT NULL,
    status ENUM('present', 'absent') DEFAULT 'present',
    marked_by VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (roll_number) REFERENCES students(roll_number),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id),
    UNIQUE KEY unique_attendance (roll_number, subject_id, attendance_date)
);

-- Sample attendance data (BCA Semester 5)
INSERT INTO attendance (roll_number, subject_id, attendance_date, status, marked_by) VALUES
('BCA23001', 13, '2026-01-06', 'present', 'admin'),
('BCA23002', 13, '2026-01-06', 'present', 'admin'),
('BCA23003', 13, '2026-01-06', 'absent', 'admin'),
('BCA23004', 13, '2026-01-06', 'present', 'admin'),
('BCA23001', 13, '2026-01-07', 'present', 'admin'),
('BCA23002', 13, '2026-01-07', 'present', 'admin'),
('BCA23003', 13, '2026-01-07', 'present', 'admin'),
('BCA23004', 13, '2026-01-07', 'absent', 'admin'),
('BCA23001', 13, '2026-01-08', 'present', 'admin'),
('BCA23002', 13, '2026-01-08', 'absent', 'admin'),
('BCA23003', 13, '2026-01-08', 'present', 'admin'),
('BCA23004', 13, '2026-01-08', 'present', 'admin'),
('BCA23001', 14, '2026-01-06', 'present', 'admin'),
('BCA23002', 14, '2026-01-06', 'present', 'admin'),
('BCA23003', 14, '2026-01-06', 'present', 'admin'),
('BCA23004', 14, '2026-01-06', 'present', 'admin'),
('BCA23001', 14, '2026-01-08', 'present', 'admin'),
('BCA23002', 14, '2026-01-08', 'present', 'admin'),
('BCA23003', 14, '2026-01-08', 'absent', 'admin'),
('BCA23004', 14, '2026-01-08', 'present', 'admin'),
('BBA23001', 9, '2026-01-06', 'present', 'admin'),
('BBA23002', 9, '2026-01-06', 'present', 'admin'),
('BBA23001', 9, '2026-01-07', 'present', 'admin'),
('BBA23002', 9, '2026-01-07', 'absent', 'admin'),
('BA25001', 17, '2026-01-06', 'present', 'admin'),
('BA25002', 17, '2026-01-06', 'present', 'admin'),
('BA25001', 17, '2026-01-07', 'present', 'admin'),
('BA25002', 17, '2026-01-07', 'present', 'admin'),
('BCOM25001', 21, '2026-01-06', 'present', 'admin'),
('BCOM25001', 21, '2026-01-07', 'present', 'admin'),
('BCOM25001', 21, '2026-01-08', 'absent', 'admin');

-- =============================================
-- TABLE 6: EXAMS
-- =============================================
CREATE TABLE exams (
    exam_id INT PRIMARY KEY AUTO_INCREMENT,
    subject_id INT NOT NULL,
    exam_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    room VARCHAR(50),
    exam_type ENUM('sessional', 'final') DEFAULT 'final',
    attachment_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);

-- Sample exam timetable
INSERT INTO exams (subject_id, exam_date, start_time, end_time, room, exam_type) VALUES
(13, '2026-02-15', '10:00:00', '13:00:00', 'Lab 101', 'sessional'),
(14, '2026-02-17', '10:00:00', '13:00:00', 'Lab 102', 'sessional'),
(15, '2026-02-19', '14:00:00', '17:00:00', 'Room 203', 'sessional'),
(13, '2026-04-10', '10:00:00', '13:00:00', 'Hall A', 'final'),
(14, '2026-04-12', '10:00:00', '13:00:00', 'Hall A', 'final'),
(15, '2026-04-14', '14:00:00', '17:00:00', 'Hall B', 'final'),
(9, '2026-02-16', '10:00:00', '13:00:00', 'Room 105', 'sessional'),
(9, '2026-04-11', '10:00:00', '13:00:00', 'Hall B', 'final');

-- =============================================
-- TABLE 7: LOST AND FOUND
-- =============================================
CREATE TABLE lost_found (
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    category ENUM('id-card', 'phone', 'wallet', 'books', 'electronics', 'other') DEFAULT 'other',
    item_type ENUM('lost', 'found') NOT NULL,
    location VARCHAR(100),
    item_date DATE,
    contact_info VARCHAR(100),
    image_url VARCHAR(255),
    status ENUM('active', 'claimed') DEFAULT 'active',
    posted_by VARCHAR(50),
    claimed_by VARCHAR(20),
    claimed_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Sample lost and found items
INSERT INTO lost_found (title, description, category, item_type, location, item_date, contact_info, status, posted_by) VALUES
('Black Leather Wallet', 'Black leather wallet with some cash and ID cards inside', 'wallet', 'found', 'Library - 2nd Floor', '2026-01-10', 'Security Office - Ext. 1234', 'active', 'admin'),
('Student ID Card - Rahul K', 'ID card found near canteen', 'id-card', 'found', 'Canteen Area', '2026-01-12', 'Main Office', 'active', 'admin'),
('Blue Umbrella', 'Lost my blue umbrella somewhere in college', 'other', 'lost', 'Unknown', '2026-01-14', 'Contact: 9876543210', 'active', 'BCA23001'),
('Samsung Earbuds', 'White Samsung earbuds in black case', 'electronics', 'found', 'Computer Lab', '2026-01-15', 'Lab Attendant', 'active', 'admin'),
('Engineering Mathematics Book', 'Found a maths textbook on bench', 'books', 'found', 'Garden Area', '2026-01-08', 'Library Counter', 'claimed', 'admin'),
('iPhone Charger', 'White Apple charger with cable', 'electronics', 'found', 'Classroom 201', '2026-01-16', 'Reception Desk', 'active', 'admin'),
('House Keys', 'Set of 3 keys on a blue keychain', 'other', 'lost', 'Parking Area', '2026-01-11', 'Call: 9988776655', 'active', 'BBA23001');

-- =============================================
-- TABLE 8: ANNOUNCEMENTS
-- =============================================
CREATE TABLE announcements (
    announcement_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    attachment_url VARCHAR(255),
    priority ENUM('high', 'medium', 'low') DEFAULT 'medium',
    target_dept VARCHAR(50) DEFAULT 'all',
    target_semester VARCHAR(20) DEFAULT 'all',
    posted_by VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Sample announcements
INSERT INTO announcements (title, description, priority, target_dept, target_semester, posted_by) VALUES
('Republic Day Holiday', 'College will remain closed on 26th January 2026 for Republic Day celebrations. All students are encouraged to participate in the flag hoisting ceremony at 8:00 AM.', 'high', 'all', 'all', 'admin'),
('Fee Payment Deadline', 'Last date for semester fee payment is February 5, 2026. Late fee of Rs. 500 will be applicable after the deadline.', 'high', 'all', 'all', 'admin'),
('Mid-Term Exam Schedule', 'Mid-term examinations for Semester 5 will begin from February 15, 2026. Detailed timetable has been published.', 'medium', 'all', '5', 'admin'),
('Library Timing Change', 'Library will remain open till 8:00 PM from Monday to Friday starting next week.', 'low', 'all', 'all', 'admin'),
('Sports Day Registration', 'Annual sports day is scheduled for February 20, 2026. Register with your department sports coordinator by January 25.', 'medium', 'all', 'all', 'admin'),
('Guest Lecture on AI', 'A special guest lecture on Artificial Intelligence will be held on Jan 22 at 2 PM in the Auditorium. All BCA students must attend.', 'medium', 'BCA', 'all', 'admin'),
('Placement Drive Notice', 'TCS will be visiting campus on February 1st for placement. Eligible students should register by Jan 28.', 'high', 'BCA', '5', 'admin');

-- =============================================
-- TABLE 9: CLASS ROUTINES
-- =============================================
CREATE TABLE class_routines (
    routine_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL,
    file_url VARCHAR(255) NOT NULL,
    dept_code VARCHAR(10) NOT NULL,
    semester VARCHAR(10) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =============================================
-- TABLE 10: EXAM SCHEDULES
-- =============================================
CREATE TABLE exam_schedules (
    schedule_id INT PRIMARY KEY AUTO_INCREMENT,
    schedule_type ENUM('sessional', 'final') NOT NULL UNIQUE,
    file_url VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =============================================
-- END OF DATABASE SETUP
-- =============================================

