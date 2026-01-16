<?php
// =============================================
// ADD ANNOUNCEMENT API
// =============================================

include 'config.php';

// Get POST data
$title = isset($_POST['title']) ? trim($_POST['title']) : '';
$description = isset($_POST['description']) ? trim($_POST['description']) : '';
$priority = isset($_POST['priority']) ? trim($_POST['priority']) : 'medium';
$target_dept = isset($_POST['target_dept']) ? trim($_POST['target_dept']) : 'all';
$target_semester = isset($_POST['target_semester']) ? trim($_POST['target_semester']) : 'all';
$posted_by = isset($_POST['posted_by']) ? trim($_POST['posted_by']) : 'admin';

// Validate
if (empty($title) || empty($description)) {
    sendResponse(false, 'Title and description are required');
}

// Insert announcement
$sql = "INSERT INTO announcements (title, description, priority, target_dept, target_semester, posted_by) 
        VALUES (?, ?, ?, ?, ?, ?)";

$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "ssssss", $title, $description, $priority, $target_dept, $target_semester, $posted_by);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Announcement posted successfully', [
        'announcement_id' => mysqli_insert_id($conn)
    ]);
} else {
    sendResponse(false, 'Failed to post announcement: ' . mysqli_error($conn));
}

mysqli_close($conn);
?>