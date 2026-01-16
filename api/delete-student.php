<?php
// =============================================
// DELETE STUDENT API
// =============================================

include 'config.php';

// Get POST data
$roll_number = isset($_POST['roll_number']) ? trim($_POST['roll_number']) : '';

if (empty($roll_number)) {
    sendResponse(false, 'Roll number is required');
}

// First delete attendance records
$delAttendance = "DELETE FROM attendance WHERE roll_number = ?";
$stmt1 = mysqli_prepare($conn, $delAttendance);
mysqli_stmt_bind_param($stmt1, "s", $roll_number);
mysqli_stmt_execute($stmt1);

// Then delete student
$sql = "DELETE FROM students WHERE roll_number = ?";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "s", $roll_number);

if (mysqli_stmt_execute($stmt)) {
    if (mysqli_stmt_affected_rows($stmt) > 0) {
        sendResponse(true, 'Student deleted successfully');
    } else {
        sendResponse(false, 'Student not found');
    }
} else {
    sendResponse(false, 'Failed to delete student: ' . mysqli_error($conn));
}

mysqli_close($conn);
?>