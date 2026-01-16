<?php
// =============================================
// GET ATTENDANCE API
// =============================================

include 'config.php';

// Get roll number from query
$roll_number = isset($_GET['roll']) ? trim($_GET['roll']) : '';

if (empty($roll_number)) {
    sendResponse(false, 'Roll number is required');
}

// Query for attendance summary by subject
$sql = "SELECT 
            sub.subject_id,
            sub.subject_code,
            sub.subject_name,
            COUNT(a.attendance_id) as total_classes,
            SUM(CASE WHEN a.status = 'present' THEN 1 ELSE 0 END) as present_count,
            ROUND((SUM(CASE WHEN a.status = 'present' THEN 1 ELSE 0 END) / COUNT(a.attendance_id)) * 100, 1) as percentage
        FROM attendance a
        JOIN subjects sub ON a.subject_id = sub.subject_id
        WHERE a.roll_number = ?
        GROUP BY sub.subject_id, sub.subject_code, sub.subject_name
        ORDER BY sub.subject_name";

$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "s", $roll_number);
mysqli_stmt_execute($stmt);
$result = mysqli_stmt_get_result($stmt);

$attendance = [];
while ($row = mysqli_fetch_assoc($result)) {
    $attendance[] = $row;
}

sendResponse(true, 'Attendance fetched', $attendance);

mysqli_close($conn);
?>