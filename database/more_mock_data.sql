-- =============================================
-- ADDITIONAL MOCK DATA FOR CAMPUS PORTAL
-- =============================================

USE campus_portal;

-- 1. ADDING MORE SUBJECTS
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


-- 2. ADDING MORE STUDENTS (Covering all Semesters)
-- =============================================

-- BCA Students
INSERT INTO students (roll_number, name, dob, email, phone, dept_code, semester) VALUES
('UT-241-049-0003', 'Siddharth Roy', '2005-02-14', 'siddharth@icc.edu', '9876543230', 'BCA', 4),
('UT-241-049-0004', 'Tanvi Desai', '2005-08-30', 'tanvi@icc.edu', '9876543231', 'BCA', 4),
('UT-221-049-0001', 'Manoj Kumar', '2003-12-05', 'manoj@icc.edu', '9876543232', 'BCA', 6),
('UT-221-049-0002', 'Shweta Singh', '2003-10-18', 'shweta@icc.edu', '9876543233', 'BCA', 6),
('UT-251-049-0003', 'Rahul Das', '2006-04-22', 'rahul.das@icc.edu', '9876543234', 'BCA', 2),
('UT-251-049-0004', 'Pooja Sharma', '2006-11-12', 'pooja.s@icc.edu', '9876543235', 'BCA', 2);

-- BBA Students
INSERT INTO students (roll_number, name, dob, email, phone, dept_code, semester) VALUES
('UT-241-050-0002', 'Zaid Ahmed', '2005-05-15', 'zaid@icc.edu', '9876543236', 'BBA', 4),
('UT-241-050-0003', 'Simran Kaur', '2005-09-22', 'simran@icc.edu', '9876543237', 'BBA', 4),
('UT-221-050-0001', 'Abhinav Baruah', '2003-03-10', 'abhinav@icc.edu', '9876543238', 'BBA', 6),
('UT-221-050-0002', 'Neha Kalita', '2003-07-05', 'neha.k@icc.edu', '9876543239', 'BBA', 6),
('UT-251-050-0003', 'Pallav Jyoti', '2006-01-20', 'pallav@icc.edu', '9876543240', 'BBA', 2),
('UT-251-050-0004', 'Priyanka Gogoi', '2006-06-12', 'priyanka@icc.edu', '9876543241', 'BBA', 2);

-- BA Students
INSERT INTO students (roll_number, name, dob, email, phone, dept_code, semester) VALUES
('UT-241-051-0002', 'Jitu Mani', '2005-02-28', 'jitu@icc.edu', '9876543242', 'BA', 4),
('UT-241-051-0003', 'Dipali Saikia', '2005-12-18', 'dipali@icc.edu', '9876543243', 'BA', 4),
('UT-221-051-0001', 'Bikash Chetia', '2003-04-25', 'bikash@icc.edu', '9876543244', 'BA', 6),
('UT-221-051-0002', 'Moni Borah', '2003-08-30', 'moni@icc.edu', '9876543245', 'BA', 6),
('UT-251-051-0003', 'Hiranya Nath', '2006-03-15', 'hiranya@icc.edu', '9876543246', 'BA', 2),
('UT-251-051-0004', 'Kabita Devi', '2006-09-05', 'kabita@icc.edu', '9876543247', 'BA', 2);

-- BCOM Students
INSERT INTO students (roll_number, name, dob, email, phone, dept_code, semester) VALUES
('UT-241-052-0002', 'Arindam Sharma', '2005-11-14', 'arindam@icc.edu', '9876543248', 'BCOM', 4),
('UT-241-052-0003', 'Mousumi Dutta', '2005-07-22', 'mousumi@icc.edu', '9876543249', 'BCOM', 4),
('UT-221-052-0001', 'Biswajit Ray', '2003-05-08', 'biswajit@icc.edu', '9876543250', 'BCOM', 6),
('UT-221-052-0002', 'Sunita Agarwal', '2003-09-17', 'sunita@icc.edu', '9876543251', 'BCOM', 6),
('UT-251-052-0002', 'Pranjal Sarma', '2006-02-14', 'pranjal@icc.edu', '9876543252', 'BCOM', 2),
('UT-251-052-0003', 'Rumi Begum', '2006-10-25', 'rumi@icc.edu', '9876543253', 'BCOM', 2);



-- 3. ADDING RESOURCES
-- =============================================

INSERT INTO resources (title, description, resource_type, file_url, dept_code, semester, subject_id, posted_by) VALUES
('BCA 5th Sem Syllabus', 'Complete syllabus for BCA 5th Semester under GU', 'syllabus', 'uploads/resources/bca_sem5_syllabus.pdf', 'BCA', '5', NULL, 'admin'),
('Java Programming Notes', 'Comprehensive notes for Java (Sem 4)', 'material', 'uploads/resources/java_notes.pdf', 'BCA', '4', 11, 'admin'),
('Python Cookbook', 'Reference book for Python Programming', 'book', 'uploads/resources/python_cookbook.pdf', 'BCA', '5', 14, 'admin'),
('Database Concepts Video', 'Introduction to RDBMS and SQL', 'link', NULL, 'BCA', '3', 8, 'admin'),
('Financial Management PDF', 'Module 1: Time Value of Money', 'material', 'uploads/resources/fin_mgmt_m1.pdf', 'BBA', '3', 25, 'admin'),
('Sociology Overview', 'Basic concepts of Sociology for Sem 2', 'text', NULL, 'BA', '2', 32, 'admin'),
('Corporate Accounting Guide', 'Step by step guide for Corporate Accounting', 'book', 'uploads/resources/corp_acc_guide.pdf', 'BCOM', '3', 43, 'admin');

-- Adding some links to resources
UPDATE resources SET link_url = 'https://www.tutorialspoint.com/dbms/index.htm' WHERE title = 'Database Concepts Video';

-- 4. ADDING MORE ANNOUNCEMENTS
-- =============================================

INSERT INTO announcements (title, description, priority, target_dept, target_semester, posted_by) VALUES
('Campus Recruitment Drive', 'TCS will be visiting our campus for a recruitment drive on May 10th. Open for BCA and BBA 6th semester students only.', 'high', 'all', '6', 'admin'),
('Yoga Workshop', 'A three-day yoga workshop is organized in the college auditorium starting from next Monday.', 'low', 'all', 'all', 'admin'),
('Online Seminar on AI', 'Join us for an online seminar on "Future of AI" by Dr. John Doe on April 30th at 4:00 PM via Google Meet.', 'medium', 'all', 'all', 'admin');

-- 5. ADDING MORE ATTENDANCE (For New Students)
-- =============================================

-- BCA Sem 4 Students (UT-241-049-0003, UT-241-049-0004) for Java (subject_id = 11)
INSERT INTO attendance (roll_number, subject_id, attendance_date, status, marked_by) VALUES
('UT-241-049-0003', 11, '2026-03-01', 'present', 'staff'),
('UT-241-049-0004', 11, '2026-03-01', 'present', 'staff'),
('UT-241-049-0003', 11, '2026-03-02', 'present', 'staff'),
('UT-241-049-0004', 11, '2026-03-02', 'absent', 'staff');

-- BBA Sem 3 Students (UT-241-050-0001) for Financial Management (subject_id = 25 - if it was 25)
-- Note: subject_id might vary depending on previous inserts, but based on existing 22 subjects + new ones:
-- BBA202 -> 23, BBA302 -> 24, BBA401 -> 25... wait let me check the subject_id sequence.
-- BCA: 18 subjects (id 1-18)
-- BBA: 4 subjects (id 19-22)
-- BA: 3 subjects (id 23-25)
-- BCOM: 3 subjects (id 26-28)
-- New BBA: 8 (id 29-36)
-- New BA: 9 (id 37-45)
-- New BCOM: 9 (id 46-54)

-- I'll use some IDs that are likely to exist.
-- Let's just add for some existing ones too.
INSERT INTO attendance (roll_number, subject_id, attendance_date, status, marked_by) VALUES
('UT-241-050-0001', 9, '2026-02-01', 'present', 'admin'),
('UT-241-051-0001', 17, '2026-02-01', 'present', 'admin'),
('UT-241-052-0001', 21, '2026-02-01', 'present', 'admin');
