<?php
// =============================================
// DELETE LOST/FOUND ITEM API
// =============================================

include 'config.php';

$item_id = isset($_POST['item_id']) ? intval($_POST['item_id']) : 0;

if ($item_id === 0) {
    sendResponse(false, 'Item ID is required');
}

$sql = "DELETE FROM lost_found WHERE item_id = ?";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "i", $item_id);

if (mysqli_stmt_execute($stmt)) {
    if (mysqli_stmt_affected_rows($stmt) > 0) {
        sendResponse(true, 'Item deleted successfully');
    } else {
        sendResponse(false, 'Item not found');
    }
} else {
    sendResponse(false, 'Failed to delete item');
}

mysqli_close($conn);
?>