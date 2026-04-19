<?php
// =============================================
// DELETE RESOURCE API
// =============================================

include 'config.php';

// Check admin login (simulated check)
// In real app: checkAdminLogin();

$resource_id = isset($_POST['resource_id']) ? intval($_POST['resource_id']) : 0;

if ($resource_id <= 0) {
    sendResponse(false, 'Invalid resource ID');
}

// Get file URL to delete from disk if it exists
$sql = "SELECT file_url FROM resources WHERE resource_id = ?";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "i", $resource_id);
mysqli_stmt_execute($stmt);
$result = mysqli_stmt_get_result($stmt);

if ($row = mysqli_fetch_assoc($result)) {
    if (!empty($row['file_url'])) {
        $filePath = '../' . $row['file_url'];
        if (file_exists($filePath)) {
            unlink($filePath);
        }
    }
}

// Delete from database
$sql = "DELETE FROM resources WHERE resource_id = ?";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "i", $resource_id);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Resource deleted successfully');
} else {
    sendResponse(false, 'Database error: ' . mysqli_error($conn));
}

mysqli_close($conn);
?>
