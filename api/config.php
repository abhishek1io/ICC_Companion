<?php
// =============================================
// DATABASE CONFIGURATION
// ICON COMMERCE COLLEGE - Campus Portal
// =============================================

// Database credentials
$db_host = "localhost";
$db_user = "root";
$db_pass = "";  // Default XAMPP has no password
$db_name = "campus_portal";

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
    if (session_status() === PHP_SESSION_NONE) {
        session_start();
    }
    if (!isset($_SESSION['student_roll'])) {
        sendResponse(false, 'Please login first');
    }
    return $_SESSION['student_roll'];
}

function checkAdminLogin() {
    if (session_status() === PHP_SESSION_NONE) {
        session_start();
    }
    if (!isset($_SESSION['admin_id'])) {
        sendResponse(false, 'Admin login required');
    }
    return $_SESSION['admin_id'];
}

function getAdminScope() {
    if (session_status() === PHP_SESSION_NONE) {
        session_start();
    }
    return [
        'dept' => isset($_SESSION['assigned_dept']) ? $_SESSION['assigned_dept'] : 'all',
        'sem' => isset($_SESSION['assigned_semester']) ? $_SESSION['assigned_semester'] : 'all'
    ];
}
