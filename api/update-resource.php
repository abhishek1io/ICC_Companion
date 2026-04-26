<?php
include 'config.php';

$resource_id = isset($_POST['resource_id']) ? intval($_POST['resource_id']) : 0;
$title = isset($_POST['title']) ? trim($_POST['title']) : '';
$description = isset($_POST['description']) ? trim($_POST['description']) : '';
$resource_type = isset($_POST['resource_type']) ? trim($_POST['resource_type']) : '';
$dept_code = isset($_POST['dept_code']) ? trim($_POST['dept_code']) : '';
$semester = isset($_POST['semester']) ? intval($_POST['semester']) : 0;
$subject_id = isset($_POST['subject_id']) ? intval($_POST['subject_id']) : null;
$link_url = isset($_POST['link_url']) ? trim($_POST['link_url']) : null;
$content_text = isset($_POST['content_text']) ? trim($_POST['content_text']) : null;

if (!$resource_id || empty($title) || empty($resource_type)) {
    sendResponse(false, 'Missing required fields');
}

// Handle file update if applicable
$file_url = null;
if (isset($_FILES['file']) && $_FILES['file']['error'] == 0) {
    $target_dir = "../uploads/resources/";
    if (!file_exists($target_dir)) mkdir($target_dir, 0777, true);
    
    $file_ext = pathinfo($_FILES["file"]["name"], PATHINFO_EXTENSION);
    $file_name = "res_" . time() . "_" . rand(1000, 9999) . "." . $file_ext;
    $target_file = $target_dir . $file_name;

    if (move_uploaded_file($_FILES["file"]["tmp_name"], $target_file)) {
        $file_url = "uploads/resources/" . $file_name;
    }
}

$sql = "UPDATE resources SET title = ?, description = ?, resource_type = ?, dept_code = ?, semester = ?, subject_id = ?, link_url = ?, content_text = ?";
$params = [$title, $description, $resource_type, $dept_code, $semester, $subject_id, $link_url, $content_text];
$types = "ssssiiss";

if ($file_url) {
    $sql .= ", file_url = ?";
    $params[] = $file_url;
    $types .= "s";
}

$sql .= " WHERE resource_id = ?";
$params[] = $resource_id;
$types .= "i";

$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, $types, ...$params);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Resource updated successfully');
} else {
    sendResponse(false, 'Error updating resource: ' . mysqli_error($conn));
}

mysqli_close($conn);
?>
