<?php
include 'config.php';

$dept_id = isset($_POST['dept_id']) ? intval($_POST['dept_id']) : 0;

if (!$dept_id) {
    sendResponse(false, 'Department ID is required');
}

// Check for dependencies first (students, subjects, etc.)
// For now, let's just try to delete and let the database foreign keys handle it or just delete.
// Usually better to warn the user.

$sql = "DELETE FROM departments WHERE dept_id = ?";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "i", $dept_id);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Department deleted successfully');
} else {
    sendResponse(false, 'Cannot delete department. It may have associated students or subjects.');
}

mysqli_close($conn);
?>
