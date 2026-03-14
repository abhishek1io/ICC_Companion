<?php
// =============================================
// UPLOAD EXAM SCHEDULE FILE API
// =============================================

include 'config.php';

$schedule_type = isset($_POST['schedule_type']) ? trim($_POST['schedule_type']) : '';
$dept_code = isset($_POST['dept_code']) ? trim($_POST['dept_code']) : '';
$semester = isset($_POST['semester']) ? intval($_POST['semester']) : 0;

if (empty($schedule_type) || !in_array($schedule_type, ['sessional', 'final'])) {
    sendResponse(false, 'Invalid schedule type');
}

if (empty($dept_code) || $semester <= 0) {
    sendResponse(false, 'Department and Semester are required');
}

// Handle file upload
if (!isset($_FILES['file']) || $_FILES['file']['error'] !== UPLOAD_ERR_OK) {
    sendResponse(false, 'Please upload a file');
}

$uploadDir = '../uploads/exam-schedules/';
if (!file_exists($uploadDir)) {
    mkdir($uploadDir, 0777, true);
}

$fileExt = strtolower(pathinfo($_FILES['file']['name'], PATHINFO_EXTENSION));
$allowed = ['pdf', 'jpg', 'jpeg', 'png'];

if (!in_array($fileExt, $allowed)) {
    sendResponse(false, 'Invalid file type. Allowed: PDF, JPG, PNG');
}

$newFileName = 'schedule_' . $schedule_type . '_' . $dept_code . '_sem' . $semester . '_' . time() . '.' . $fileExt;
$uploadPath = $uploadDir . $newFileName;

if (!move_uploaded_file($_FILES['file']['tmp_name'], $uploadPath)) {
    sendResponse(false, 'Failed to upload file');
}

$file_url = 'uploads/exam-schedules/' . $newFileName;

// Delete old schedule of same type, dept and sem first
$sql = "SELECT file_url FROM exam_schedules WHERE schedule_type = ? AND dept_code = ? AND semester = ?";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "ssi", $schedule_type, $dept_code, $semester);
mysqli_stmt_execute($stmt);
$result = mysqli_stmt_get_result($stmt);
if ($row = mysqli_fetch_assoc($result)) {
    $oldFile = '../' . $row['file_url'];
    if (file_exists($oldFile))
        unlink($oldFile);
}

// Delete old record
mysqli_query($conn, "DELETE FROM exam_schedules WHERE schedule_type = '$schedule_type' AND dept_code = '$dept_code' AND semester = $semester");

// Insert new
$sql = "INSERT INTO exam_schedules (schedule_type, file_url, dept_code, semester) VALUES (?, ?, ?, ?)";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "sssi", $schedule_type, $file_url, $dept_code, $semester);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Schedule uploaded', ['schedule_id' => mysqli_insert_id($conn)]);
} else {
    sendResponse(false, 'Database error: ' . mysqli_error($conn));
}

mysqli_close($conn);
?>