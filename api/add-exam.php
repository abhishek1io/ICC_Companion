<?php
// =============================================
// ADD EXAM API
// =============================================

include 'config.php';

// Get POST data
$subject_id = isset($_POST['subject_id']) ? intval($_POST['subject_id']) : 0;
$exam_date = isset($_POST['exam_date']) ? trim($_POST['exam_date']) : '';
$start_time = isset($_POST['start_time']) ? trim($_POST['start_time']) : '';
$end_time = isset($_POST['end_time']) ? trim($_POST['end_time']) : '';
$room = isset($_POST['room']) ? trim($_POST['room']) : '';
$exam_type = isset($_POST['exam_type']) ? trim($_POST['exam_type']) : 'end-term';

// Validate
if ($subject_id === 0 || empty($exam_date) || empty($start_time) || empty($end_time) || empty($room)) {
    sendResponse(false, 'Please fill all required fields');
}

// Insert exam
$sql = "INSERT INTO exams (subject_id, exam_date, start_time, end_time, room, exam_type) 
        VALUES (?, ?, ?, ?, ?, ?)";

$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "isssss", $subject_id, $exam_date, $start_time, $end_time, $room, $exam_type);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Exam added successfully', [
        'exam_id' => mysqli_insert_id($conn)
    ]);
} else {
    sendResponse(false, 'Failed to add exam: ' . mysqli_error($conn));
}

mysqli_close($conn);
?>