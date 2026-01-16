<?php
// =============================================
// ADD EXAM API (with attachment support)
// =============================================

include 'config.php';

// Get POST data
$subject_id = isset($_POST['subject_id']) ? intval($_POST['subject_id']) : 0;
$exam_date = isset($_POST['exam_date']) ? trim($_POST['exam_date']) : '';
$start_time = isset($_POST['start_time']) ? trim($_POST['start_time']) : '';
$end_time = isset($_POST['end_time']) ? trim($_POST['end_time']) : '';
$room = isset($_POST['room']) ? trim($_POST['room']) : '';
$exam_type = isset($_POST['exam_type']) ? trim($_POST['exam_type']) : 'final';
$attachment_url = '';

// Validate
if ($subject_id === 0 || empty($exam_date) || empty($start_time) || empty($end_time) || empty($room)) {
    sendResponse(false, 'Please fill all required fields');
}

// Handle file upload if present
if (isset($_FILES['attachment']) && $_FILES['attachment']['error'] === UPLOAD_ERR_OK) {
    $uploadDir = '../uploads/exams/';

    // Create directory if not exists
    if (!file_exists($uploadDir)) {
        mkdir($uploadDir, 0777, true);
    }

    // Get file info
    $fileName = $_FILES['attachment']['name'];
    $fileTmp = $_FILES['attachment']['tmp_name'];
    $fileExt = strtolower(pathinfo($fileName, PATHINFO_EXTENSION));

    // Allowed extensions
    $allowed = ['pdf', 'jpg', 'jpeg', 'png', 'doc', 'docx'];

    if (!in_array($fileExt, $allowed)) {
        sendResponse(false, 'Invalid file type. Allowed: PDF, JPG, PNG, DOC, DOCX');
    }

    // Generate unique filename
    $newFileName = 'exam_' . time() . '_' . rand(1000, 9999) . '.' . $fileExt;
    $uploadPath = $uploadDir . $newFileName;

    if (move_uploaded_file($fileTmp, $uploadPath)) {
        $attachment_url = 'uploads/exams/' . $newFileName;
    }
}

// Insert exam
$sql = "INSERT INTO exams (subject_id, exam_date, start_time, end_time, room, exam_type, attachment_url) 
        VALUES (?, ?, ?, ?, ?, ?, ?)";

$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "issssss", $subject_id, $exam_date, $start_time, $end_time, $room, $exam_type, $attachment_url);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Exam added successfully', [
        'exam_id' => mysqli_insert_id($conn)
    ]);
} else {
    sendResponse(false, 'Failed to add exam: ' . mysqli_error($conn));
}

mysqli_close($conn);
?>