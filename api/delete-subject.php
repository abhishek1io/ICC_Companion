<?php
// =============================================
// DELETE SUBJECT API
// =============================================

include 'config.php';

// Check admin login
checkAdminLogin();

// Get POST data
$subject_id = isset($_POST['subject_id']) ? intval($_POST['subject_id']) : 0;

if ($subject_id === 0) {
    sendResponse(false, 'Subject ID is required');
}

// Delete subject
$sql = "DELETE FROM subjects WHERE subject_id = ?";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "i", $subject_id);

if (mysqli_stmt_execute($stmt)) {
    if (mysqli_stmt_affected_rows($stmt) > 0) {
        sendResponse(true, 'Subject deleted successfully');
    } else {
        sendResponse(false, 'Subject not found');
    }
} else {
    sendResponse(false, 'Failed to delete subject: ' . mysqli_error($conn));
}

mysqli_close($conn);
?>
