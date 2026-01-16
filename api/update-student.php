<?php
// =============================================
// UPDATE STUDENT API
// =============================================

include 'config.php';

// Get POST data
$student_id = isset($_POST['student_id']) ? intval($_POST['student_id']) : 0;
$name = isset($_POST['name']) ? trim($_POST['name']) : '';
$dob = isset($_POST['dob']) ? trim($_POST['dob']) : '';
$dept_code = isset($_POST['dept_code']) ? trim($_POST['dept_code']) : '';
$semester = isset($_POST['semester']) ? intval($_POST['semester']) : 0;
$email = isset($_POST['email']) ? trim($_POST['email']) : '';
$phone = isset($_POST['phone']) ? trim($_POST['phone']) : '';

// Validate
if ($student_id === 0 || empty($name) || empty($dob) || empty($dept_code) || $semester === 0) {
    sendResponse(false, 'Please fill all required fields');
}

// Update student
$sql = "UPDATE students SET 
            name = ?, 
            dob = ?, 
            dept_code = ?, 
            semester = ?, 
            email = ?, 
            phone = ? 
        WHERE student_id = ?";

$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "sssissi", $name, $dob, $dept_code, $semester, $email, $phone, $student_id);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Student updated successfully');
} else {
    sendResponse(false, 'Failed to update student: ' . mysqli_error($conn));
}

mysqli_close($conn);
?>