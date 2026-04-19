<?php
// =============================================
// SAVE RESOURCE API (Files, Links, or Text)
// =============================================

include 'config.php';

// Check admin login
$adminId = isset($_POST['admin_id']) ? $_POST['admin_id'] : '';
// In a real app, we would verify this against session/token

$title = isset($_POST['title']) ? trim($_POST['title']) : '';
$description = isset($_POST['description']) ? trim($_POST['description']) : '';
$resource_type = isset($_POST['resource_type']) ? trim($_POST['resource_type']) : '';
$dept_code = isset($_POST['dept_code']) ? trim($_POST['dept_code']) : '';
$semester = isset($_POST['semester']) ? trim($_POST['semester']) : '';
$subject_id = isset($_POST['subject_id']) && $_POST['subject_id'] !== '' ? intval($_POST['subject_id']) : null;
$posted_by = isset($_POST['posted_by']) ? trim($_POST['posted_by']) : 'admin';

if (empty($title) || empty($resource_type) || empty($dept_code) || empty($semester)) {
    sendResponse(false, 'Required fields missing: Title, Type, Dept, and Semester');
}

$file_url = null;
$link_url = isset($_POST['link_url']) ? trim($_POST['link_url']) : null;
$content_text = isset($_POST['content_text']) ? trim($_POST['content_text']) : null;

// Handle file upload if present and type is syllabus/book/material
if (isset($_FILES['file']) && $_FILES['file']['error'] === UPLOAD_ERR_OK) {
    if (in_array($resource_type, ['syllabus', 'book', 'material', 'others'])) {
        $uploadDir = '../uploads/resources/';
        if (!file_exists($uploadDir)) {
            mkdir($uploadDir, 0777, true);
        }

        $fileExt = strtolower(pathinfo($_FILES['file']['name'], PATHINFO_EXTENSION));
        $allowed = ['pdf', 'jpg', 'jpeg', 'png', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'zip', 'txt'];
        
        if (!in_array($fileExt, $allowed)) {
            sendResponse(false, 'Invalid file type. Allowed: PDF, Images, Office Docs, Zip');
        }

        $newFileName = 'res_' . $resource_type . '_' . time() . '_' . rand(1000, 9999) . '.' . $fileExt;
        $uploadPath = $uploadDir . $newFileName;

        if (move_uploaded_file($_FILES['file']['tmp_name'], $uploadPath)) {
            $file_url = 'uploads/resources/' . $newFileName;
        } else {
            sendResponse(false, 'Failed to save uploaded file');
        }
    }
}

// Insert into database
$sql = "INSERT INTO resources (title, description, resource_type, file_url, link_url, content_text, dept_code, semester, subject_id, posted_by) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "ssssssssis", $title, $description, $resource_type, $file_url, $link_url, $content_text, $dept_code, $semester, $subject_id, $posted_by);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Resource saved successfully', ['resource_id' => mysqli_insert_id($conn)]);
} else {
    // If we uploaded a file but DB failed, cleanup
    if ($file_url && file_exists('../' . $file_url)) {
        unlink('../' . $file_url);
    }
    sendResponse(false, 'Database error: ' . mysqli_error($conn));
}

mysqli_close($conn);
?>
