<?php
// =============================================
// ADD ANNOUNCEMENT API (with attachment support)
// =============================================

include 'config.php';

// Get POST data
$title = isset($_POST['title']) ? trim($_POST['title']) : '';
$description = isset($_POST['description']) ? trim($_POST['description']) : '';
$priority = isset($_POST['priority']) ? trim($_POST['priority']) : 'medium';
$target_dept = isset($_POST['target_dept']) ? trim($_POST['target_dept']) : 'all';
$target_semester = isset($_POST['target_semester']) ? trim($_POST['target_semester']) : 'all';
$posted_by = isset($_POST['posted_by']) ? trim($_POST['posted_by']) : 'admin';
$attachment_url = '';

// Validate
if (empty($title) || empty($description)) {
    sendResponse(false, 'Title and description are required');
}

// Handle file upload if present
if (isset($_FILES['attachment']) && $_FILES['attachment']['error'] === UPLOAD_ERR_OK) {
    $uploadDir = '../uploads/announcements/';

    // Create directory if not exists
    if (!file_exists($uploadDir)) {
        mkdir($uploadDir, 0777, true);
    }

    // Get file info
    $fileName = $_FILES['attachment']['name'];
    $fileTmp = $_FILES['attachment']['tmp_name'];
    $fileExt = strtolower(pathinfo($fileName, PATHINFO_EXTENSION));

    // Allowed extensions
    $allowed = ['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png'];

    if (!in_array($fileExt, $allowed)) {
        sendResponse(false, 'Invalid file type. Allowed: PDF, DOC, DOCX, JPG, PNG');
    }

    // Generate unique filename
    $newFileName = 'announcement_' . time() . '_' . rand(1000, 9999) . '.' . $fileExt;
    $uploadPath = $uploadDir . $newFileName;

    if (move_uploaded_file($fileTmp, $uploadPath)) {
        $attachment_url = 'uploads/announcements/' . $newFileName;
    }
}

// Insert announcement
$sql = "INSERT INTO announcements (title, description, attachment_url, priority, target_dept, target_semester, posted_by) 
        VALUES (?, ?, ?, ?, ?, ?, ?)";

$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "sssssss", $title, $description, $attachment_url, $priority, $target_dept, $target_semester, $posted_by);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Announcement posted successfully', [
        'announcement_id' => mysqli_insert_id($conn)
    ]);
} else {
    sendResponse(false, 'Failed to post announcement: ' . mysqli_error($conn));
}

mysqli_close($conn);
?>