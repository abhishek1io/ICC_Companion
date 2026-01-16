<?php
// =============================================
// ADD ROUTINE API
// =============================================

include 'config.php';

// Get POST data
$title = isset($_POST['title']) ? trim($_POST['title']) : '';
$description = isset($_POST['description']) ? trim($_POST['description']) : '';
$routine_type = isset($_POST['routine_type']) ? trim($_POST['routine_type']) : 'class';
$dept_code = isset($_POST['dept_code']) ? trim($_POST['dept_code']) : 'all';
$semester = isset($_POST['semester']) ? trim($_POST['semester']) : 'all';
$posted_by = isset($_POST['posted_by']) ? trim($_POST['posted_by']) : 'admin';
$file_url = '';

// Validate
if (empty($title)) {
    sendResponse(false, 'Title is required');
}

// Handle file upload (required)
if (!isset($_FILES['file']) || $_FILES['file']['error'] !== UPLOAD_ERR_OK) {
    sendResponse(false, 'Please upload a file');
}

$uploadDir = '../uploads/routines/';

// Create directory if not exists
if (!file_exists($uploadDir)) {
    mkdir($uploadDir, 0777, true);
}

// Get file info
$fileName = $_FILES['file']['name'];
$fileTmp = $_FILES['file']['tmp_name'];
$fileExt = strtolower(pathinfo($fileName, PATHINFO_EXTENSION));

// Allowed extensions
$allowed = ['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png'];

if (!in_array($fileExt, $allowed)) {
    sendResponse(false, 'Invalid file type. Allowed: PDF, DOC, DOCX, JPG, PNG');
}

// Check file size (max 10MB)
if ($_FILES['file']['size'] > 10 * 1024 * 1024) {
    sendResponse(false, 'File too large. Maximum 10MB allowed.');
}

// Generate unique filename
$newFileName = 'routine_' . $routine_type . '_' . time() . '_' . rand(1000, 9999) . '.' . $fileExt;
$uploadPath = $uploadDir . $newFileName;

if (!move_uploaded_file($fileTmp, $uploadPath)) {
    sendResponse(false, 'Failed to upload file');
}

$file_url = 'uploads/routines/' . $newFileName;

// Insert routine
$sql = "INSERT INTO routines (title, description, file_url, dept_code, semester, routine_type, posted_by) 
        VALUES (?, ?, ?, ?, ?, ?, ?)";

$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "sssssss", $title, $description, $file_url, $dept_code, $semester, $routine_type, $posted_by);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Routine uploaded successfully', [
        'routine_id' => mysqli_insert_id($conn)
    ]);
} else {
    sendResponse(false, 'Failed to save routine: ' . mysqli_error($conn));
}

mysqli_close($conn);
?>