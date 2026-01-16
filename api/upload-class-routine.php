<?php
// =============================================
// UPLOAD CLASS ROUTINE API
// =============================================

include 'config.php';

$title = isset($_POST['title']) ? trim($_POST['title']) : '';
$dept_code = isset($_POST['dept_code']) ? trim($_POST['dept_code']) : '';
$semester = isset($_POST['semester']) ? trim($_POST['semester']) : '';

if (empty($title) || empty($dept_code) || empty($semester)) {
    sendResponse(false, 'Title, department and semester are required');
}

// Handle file upload
if (!isset($_FILES['file']) || $_FILES['file']['error'] !== UPLOAD_ERR_OK) {
    sendResponse(false, 'Please upload a file');
}

$uploadDir = '../uploads/routines/';
if (!file_exists($uploadDir)) {
    mkdir($uploadDir, 0777, true);
}

$fileExt = strtolower(pathinfo($_FILES['file']['name'], PATHINFO_EXTENSION));
$allowed = ['pdf', 'jpg', 'jpeg', 'png'];

if (!in_array($fileExt, $allowed)) {
    sendResponse(false, 'Invalid file type. Allowed: PDF, JPG, PNG');
}

$newFileName = 'routine_' . $dept_code . '_sem' . $semester . '_' . time() . '.' . $fileExt;
$uploadPath = $uploadDir . $newFileName;

if (!move_uploaded_file($_FILES['file']['tmp_name'], $uploadPath)) {
    sendResponse(false, 'Failed to upload file');
}

$file_url = 'uploads/routines/' . $newFileName;

// Insert new routine
$sql = "INSERT INTO class_routines (title, file_url, dept_code, semester) VALUES (?, ?, ?, ?)";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "ssss", $title, $file_url, $dept_code, $semester);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Routine uploaded', ['routine_id' => mysqli_insert_id($conn)]);
} else {
    sendResponse(false, 'Database error');
}

mysqli_close($conn);
?>