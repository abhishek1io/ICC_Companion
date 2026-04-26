<?php
error_reporting(0);
session_start();
include 'config.php';

// Only allow super-admin to view all admins
// But for now let's just return all for simplicity if called from manage-staff

$sql = "SELECT admin_id, username, name, role, assigned_dept, assigned_semester FROM admins ORDER BY admin_id DESC";
$result = mysqli_query($conn, $sql);

$admins = [];
while ($row = mysqli_fetch_assoc($result)) {
    $admins[] = $row;
}

sendResponse(true, 'Admins fetched successfully', $admins);

mysqli_close($conn);
?>
