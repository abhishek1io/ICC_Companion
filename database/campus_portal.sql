-- =============================================
-- CAMPUS PORTAL - DATABASE SETUP
-- ICON COMMERCE COLLEGE (ICC)
-- =============================================

-- Create database
CREATE DATABASE IF NOT EXISTS campus_portal;
USE campus_portal;

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

-- Insert 20 sample students (mixed departments)
INSERT INTO students (roll_number, name, dob, email, phone, dept_code, semester) VALUES
-- BCA Students (8)
('UT-231-049-0001', 'Rahul Kumar', '2004-05-15', 'rahul@icc.edu', '9876543210', 'BCA', 5),
('UT-231-049-0002', 'Priya Sharma', '2004-08-22', 'priya@icc.edu', '9876543211', 'BCA', 5),
('UT-231-049-0003', 'Amit Singh', '2004-03-10', 'amit@icc.edu', '9876543212', 'BCA', 5),
('UT-231-049-0004', 'Neha Gupta', '2004-11-05', 'neha@icc.edu', '9876543213', 'BCA', 5),
('UT-241-049-0001', 'Vikram Patel', '2005-01-20', 'vikram@icc.edu', '9876543214', 'BCA', 3),
('UT-241-049-0002', 'Anjali Verma', '2005-07-12', 'anjali@icc.edu', '9876543215', 'BCA', 3),
('UT-251-049-0001', 'Rohan Joshi', '2006-02-28', 'rohan@icc.edu', '9876543216', 'BCA', 1),
('UT-251-049-0002', 'Sneha Reddy', '2006-09-18', 'sneha@icc.edu', '9876543217', 'BCA', 1),

-- BBA Students (5)
('UT-231-050-0001', 'Arjun Malhotra', '2004-04-25', 'arjun@icc.edu', '9876543218', 'BBA', 5),
('UT-231-050-0002', 'Kavya Nair', '2004-06-30', 'kavya@icc.edu', '9876543219', 'BBA', 5),
('UT-241-050-0001', 'Sanjay Kapoor', '2005-03-15', 'sanjay@icc.edu', '9876543220', 'BBA', 3),
('UT-251-050-0001', 'Divya Sharma', '2006-08-05', 'divya@icc.edu', '9876543221', 'BBA', 1),
('UT-251-050-0002', 'Manish Kumar', '2006-12-10', 'manish@icc.edu', '9876543222', 'BBA', 1),

-- BA Students (4)
('UT-231-051-0001', 'Pooja Singh', '2004-02-14', 'pooja@icc.edu', '9876543223', 'BA', 5),
('UT-241-051-0001', 'Ravi Shankar', '2005-05-22', 'ravi@icc.edu', '9876543224', 'BA', 3),
('UT-251-051-0001', 'Meera Jain', '2006-07-08', 'meera@icc.edu', '9876543225', 'BA', 1),
('UT-251-051-0002', 'Karan Thakur', '2006-11-25', 'karan@icc.edu', '9876543226', 'BA', 1),

-- BCOM Students (3)
('UT-231-052-0001', 'Ananya Iyer', '2004-09-12', 'ananya@icc.edu', '9876543227', 'BCOM', 5),
('UT-241-052-0001', 'Suresh Menon', '2005-04-03', 'suresh@icc.edu', '9876543228', 'BCOM', 3),
('UT-251-052-0001', 'Lakshmi Rao', '2006-06-17', 'lakshmi@icc.edu', '9876543229', 'BCOM', 1);

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

-- Insert default admin (password: admin123)
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

-- Sample attendance data for BCA Semester 5 students
-- Web Technologies (subject_id = 13)
INSERT INTO attendance (roll_number, subject_id, attendance_date, status, marked_by) VALUES
('UT-231-049-0001', 13, '2026-01-06', 'present', 'admin'),
('UT-231-049-0002', 13, '2026-01-06', 'present', 'admin'),
('UT-231-049-0003', 13, '2026-01-06', 'absent', 'admin'),
('UT-231-049-0004', 13, '2026-01-06', 'present', 'admin'),
('UT-231-049-0001', 13, '2026-01-07', 'present', 'admin'),
('UT-231-049-0002', 13, '2026-01-07', 'present', 'admin'),
('UT-231-049-0003', 13, '2026-01-07', 'present', 'admin'),
('UT-231-049-0004', 13, '2026-01-07', 'absent', 'admin'),
('UT-231-049-0001', 13, '2026-01-08', 'present', 'admin'),
('UT-231-049-0002', 13, '2026-01-08', 'absent', 'admin'),
('UT-231-049-0003', 13, '2026-01-08', 'present', 'admin'),
('UT-231-049-0004', 13, '2026-01-08', 'present', 'admin'),
('UT-231-049-0001', 13, '2026-01-09', 'present', 'admin'),
('UT-231-049-0002', 13, '2026-01-09', 'present', 'admin'),
('UT-231-049-0003', 13, '2026-01-09', 'present', 'admin'),
('UT-231-049-0004', 13, '2026-01-09', 'present', 'admin'),
('UT-231-049-0001', 13, '2026-01-10', 'present', 'admin'),
('UT-231-049-0002', 13, '2026-01-10', 'present', 'admin'),
('UT-231-049-0003', 13, '2026-01-10', 'absent', 'admin'),
('UT-231-049-0004', 13, '2026-01-10', 'present', 'admin');

-- Python Programming (subject_id = 14)
INSERT INTO attendance (roll_number, subject_id, attendance_date, status, marked_by) VALUES
('UT-231-049-0001', 14, '2026-01-06', 'present', 'admin'),
('UT-231-049-0002', 14, '2026-01-06', 'present', 'admin'),
('UT-231-049-0003', 14, '2026-01-06', 'present', 'admin'),
('UT-231-049-0004', 14, '2026-01-06', 'present', 'admin'),
('UT-231-049-0001', 14, '2026-01-08', 'present', 'admin'),
('UT-231-049-0002', 14, '2026-01-08', 'present', 'admin'),
('UT-231-049-0003', 14, '2026-01-08', 'absent', 'admin'),
('UT-231-049-0004', 14, '2026-01-08', 'present', 'admin'),
('UT-231-049-0001', 14, '2026-01-10', 'absent', 'admin'),
('UT-231-049-0002', 14, '2026-01-10', 'present', 'admin'),
('UT-231-049-0003', 14, '2026-01-10', 'present', 'admin'),
('UT-231-049-0004', 14, '2026-01-10', 'present', 'admin');

-- BBA Semester 5 Attendance (subject_id = 9: Marketing Management)
INSERT INTO attendance (roll_number, subject_id, attendance_date, status, marked_by) VALUES
('UT-231-050-0001', 9, '2026-01-06', 'present', 'admin'),
('UT-231-050-0002', 9, '2026-01-06', 'present', 'admin'),
('UT-231-050-0001', 9, '2026-01-07', 'present', 'admin'),
('UT-231-050-0002', 9, '2026-01-07', 'absent', 'admin'),
('UT-231-050-0001', 9, '2026-01-08', 'present', 'admin'),
('UT-231-050-0002', 9, '2026-01-08', 'present', 'admin'),
('UT-231-050-0001', 9, '2026-01-09', 'absent', 'admin'),
('UT-231-050-0002', 9, '2026-01-09', 'present', 'admin'),
('UT-231-050-0001', 9, '2026-01-10', 'present', 'admin'),
('UT-231-050-0002', 9, '2026-01-10', 'present', 'admin');

-- BA Semester 1 Attendance (subject_id = 17: English Literature)
INSERT INTO attendance (roll_number, subject_id, attendance_date, status, marked_by) VALUES
('UT-251-051-0001', 17, '2026-01-06', 'present', 'admin'),
('UT-251-051-0002', 17, '2026-01-06', 'present', 'admin'),
('UT-251-051-0001', 17, '2026-01-07', 'present', 'admin'),
('UT-251-051-0002', 17, '2026-01-07', 'present', 'admin'),
('UT-251-051-0001', 17, '2026-01-08', 'absent', 'admin'),
('UT-251-051-0002', 17, '2026-01-08', 'present', 'admin'),
('UT-251-051-0001', 17, '2026-01-09', 'present', 'admin'),
('UT-251-051-0002', 17, '2026-01-09', 'absent', 'admin');

-- BCOM Semester 1 Attendance (subject_id = 21: Financial Accounting)
INSERT INTO attendance (roll_number, subject_id, attendance_date, status, marked_by) VALUES
('UT-251-052-0001', 21, '2026-01-06', 'present', 'admin'),
('UT-251-052-0001', 21, '2026-01-07', 'present', 'admin'),
('UT-251-052-0001', 21, '2026-01-08', 'present', 'admin'),
('UT-251-052-0001', 21, '2026-01-09', 'absent', 'admin'),
('UT-251-052-0001', 21, '2026-01-10', 'present', 'admin');

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

-- Sample exam timetable for BCA Semester 5
INSERT INTO exams (subject_id, exam_date, start_time, end_time, room, exam_type) VALUES
(13, '2026-02-15', '10:00:00', '13:00:00', 'Lab 101', 'sessional'),
(14, '2026-02-17', '10:00:00', '13:00:00', 'Lab 102', 'sessional'),
(15, '2026-02-19', '14:00:00', '17:00:00', 'Room 203', 'sessional'),
(13, '2026-04-10', '10:00:00', '13:00:00', 'Hall A', 'final'),
(14, '2026-04-12', '10:00:00', '13:00:00', 'Hall A', 'final'),
(15, '2026-04-14', '14:00:00', '17:00:00', 'Hall B', 'final');

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
('Blue Umbrella', 'Lost my blue umbrella somewhere in college', 'other', 'lost', 'Unknown', '2026-01-14', 'Contact: 9876543210', 'active', 'UT-231-049-0001'),
('Samsung Earbuds', 'White Samsung earbuds in black case', 'electronics', 'found', 'Computer Lab', '2026-01-15', 'Lab Attendant', 'active', 'admin'),
('Engineering Mathematics Book', 'Found a maths textbook on bench', 'books', 'found', 'Garden Area', '2026-01-08', 'Library Counter', 'claimed', 'admin');

-- =============================================
-- TABLE 8: ANNOUNCEMENTS
-- =============================================
CREATE TABLE announcements (
    announcement_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    attachment_url VARCHAR(255),
    link_url VARCHAR(255),
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
('Sports Day Registration', 'Annual sports day is scheduled for February 20, 2026. Register with your department sports coordinator by January 25.', 'medium', 'all', 'all', 'admin');

-- =============================================
-- TABLE 9: CLASS ROUTINES (One file per dept+sem)
-- =============================================
CREATE TABLE class_routines (
    routine_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL,
    file_url VARCHAR(255) NOT NULL,
    dept_code VARCHAR(10) NOT NULL,
    semester VARCHAR(10) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Sample class routine
INSERT INTO class_routines (title, file_url, dept_code, semester) VALUES
('BCA Semester 5 Weekly Routine', 'uploads/routines/bca_sem5_routine.pdf', 'BCA', '5');

-- =============================================
-- TABLE 11: RESOURCES (Syllabus, Books, Materials, Links, Text)
-- =============================================
CREATE TABLE resources (
    resource_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    resource_type ENUM('syllabus', 'book', 'material', 'link', 'text', 'others') NOT NULL,
    file_url VARCHAR(255),
    link_url TEXT,
    content_text TEXT,
    dept_code VARCHAR(10) NOT NULL,
    semester VARCHAR(10) NOT NULL,
    subject_id INT,
    posted_by VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (dept_code) REFERENCES departments(dept_code),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);

-- =============================================
-- TABLE 10: EXAM SCHEDULES (One file per type)
-- =============================================
CREATE TABLE exam_schedules (
    schedule_id INT PRIMARY KEY AUTO_INCREMENT,
    schedule_type ENUM('sessional', 'final') NOT NULL UNIQUE,
    file_url VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =============================================
-- HELPFUL VIEWS (Optional but useful)
-- =============================================

-- View: Student attendance summary
CREATE VIEW student_attendance_summary AS
SELECT 
    s.roll_number,
    s.name,
    s.dept_code,
    s.semester,
    sub.subject_name,
    sub.subject_id,
    COUNT(a.attendance_id) as total_classes,
    SUM(CASE WHEN a.status = 'present' THEN 1 ELSE 0 END) as present_count,
    ROUND((SUM(CASE WHEN a.status = 'present' THEN 1 ELSE 0 END) / COUNT(a.attendance_id)) * 100, 1) as percentage
FROM students s
JOIN subjects sub ON s.dept_code = sub.dept_code AND s.semester = sub.semester
LEFT JOIN attendance a ON s.roll_number = a.roll_number AND sub.subject_id = a.subject_id
GROUP BY s.roll_number, s.name, s.dept_code, s.semester, sub.subject_name, sub.subject_id;

-- =============================================
-- ADDITIONAL MOCK DATA
-- =============================================

-- BBA Subjects (Remaining Semesters)
INSERT INTO subjects (subject_code, subject_name, dept_code, semester) VALUES
('BBA202', 'Organizational Behavior', 'BBA', 2),
('BBA302', 'Financial Management', 'BBA', 3),
('BBA401', 'Human Resource Management', 'BBA', 4),
('BBA402', 'Business Research Methods', 'BBA', 4),
('BBA501', 'Operations Management', 'BBA', 5),
('BBA502', 'Strategic Management', 'BBA', 5),
('BBA601', 'Entrepreneurship', 'BBA', 6),
('BBA602', 'Project Management', 'BBA', 6);

-- BA Subjects (Remaining Semesters)
INSERT INTO subjects (subject_code, subject_name, dept_code, semester) VALUES
('BA202', 'Sociology of India', 'BA', 2),
('BA301', 'Economics I', 'BA', 3),
('BA302', 'Geography of India', 'BA', 3),
('BA401', 'Psychology Fundamentals', 'BA', 4),
('BA402', 'Public Administration', 'BA', 4),
('BA501', 'International Relations', 'BA', 5),
('BA502', 'Indian Economy', 'BA', 5),
('BA601', 'Ethics and Values', 'BA', 6),
('BA602', 'World History', 'BA', 6);

-- BCOM Subjects (Remaining Semesters)
INSERT INTO subjects (subject_code, subject_name, dept_code, semester) VALUES
('BCOM202', 'Company Law', 'BCOM', 2),
('BCOM301', 'Corporate Accounting', 'BCOM', 3),
('BCOM302', 'Income Tax Law', 'BCOM', 3),
('BCOM401', 'Management Accounting', 'BCOM', 4),
('BCOM402', 'Auditing', 'BCOM', 4),
('BCOM501', 'GST and Indirect Taxes', 'BCOM', 5),
('BCOM502', 'Investment Management', 'BCOM', 5),
('BCOM601', 'Banking and Insurance', 'BCOM', 6),
('BCOM602', 'Financial Markets', 'BCOM', 6);

-- More Students (Covering all Semesters)
INSERT INTO students (roll_number, name, dob, email, phone, dept_code, semester) VALUES
('UT-241-049-0003', 'Siddharth Roy', '2005-02-14', 'siddharth@icc.edu', '9876543230', 'BCA', 4),
('UT-241-049-0004', 'Tanvi Desai', '2005-08-30', 'tanvi@icc.edu', '9876543231', 'BCA', 4),
('UT-221-049-0001', 'Manoj Kumar', '2003-12-05', 'manoj@icc.edu', '9876543232', 'BCA', 6),
('UT-221-049-0002', 'Shweta Singh', '2003-10-18', 'shweta@icc.edu', '9876543233', 'BCA', 6),
('UT-251-049-0003', 'Rahul Das', '2006-04-22', 'rahul.das@icc.edu', '9876543234', 'BCA', 2),
('UT-251-049-0004', 'Pooja Sharma', '2006-11-12', 'pooja.s@icc.edu', '9876543235', 'BCA', 2),
('UT-241-050-0002', 'Zaid Ahmed', '2005-05-15', 'zaid@icc.edu', '9876543236', 'BBA', 4),
('UT-241-050-0003', 'Simran Kaur', '2005-09-22', 'simran@icc.edu', '9876543237', 'BBA', 4),
('UT-221-050-0001', 'Abhinav Baruah', '2003-03-10', 'abhinav@icc.edu', '9876543238', 'BBA', 6),
('UT-221-050-0002', 'Neha Kalita', '2003-07-05', 'neha.k@icc.edu', '9876543239', 'BBA', 6),
('UT-251-050-0003', 'Pallav Jyoti', '2006-01-20', 'pallav@icc.edu', '9876543240', 'BBA', 2),
('UT-251-050-0004', 'Priyanka Gogoi', '2006-06-12', 'priyanka@icc.edu', '9876543241', 'BBA', 2),
('UT-241-051-0002', 'Jitu Mani', '2005-02-28', 'jitu@icc.edu', '9876543242', 'BA', 4),
('UT-241-051-0003', 'Dipali Saikia', '2005-12-18', 'dipali@icc.edu', '9876543243', 'BA', 4),
('UT-221-051-0001', 'Bikash Chetia', '2003-04-25', 'bikash@icc.edu', '9876543244', 'BA', 6),
('UT-221-051-0002', 'Moni Borah', '2003-08-30', 'moni@icc.edu', '9876543245', 'BA', 6),
('UT-251-051-0003', 'Hiranya Nath', '2006-03-15', 'hiranya@icc.edu', '9876543246', 'BA', 2),
('UT-251-051-0004', 'Kabita Devi', '2006-09-05', 'kabita@icc.edu', '9876543247', 'BA', 2),
('UT-241-052-0002', 'Arindam Sharma', '2005-11-14', 'arindam@icc.edu', '9876543248', 'BCOM', 4),
('UT-241-052-0003', 'Mousumi Dutta', '2005-07-22', 'mousumi@icc.edu', '9876543249', 'BCOM', 4),
('UT-221-052-0001', 'Biswajit Ray', '2003-05-08', 'biswajit@icc.edu', '9876543250', 'BCOM', 6),
('UT-221-052-0002', 'Sunita Agarwal', '2003-09-17', 'sunita@icc.edu', '9876543251', 'BCOM', 6),
('UT-251-052-0002', 'Pranjal Sarma', '2006-02-14', 'pranjal@icc.edu', '9876543252', 'BCOM', 2),
('UT-251-052-0003', 'Rumi Begum', '2006-10-25', 'rumi@icc.edu', '9876543253', 'BCOM', 2);


-- Additional Resources
INSERT INTO resources (title, description, resource_type, file_url, dept_code, semester, subject_id, posted_by) VALUES
('BCA 5th Sem Syllabus', 'Complete syllabus for BCA 5th Semester under GU', 'syllabus', 'uploads/resources/bca_sem5_syllabus.pdf', 'BCA', '5', NULL, 'admin'),
('Java Programming Notes', 'Comprehensive notes for Java (Sem 4)', 'material', 'uploads/resources/java_notes.pdf', 'BCA', '4', 11, 'admin'),
('Python Cookbook', 'Reference book for Python Programming', 'book', 'uploads/resources/python_cookbook.pdf', 'BCA', '5', 14, 'admin'),
('Database Concepts Video', 'Introduction to RDBMS and SQL', 'link', NULL, 'BCA', '3', 8, 'admin'),
('Financial Management PDF', 'Module 1: Time Value of Money', 'material', 'uploads/resources/fin_mgmt_m1.pdf', 'BBA', '3', 25, 'admin'),
('Sociology Overview', 'Basic concepts of Sociology for Sem 2', 'text', NULL, 'BA', '2', 32, 'admin'),
('Corporate Accounting Guide', 'Step by step guide for Corporate Accounting', 'book', 'uploads/resources/corp_acc_guide.pdf', 'BCOM', '3', 43, 'admin');

-- Additional Announcements
INSERT INTO announcements (title, description, priority, target_dept, target_semester, posted_by) VALUES
('Campus Recruitment Drive', 'TCS will be visiting our campus for a recruitment drive on May 10th. Open for BCA and BBA 6th semester students only.', 'high', 'all', '6', 'admin'),
('Yoga Workshop', 'A three-day yoga workshop is organized in the college auditorium starting from next Monday.', 'low', 'all', 'all', 'admin'),
('Online Seminar on AI', 'Join us for an online seminar on "Future of AI" by Dr. John Doe on April 30th at 4:00 PM via Google Meet.', 'medium', 'all', 'all', 'admin');

-- =============================================
-- END OF DATABASE SETUP
-- =============================================

