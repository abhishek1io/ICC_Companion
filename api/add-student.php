<?php
// =============================================
// ADD STUDENT API
// =============================================

include 'config.php';

// Get POST data
$roll_number = isset($_POST['roll_number']) ? strtoupper(trim($_POST['roll_number'])) : '';
$name = isset($_POST['name']) ? trim($_POST['name']) : '';
$dob = isset($_POST['dob']) ? trim($_POST['dob']) : '';
$dept_code = isset($_POST['dept_code']) ? trim($_POST['dept_code']) : '';
$semester = isset($_POST['semester']) ? intval($_POST['semester']) : 0;
$email = isset($_POST['email']) ? trim($_POST['email']) : '';
$phone = isset($_POST['phone']) ? trim($_POST['phone']) : '';

// Validate required fields
if (empty($roll_number) || empty($name) || empty($dob) || empty($dept_code) || $semester === 0) {
    sendResponse(false, 'Please fill all required fields');
}

// Check if roll number already exists
$checkSql = "SELECT student_id FROM students WHERE roll_number = ?";
$checkStmt = mysqli_prepare($conn, $checkSql);
mysqli_stmt_bind_param($checkStmt, "s", $roll_number);
mysqli_stmt_execute($checkStmt);
$checkResult = mysqli_stmt_get_result($checkStmt);

if (mysqli_fetch_assoc($checkResult)) {
    sendResponse(false, 'Roll number already exists');
}

// Insert student
$sql = "INSERT INTO students (roll_number, name, dob, dept_code, semester, email, phone) 
        VALUES (?, ?, ?, ?, ?, ?, ?)";

$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "ssssiss", $roll_number, $name, $dob, $dept_code, $semester, $email, $phone);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Student added successfully', [
        'student_id' => mysqli_insert_id($conn),
        'roll_number' => $roll_number
    ]);
} else {
    sendResponse(false, 'Failed to add student: ' . mysqli_error($conn));
}

mysqli_close($conn);
?>