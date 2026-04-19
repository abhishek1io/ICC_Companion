<?php
// =============================================
// ADD SUBJECT API
// =============================================

include 'config.php';

// Check admin login
checkAdminLogin();

// Get POST data
$subject_code = isset($_POST['subject_code']) ? strtoupper(trim($_POST['subject_code'])) : '';
$subject_name = isset($_POST['subject_name']) ? trim($_POST['subject_name']) : '';
$dept_code = isset($_POST['dept_code']) ? strtoupper(trim($_POST['dept_code'])) : '';
$semester = isset($_POST['semester']) ? intval($_POST['semester']) : 0;

// Validate required fields
if (empty($subject_code) || empty($subject_name) || empty($dept_code) || $semester === 0) {
    sendResponse(false, 'Please fill all required fields');
}

// Check if subject code already exists for this dept/sem
$checkSql = "SELECT subject_id FROM subjects WHERE subject_code = ? AND dept_code = ?";
$checkStmt = mysqli_prepare($conn, $checkSql);
mysqli_stmt_bind_param($checkStmt, "ss", $subject_code, $dept_code);
mysqli_stmt_execute($checkStmt);
$checkResult = mysqli_stmt_get_result($checkStmt);

if (mysqli_fetch_assoc($checkResult)) {
    sendResponse(false, 'Subject code already exists for this department');
}

// Insert subject
$sql = "INSERT INTO subjects (subject_code, subject_name, dept_code, semester) 
        VALUES (?, ?, ?, ?)";

$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "sssi", $subject_code, $subject_name, $dept_code, $semester);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Subject added successfully', [
        'subject_id' => mysqli_insert_id($conn)
    ]);
} else {
    sendResponse(false, 'Failed to add subject: ' . mysqli_error($conn));
}

mysqli_close($conn);
?>
