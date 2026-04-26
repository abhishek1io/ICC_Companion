<?php
error_reporting(0);
include 'config.php';

$admin_id = isset($_GET['admin_id']) ? intval($_GET['admin_id']) : 0;

if ($admin_id <= 0) {
    sendResponse(false, 'Invalid Admin ID');
}

$sql = "SELECT fs.subject_id, s.subject_name, s.subject_code 
        FROM faculty_subjects fs
        JOIN subjects s ON fs.subject_id = s.subject_id
        WHERE fs.admin_id = ?";

$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "i", $admin_id);
mysqli_stmt_execute($stmt);
$result = mysqli_stmt_get_result($stmt);

$data = [];
while ($row = mysqli_fetch_assoc($result)) {
    $data[] = $row;
}

sendResponse(true, 'Data fetched', $data);

mysqli_close($conn);
?>
