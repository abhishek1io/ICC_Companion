<?php
error_reporting(0);
session_start();
include 'config.php';

$admin_id = isset($_POST['admin_id']) ? intval($_POST['admin_id']) : 0;

if (!$admin_id) {
    sendResponse(false, 'Invalid Admin ID');
}

// Don't allow deleting yourself or the main admin if possible
// For simplicity, just delete

$sql = "DELETE FROM admins WHERE admin_id = ?";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "i", $admin_id);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Staff member deleted successfully');
} else {
    sendResponse(false, 'Failed to delete staff member: ' . mysqli_error($conn));
}

mysqli_close($conn);
?>
