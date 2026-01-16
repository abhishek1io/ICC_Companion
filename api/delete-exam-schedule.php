<?php
// =============================================
// DELETE EXAM SCHEDULE API
// =============================================

include 'config.php';

$schedule_type = isset($_POST['schedule_type']) ? trim($_POST['schedule_type']) : '';

if (empty($schedule_type)) {
    sendResponse(false, 'Invalid schedule type');
}

// Get file to delete
$sql = "SELECT file_url FROM exam_schedules WHERE schedule_type = ?";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "s", $schedule_type);
mysqli_stmt_execute($stmt);
$result = mysqli_stmt_get_result($stmt);

if ($row = mysqli_fetch_assoc($result)) {
    $filePath = '../' . $row['file_url'];
    if (file_exists($filePath)) {
        unlink($filePath);
    }
}

// Delete from database
$sql = "DELETE FROM exam_schedules WHERE schedule_type = ?";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "s", $schedule_type);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Schedule deleted');
} else {
    sendResponse(false, 'Failed to delete');
}

mysqli_close($conn);
?>