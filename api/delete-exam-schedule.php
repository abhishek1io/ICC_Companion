<?php
// =============================================
// DELETE EXAM SCHEDULE API
// =============================================

include 'config.php';

$schedule_type = isset($_POST['schedule_type']) ? trim($_POST['schedule_type']) : '';
$dept_code = isset($_POST['dept_code']) ? trim($_POST['dept_code']) : '';
$semester = isset($_POST['semester']) ? intval($_POST['semester']) : 0;

if (empty($schedule_type)) {
    sendResponse(false, 'Invalid schedule type');
}

// Get file to delete
$sql = "SELECT file_url FROM exam_schedules WHERE schedule_type = ? AND dept_code = ? AND semester = ?";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "ssi", $schedule_type, $dept_code, $semester);
mysqli_stmt_execute($stmt);
$result = mysqli_stmt_get_result($stmt);

if ($row = mysqli_fetch_assoc($result)) {
    $filePath = '../' . $row['file_url'];
    if (file_exists($filePath)) {
        unlink($filePath);
    }
}

// Delete from database
$sql = "DELETE FROM exam_schedules WHERE schedule_type = ? AND dept_code = ? AND semester = ?";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "ssi", $schedule_type, $dept_code, $semester);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Schedule deleted');
} else {
    sendResponse(false, 'Failed to delete');
}

mysqli_close($conn);
?>