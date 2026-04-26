<?php
error_reporting(0);
include 'config.php';

$admin_id = isset($_POST['admin_id']) ? intval($_POST['admin_id']) : 0;
$subject_ids_json = isset($_POST['subject_ids']) ? $_POST['subject_ids'] : '[]';
$subject_ids = json_decode($subject_ids_json, true);

if ($admin_id <= 0) {
    sendResponse(false, 'Invalid Admin ID');
}

// 1. Clear existing assignments
$sql_delete = "DELETE FROM faculty_subjects WHERE admin_id = ?";
$stmt_del = mysqli_prepare($conn, $sql_delete);
mysqli_stmt_bind_param($stmt_del, "i", $admin_id);
mysqli_stmt_execute($stmt_del);

// 2. Insert new assignments
if (!empty($subject_ids)) {
    $sql_insert = "INSERT INTO faculty_subjects (admin_id, subject_id) VALUES (?, ?)";
    $stmt_ins = mysqli_prepare($conn, $sql_insert);
    
    foreach ($subject_ids as $sid) {
        $sid = intval($sid);
        mysqli_stmt_bind_param($stmt_ins, "ii", $admin_id, $sid);
        mysqli_stmt_execute($stmt_ins);
    }
}

sendResponse(true, 'Assignments updated successfully');

mysqli_close($conn);
?>
