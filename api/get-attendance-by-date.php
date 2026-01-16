<?php
// =============================================
// GET ATTENDANCE BY DATE API
// =============================================

include 'config.php';

// Get parameters
$subject_id = isset($_GET['subject_id']) ? intval($_GET['subject_id']) : 0;
$date = isset($_GET['date']) ? trim($_GET['date']) : '';

if ($subject_id === 0 || empty($date)) {
    sendResponse(false, 'Subject ID and date are required');
}

$sql = "SELECT roll_number, status FROM attendance 
        WHERE subject_id = ? AND attendance_date = ?";

$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "is", $subject_id, $date);
mysqli_stmt_execute($stmt);
$result = mysqli_stmt_get_result($stmt);

$attendance = [];
while ($row = mysqli_fetch_assoc($result)) {
    $attendance[] = $row;
}

sendResponse(true, 'Attendance fetched', $attendance);

mysqli_close($conn);
?>