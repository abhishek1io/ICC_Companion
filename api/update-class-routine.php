<?php
include 'config.php';

$routine_id = isset($_POST['routine_id']) ? intval($_POST['routine_id']) : 0;
$title = isset($_POST['title']) ? trim($_POST['title']) : '';
$dept_code = isset($_POST['dept_code']) ? trim($_POST['dept_code']) : '';
$semester = isset($_POST['semester']) ? intval($_POST['semester']) : 0;

if (!$routine_id || empty($title) || empty($dept_code) || !$semester) {
    sendResponse(false, 'Missing required data');
}

// Handle file update
$file_url = null;
if (isset($_FILES['file']) && $_FILES['file']['error'] == 0) {
    $target_dir = "../uploads/routines/";
    if (!file_exists($target_dir)) mkdir($target_dir, 0777, true);
    
    $file_ext = pathinfo($_FILES["file"]["name"], PATHINFO_EXTENSION);
    $file_name = "rot_" . time() . "_" . rand(1000, 9999) . "." . $file_ext;
    $target_file = $target_dir . $file_name;

    if (move_uploaded_file($_FILES["file"]["tmp_name"], $target_file)) {
        $file_url = "uploads/routines/" . $file_name;
    }
}

if ($file_url) {
    $sql = "UPDATE class_routines SET title = ?, dept_code = ?, semester = ?, file_url = ? WHERE routine_id = ?";
    $stmt = mysqli_prepare($conn, $sql);
    mysqli_stmt_bind_param($stmt, "ssisi", $title, $dept_code, $semester, $file_url, $routine_id);
} else {
    $sql = "UPDATE class_routines SET title = ?, dept_code = ?, semester = ? WHERE routine_id = ?";
    $stmt = mysqli_prepare($conn, $sql);
    mysqli_stmt_bind_param($stmt, "ssii", $title, $dept_code, $semester, $routine_id);
}

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Routine updated successfully');
} else {
    sendResponse(false, 'Error updating routine: ' . mysqli_error($conn));
}

mysqli_close($conn);
?>
