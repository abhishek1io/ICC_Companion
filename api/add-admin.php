<?php
error_reporting(0);
session_start();
include 'config.php';

$username = isset($_POST['username']) ? trim($_POST['username']) : '';
$password = isset($_POST['password']) ? trim($_POST['password']) : '';
$name = isset($_POST['name']) ? trim($_POST['name']) : '';
$role = isset($_POST['role']) ? trim($_POST['role']) : 'staff';

if (empty($username) || empty($password) || empty($name)) {
    sendResponse(false, 'Please fill all required fields');
}

// Check if username exists
$checkSql = "SELECT admin_id FROM admins WHERE username = ?";
$checkStmt = mysqli_prepare($conn, $checkSql);
mysqli_stmt_bind_param($checkStmt, "s", $username);
mysqli_stmt_execute($checkStmt);
if (mysqli_num_rows(mysqli_stmt_get_result($checkStmt)) > 0) {
    sendResponse(false, 'Username already exists');
}

$sql = "INSERT INTO admins (username, password, name, role) VALUES (?, ?, ?, ?)";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "ssss", $username, $password, $name, $role);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Staff member added successfully');
} else {
    sendResponse(false, 'Failed to add staff member: ' . mysqli_error($conn));
}

mysqli_close($conn);
?>
