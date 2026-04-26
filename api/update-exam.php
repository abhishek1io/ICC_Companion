<?php
include 'config.php';

$exam_id = isset($_POST['exam_id']) ? intval($_POST['exam_id']) : 0;
$subject_id = isset($_POST['subject_id']) ? intval($_POST['subject_id']) : 0;
$exam_date = isset($_POST['exam_date']) ? trim($_POST['exam_date']) : '';
$start_time = isset($_POST['start_time']) ? trim($_POST['start_time']) : '';
$end_time = isset($_POST['end_time']) ? trim($_POST['end_time']) : '';
$room = isset($_POST['room']) ? trim($_POST['room']) : '';
$exam_type = isset($_POST['exam_type']) ? trim($_POST['exam_type']) : 'sessional';

if (!$exam_id || !$subject_id || empty($exam_date) || empty($start_time) || empty($end_time) || empty($room)) {
    sendResponse(false, 'Please fill all required fields');
}

$sql = "UPDATE exams SET subject_id = ?, exam_date = ?, start_time = ?, end_time = ?, room = ?, exam_type = ? WHERE exam_id = ?";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "isssssi", $subject_id, $exam_date, $start_time, $end_time, $room, $exam_type, $exam_id);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Exam updated successfully');
} else {
    sendResponse(false, 'Error updating exam: ' . mysqli_error($conn));
}

mysqli_close($conn);
?>
