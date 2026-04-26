<?php
include 'config.php';

$dept_id = isset($_POST['dept_id']) ? intval($_POST['dept_id']) : 0;
$dept_code = isset($_POST['dept_code']) ? strtoupper(trim($_POST['dept_code'])) : '';
$dept_name = isset($_POST['dept_name']) ? trim($_POST['dept_name']) : '';
$max_semesters = isset($_POST['max_semesters']) ? intval($_POST['max_semesters']) : 6;

if (!$dept_id || empty($dept_code) || empty($dept_name)) {
    sendResponse(false, 'Missing required data');
}

$sql = "UPDATE departments SET dept_code = ?, dept_name = ?, max_semesters = ? WHERE dept_id = ?";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "ssii", $dept_code, $dept_name, $max_semesters, $dept_id);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Department updated successfully');
} else {
    sendResponse(false, 'Failed to update department: ' . mysqli_error($conn));
}

mysqli_close($conn);
?>
