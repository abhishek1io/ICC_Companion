<?php
// =============================================
// SAVE ATTENDANCE API
// =============================================

include 'config.php';

// Get POST data
$subject_id = isset($_POST['subject_id']) ? intval($_POST['subject_id']) : 0;
$date = isset($_POST['date']) ? trim($_POST['date']) : '';
$attendance_json = isset($_POST['attendance']) ? $_POST['attendance'] : '';
$marked_by = isset($_POST['marked_by']) ? trim($_POST['marked_by']) : 'admin';

// Validate
if ($subject_id === 0 || empty($date) || empty($attendance_json)) {
    sendResponse(false, 'Subject, date, and attendance data are required');
}

// Parse attendance data
$attendance = json_decode($attendance_json, true);
if (!is_array($attendance)) {
    sendResponse(false, 'Invalid attendance data');
}

// Start transaction
mysqli_begin_transaction($conn);

try {
    // First, delete existing attendance for this date and subject
    $deleteSql = "DELETE FROM attendance WHERE subject_id = ? AND attendance_date = ?";
    $deleteStmt = mysqli_prepare($conn, $deleteSql);
    mysqli_stmt_bind_param($deleteStmt, "is", $subject_id, $date);
    mysqli_stmt_execute($deleteStmt);

    // Insert new attendance records
    $insertSql = "INSERT INTO attendance (roll_number, subject_id, attendance_date, status, marked_by) 
                  VALUES (?, ?, ?, ?, ?)";
    $insertStmt = mysqli_prepare($conn, $insertSql);

    foreach ($attendance as $record) {
        $roll = $record['roll_number'];
        $status = $record['status'];

        mysqli_stmt_bind_param($insertStmt, "sisss", $roll, $subject_id, $date, $status, $marked_by);
        mysqli_stmt_execute($insertStmt);
    }

    mysqli_commit($conn);
    sendResponse(true, 'Attendance saved successfully', [
        'records' => count($attendance)
    ]);

} catch (Exception $e) {
    mysqli_rollback($conn);
    sendResponse(false, 'Failed to save attendance: ' . $e->getMessage());
}

mysqli_close($conn);
?>