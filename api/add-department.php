<?php
include 'config.php';

$dept_code = isset($_POST['dept_code']) ? strtoupper(trim($_POST['dept_code'])) : '';
$dept_name = isset($_POST['dept_name']) ? trim($_POST['dept_name']) : '';
$max_semesters = isset($_POST['max_semesters']) ? intval($_POST['max_semesters']) : 6;

if (empty($dept_code) || empty($dept_name)) {
    sendResponse(false, 'Department code and name are required');
}

$sql = "INSERT INTO departments (dept_code, dept_name, max_semesters) VALUES (?, ?, ?)";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "ssi", $dept_code, $dept_name, $max_semesters);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Department added successfully');
} else {
    sendResponse(false, 'Failed to add department: ' . mysqli_error($conn));
}

mysqli_close($conn);
?>
