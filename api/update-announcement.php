<?php
include 'config.php';

$announcement_id = isset($_POST['announcement_id']) ? intval($_POST['announcement_id']) : 0;
$title = isset($_POST['title']) ? trim($_POST['title']) : '';
$description = isset($_POST['description']) ? trim($_POST['description']) : '';
$priority = isset($_POST['priority']) ? trim($_POST['priority']) : 'medium';
$target_dept = isset($_POST['target_dept']) ? trim($_POST['target_dept']) : 'all';
$target_semester = isset($_POST['target_semester']) ? trim($_POST['target_semester']) : 'all';

$link_url = isset($_POST['link_url']) ? trim($_POST['link_url']) : '';

if (!$announcement_id || empty($title) || empty($description)) {
    sendResponse(false, 'Missing required data');
}

// Check if new attachment is uploaded
$attachment_url = null;
if (isset($_FILES['attachment']) && $_FILES['attachment']['error'] == 0) {
    $target_dir = "../uploads/announcements/";
    if (!file_exists($target_dir)) mkdir($target_dir, 0777, true);
    
    $file_ext = pathinfo($_FILES["attachment"]["name"], PATHINFO_EXTENSION);
    $file_name = "ann_" . time() . "_" . rand(1000, 9999) . "." . $file_ext;
    $target_file = $target_dir . $file_name;

    if (move_uploaded_file($_FILES["attachment"]["tmp_name"], $target_file)) {
        $attachment_url = "uploads/announcements/" . $file_name;
    }
}

if ($attachment_url) {
    $sql = "UPDATE announcements SET title = ?, description = ?, priority = ?, target_dept = ?, target_semester = ?, attachment_url = ?, link_url = ? WHERE announcement_id = ?";
    $stmt = mysqli_prepare($conn, $sql);
    mysqli_stmt_bind_param($stmt, "sssssssi", $title, $description, $priority, $target_dept, $target_semester, $attachment_url, $link_url, $announcement_id);
} else {
    $sql = "UPDATE announcements SET title = ?, description = ?, priority = ?, target_dept = ?, target_semester = ?, link_url = ? WHERE announcement_id = ?";
    $stmt = mysqli_prepare($conn, $sql);
    mysqli_stmt_bind_param($stmt, "ssssssi", $title, $description, $priority, $target_dept, $target_semester, $link_url, $announcement_id);
}

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Announcement updated successfully');
} else {
    sendResponse(false, 'Error updating announcement: ' . mysqli_error($conn));
}

mysqli_close($conn);
?>
