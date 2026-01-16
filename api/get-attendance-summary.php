<?php
// =============================================
// GET ATTENDANCE SUMMARY API
// Shows student attendance with counts and percentages
// =============================================

include 'config.php';

$dept = isset($_GET['dept']) ? trim($_GET['dept']) : '';
$semester = isset($_GET['semester']) ? trim($_GET['semester']) : '';
$subject_id = isset($_GET['subject_id']) ? intval($_GET['subject_id']) : 0;
$month = isset($_GET['month']) ? trim($_GET['month']) : '';

// First get the attendance data
$sql = "SELECT 
            s.roll_number,
            s.name as student_name,
            s.dept_code,
            s.semester,
            sub.subject_name,
            sub.subject_id,
            COALESCE(SUM(CASE WHEN a.status = 'present' THEN 1 ELSE 0 END), 0) as present_count,
            COALESCE(COUNT(a.attendance_id), 0) as total_classes
        FROM students s
        CROSS JOIN subjects sub
        LEFT JOIN attendance a ON s.roll_number = a.roll_number AND sub.subject_id = a.subject_id";

// Add month filter to join if specified
if (!empty($month)) {
    $sql = "SELECT 
            s.roll_number,
            s.name as student_name,
            s.dept_code,
            s.semester,
            sub.subject_name,
            sub.subject_id,
            COALESCE(SUM(CASE WHEN a.status = 'present' THEN 1 ELSE 0 END), 0) as present_count,
            COALESCE(COUNT(a.attendance_id), 0) as total_classes
        FROM students s
        CROSS JOIN subjects sub
        LEFT JOIN attendance a ON s.roll_number = a.roll_number 
            AND sub.subject_id = a.subject_id 
            AND DATE_FORMAT(a.attendance_date, '%Y-%m') = '" . mysqli_real_escape_string($conn, $month) . "'";
}

$sql .= " WHERE s.dept_code = sub.dept_code AND s.semester = sub.semester";

if (!empty($dept)) {
    $sql .= " AND s.dept_code = '" . mysqli_real_escape_string($conn, $dept) . "'";
}

if (!empty($semester)) {
    $sql .= " AND s.semester = '" . mysqli_real_escape_string($conn, $semester) . "'";
}

$roll_number = isset($_GET['roll_number']) ? trim($_GET['roll_number']) : '';
if (!empty($roll_number)) {
    $sql .= " AND s.roll_number = '" . mysqli_real_escape_string($conn, $roll_number) . "'";
}

if ($subject_id > 0) {
    $sql .= " AND sub.subject_id = " . $subject_id;
}

$sql .= " GROUP BY s.roll_number, sub.subject_id
          ORDER BY s.dept_code, s.semester, s.roll_number, sub.subject_name";

$result = mysqli_query($conn, $sql);

if (!$result) {
    sendResponse(false, 'Database error: ' . mysqli_error($conn));
}

$records = [];
while ($row = mysqli_fetch_assoc($result)) {
    // Only include if there's at least some attendance data or show all for admin view
    $records[] = $row;
}

sendResponse(true, 'Attendance summary fetched', $records);

mysqli_close($conn);
?>