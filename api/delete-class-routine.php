<?php
// =============================================
// DELETE CLASS ROUTINE API
// =============================================

include 'config.php';

$routine_id = isset($_POST['routine_id']) ? intval($_POST['routine_id']) : 0;

if ($routine_id === 0) {
    sendResponse(false, 'Invalid routine ID');
}

// Get file to delete
$sql = "SELECT file_url FROM class_routines WHERE routine_id = ?";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "i", $routine_id);
mysqli_stmt_execute($stmt);
$result = mysqli_stmt_get_result($stmt);

if ($row = mysqli_fetch_assoc($result)) {
    $filePath = '../' . $row['file_url'];
    if (file_exists($filePath)) {
        unlink($filePath);
    }
}

// Delete from database
$sql = "DELETE FROM class_routines WHERE routine_id = ?";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "i", $routine_id);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Routine deleted');
} else {
    sendResponse(false, 'Failed to delete');
}

mysqli_close($conn);
?>