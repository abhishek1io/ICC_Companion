<?php
// =============================================
// DELETE ROUTINE API
// =============================================

include 'config.php';

// Get POST data
$routine_id = isset($_POST['routine_id']) ? intval($_POST['routine_id']) : 0;

// Validate
if ($routine_id === 0) {
    sendResponse(false, 'Invalid routine ID');
}

// Get file path to delete
$sql = "SELECT file_url FROM routines WHERE routine_id = ?";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "i", $routine_id);
mysqli_stmt_execute($stmt);
$result = mysqli_stmt_get_result($stmt);
$row = mysqli_fetch_assoc($result);

if ($row && !empty($row['file_url'])) {
    $filePath = '../' . $row['file_url'];
    if (file_exists($filePath)) {
        unlink($filePath); // Delete the file
    }
}

// Delete from database
$sql = "DELETE FROM routines WHERE routine_id = ?";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "i", $routine_id);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Routine deleted successfully');
} else {
    sendResponse(false, 'Failed to delete routine');
}

mysqli_close($conn);
?>