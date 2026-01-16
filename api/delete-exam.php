<?php
// =============================================
// DELETE EXAM API
// =============================================

include 'config.php';

$exam_id = isset($_POST['exam_id']) ? intval($_POST['exam_id']) : 0;

if ($exam_id === 0) {
    sendResponse(false, 'Exam ID is required');
}

$sql = "DELETE FROM exams WHERE exam_id = ?";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "i", $exam_id);

if (mysqli_stmt_execute($stmt)) {
    if (mysqli_stmt_affected_rows($stmt) > 0) {
        sendResponse(true, 'Exam deleted successfully');
    } else {
        sendResponse(false, 'Exam not found');
    }
} else {
    sendResponse(false, 'Failed to delete exam');
}

mysqli_close($conn);
?>