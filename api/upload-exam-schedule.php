<?php
// =============================================
// UPLOAD EXAM SCHEDULE FILE API
// =============================================

include 'config.php';

$schedule_type = isset($_POST['schedule_type']) ? trim($_POST['schedule_type']) : '';

if (empty($schedule_type) || !in_array($schedule_type, ['sessional', 'final'])) {
    sendResponse(false, 'Invalid schedule type');
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

$newFileName = 'schedule_' . $schedule_type . '_' . time() . '.' . $fileExt;
$uploadPath = $uploadDir . $newFileName;

if (!move_uploaded_file($_FILES['file']['tmp_name'], $uploadPath)) {
    sendResponse(false, 'Failed to upload file');
}

$file_url = 'uploads/exam-schedules/' . $newFileName;

// Delete old schedule of same type first
$sql = "SELECT file_url FROM exam_schedules WHERE schedule_type = ?";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "s", $schedule_type);
mysqli_stmt_execute($stmt);
$result = mysqli_stmt_get_result($stmt);
if ($row = mysqli_fetch_assoc($result)) {
    $oldFile = '../' . $row['file_url'];
    if (file_exists($oldFile))
        unlink($oldFile);
}

// Delete old record
mysqli_query($conn, "DELETE FROM exam_schedules WHERE schedule_type = '$schedule_type'");

// Insert new
$sql = "INSERT INTO exam_schedules (schedule_type, file_url) VALUES (?, ?)";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "ss", $schedule_type, $file_url);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Schedule uploaded', ['schedule_id' => mysqli_insert_id($conn)]);
} else {
    sendResponse(false, 'Database error');
}

mysqli_close($conn);
?>