<?php
// =============================================
// DELETE ANNOUNCEMENT API
// =============================================

include 'config.php';

$announcement_id = isset($_POST['announcement_id']) ? intval($_POST['announcement_id']) : 0;

if ($announcement_id === 0) {
    sendResponse(false, 'Announcement ID is required');
}

$sql = "DELETE FROM announcements WHERE announcement_id = ?";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "i", $announcement_id);

if (mysqli_stmt_execute($stmt)) {
    if (mysqli_stmt_affected_rows($stmt) > 0) {
        sendResponse(true, 'Announcement deleted successfully');
    } else {
        sendResponse(false, 'Announcement not found');
    }
} else {
    sendResponse(false, 'Failed to delete announcement');
}

mysqli_close($conn);
?>