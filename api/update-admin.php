<?php
error_reporting(0);
session_start();
include 'config.php';

$admin_id = isset($_POST['admin_id']) ? intval($_POST['admin_id']) : 0;
$username = isset($_POST['username']) ? trim($_POST['username']) : '';
$password = isset($_POST['password']) ? trim($_POST['password']) : '';
$name = isset($_POST['name']) ? trim($_POST['name']) : '';
$role = isset($_POST['role']) ? trim($_POST['role']) : 'staff';

if (!$admin_id || empty($username) || empty($name)) {
    sendResponse(false, 'Missing required data');
}

if (!empty($password)) {
    $sql = "UPDATE admins SET username = ?, password = ?, name = ?, role = ? WHERE admin_id = ?";
    $stmt = mysqli_prepare($conn, $sql);
    mysqli_stmt_bind_param($stmt, "ssssi", $username, $password, $name, $role, $admin_id);
} else {
    $sql = "UPDATE admins SET username = ?, name = ?, role = ? WHERE admin_id = ?";
    $stmt = mysqli_prepare($conn, $sql);
    mysqli_stmt_bind_param($stmt, "sssi", $username, $name, $role, $admin_id);
}

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Staff member updated successfully');
} else {
    sendResponse(false, 'Failed to update staff member: ' . mysqli_error($conn));
}

mysqli_close($conn);
?>
