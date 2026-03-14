<?php
error_reporting(0);
session_start();
include 'config.php';

// Get POST data
$username = isset($_POST['username']) ? trim($_POST['username']) : '';
$password = isset($_POST['password']) ? trim($_POST['password']) : '';

// Validate inputs
if (empty($username) || empty($password)) {
    sendResponse(false, 'Please enter username and password');
}

// Query database
$sql = "SELECT admin_id, username, password, name, role 
        FROM admins 
        WHERE username = ?";

$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "s", $username);
mysqli_stmt_execute($stmt);
$result = mysqli_stmt_get_result($stmt);

if ($row = mysqli_fetch_assoc($result)) {
    // Check if password matches (simple check - in production use password_hash)
    if ($row['password'] === $password) {
        // Login successful - set session
        $_SESSION['admin_id'] = $row['admin_id'];
        $_SESSION['admin_name'] = $row['name'];
        $_SESSION['admin_role'] = $row['role'];

        sendResponse(true, 'Login successful', [
            'admin_id' => $row['admin_id'],
            'name' => $row['name'],
            'role' => $row['role']
        ]);
    } else {
        sendResponse(false, 'Incorrect password');
    }
} else {
    sendResponse(false, 'Username not found');
}

mysqli_close($conn);
?>