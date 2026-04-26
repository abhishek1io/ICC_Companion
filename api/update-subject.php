<?php
include 'config.php';

$subject_id = isset($_POST['subject_id']) ? intval($_POST['subject_id']) : 0;
$subject_code = isset($_POST['subject_code']) ? trim($_POST['subject_code']) : '';
$subject_name = isset($_POST['subject_name']) ? trim($_POST['subject_name']) : '';
$dept_code = isset($_POST['dept_code']) ? trim($_POST['dept_code']) : '';
$semester = isset($_POST['semester']) ? intval($_POST['semester']) : 0;

if (!$subject_id || empty($subject_code) || empty($subject_name) || empty($dept_code) || !$semester) {
    sendResponse(false, 'Please fill all required fields');
}

$sql = "UPDATE subjects SET subject_code = ?, subject_name = ?, dept_code = ?, semester = ? WHERE subject_id = ?";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "sssii", $subject_code, $subject_name, $dept_code, $semester, $subject_id);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Subject updated successfully');
} else {
    sendResponse(false, 'Error updating subject: ' . mysqli_error($conn));
}

mysqli_close($conn);
?>
