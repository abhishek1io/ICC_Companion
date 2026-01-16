<?php
// =============================================
// UPDATE LOST/FOUND ITEM API
// =============================================

include 'config.php';

$item_id = isset($_POST['item_id']) ? intval($_POST['item_id']) : 0;
$status = isset($_POST['status']) ? trim($_POST['status']) : '';

if ($item_id === 0) {
    sendResponse(false, 'Item ID is required');
}

$sql = "UPDATE lost_found SET status = ?, claimed_date = CURDATE() WHERE item_id = ?";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "si", $status, $item_id);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Item updated successfully');
} else {
    sendResponse(false, 'Failed to update item');
}

mysqli_close($conn);
?>