<?php
// =============================================
// STUDENT LOGIN API
// =============================================

session_start();
include 'config.php';

// Get POST data
$roll_number = isset($_POST['roll_number']) ? trim($_POST['roll_number']) : '';
$dob = isset($_POST['dob']) ? trim($_POST['dob']) : '';

// Validate inputs
if (empty($roll_number) || empty($dob)) {
    sendResponse(false, 'Please enter roll number and date of birth');
}

// Convert roll number to uppercase
$roll_number = strtoupper($roll_number);

// Query database
$sql = "SELECT student_id, roll_number, name, dob, email, phone, dept_code, semester 
        FROM students 
        WHERE roll_number = ?";

$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "s", $roll_number);
mysqli_stmt_execute($stmt);
$result = mysqli_stmt_get_result($stmt);

if ($row = mysqli_fetch_assoc($result)) {
    // Check if DOB matches
    if ($row['dob'] === $dob) {
        // Login successful - set session
        $_SESSION['student_roll'] = $row['roll_number'];
        $_SESSION['student_name'] = $row['name'];
        $_SESSION['student_dept'] = $row['dept_code'];
        $_SESSION['student_semester'] = $row['semester'];

        sendResponse(true, 'Login successful', [
            'roll_number' => $row['roll_number'],
            'name' => $row['name'],
            'dept_code' => $row['dept_code'],
            'semester' => $row['semester'],
            'email' => $row['email']
        ]);
    } else {
        sendResponse(false, 'Date of birth does not match our records');
    }
} else {
    sendResponse(false, 'Roll number not found');
}

mysqli_close($conn);
?>