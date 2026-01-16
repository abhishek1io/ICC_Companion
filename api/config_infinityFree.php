<?php
// =============================================
// DATABASE CONFIGURATION
// ICON COMMERCE COLLEGE - Campus Portal
// =============================================

// Database credentials
$db_host = "sql305.infinityfree.com";
$db_user = "if0_40921421";
$db_pass = "icc0000X";  // Default XAMPP has no password
$db_name = "if0_40921421_campus_portal";

// Create connection
$conn = mysqli_connect($db_host, $db_user, $db_pass, $db_name);

// Check connection
if (!$conn) {
    die(json_encode([
        'success' => false,
        'message' => 'Database connection failed: ' . mysqli_connect_error()
    ]));
}

// Set charset to handle special characters
mysqli_set_charset($conn, "utf8");

// Helper function to send JSON response
function sendResponse($success, $message, $data = null) {
    $response = [
        'success' => $success,
        'message' => $message
    ];
    if ($data !== null) {
        $response['data'] = $data;
    }
    echo json_encode($response);
    exit;
}

// Helper function to check if user is logged in (for protected APIs)
function checkStudentLogin() {
    session_start();
    if (!isset($_SESSION['student_roll'])) {
        sendResponse(false, 'Please login first');
    }
    return $_SESSION['student_roll'];
}

function checkAdminLogin() {
    session_start();
    if (!isset($_SESSION['admin_id'])) {
        sendResponse(false, 'Admin login required');
    }
    return $_SESSION['admin_id'];
}
?>
