<?php
include 'config.php';

$item_id = isset($_POST['item_id']) ? intval($_POST['item_id']) : 0;
if (!$item_id) {
    sendResponse(false, 'Missing item ID');
}

$fields = [];
$params = [];
$types = "";

// Only update fields that are provided in POST
if (isset($_POST['title'])) { $fields[] = "title = ?"; $params[] = trim($_POST['title']); $types .= "s"; }
if (isset($_POST['description'])) { $fields[] = "description = ?"; $params[] = trim($_POST['description']); $types .= "s"; }
if (isset($_POST['item_type'])) { $fields[] = "item_type = ?"; $params[] = trim($_POST['item_type']); $types .= "s"; }
if (isset($_POST['contact_info'])) { $fields[] = "contact_info = ?"; $params[] = trim($_POST['contact_info']); $types .= "s"; }
if (isset($_POST['category'])) { $fields[] = "category = ?"; $params[] = trim($_POST['category']); $types .= "s"; }
if (isset($_POST['location'])) { $fields[] = "location = ?"; $params[] = trim($_POST['location']); $types .= "s"; }
if (isset($_POST['status'])) { $fields[] = "status = ?"; $params[] = trim($_POST['status']); $types .= "s"; }
if (isset($_POST['item_date'])) { $fields[] = "item_date = ?"; $params[] = trim($_POST['item_date']); $types .= "s"; }

// Handle image update
if (isset($_FILES['image']) && $_FILES['image']['error'] == 0) {
    $target_dir = "../uploads/lost_found/";
    if (!file_exists($target_dir)) mkdir($target_dir, 0777, true);
    
    $file_ext = pathinfo($_FILES["image"]["name"], PATHINFO_EXTENSION);
    $file_name = "lf_" . time() . "_" . rand(1000, 9999) . "." . $file_ext;
    $target_file = $target_dir . $file_name;

    if (move_uploaded_file($_FILES["image"]["tmp_name"], $target_file)) {
        $fields[] = "image_url = ?";
        $params[] = "uploads/lost_found/" . $file_name;
        $types .= "s";
    }
}

if (empty($fields)) {
    sendResponse(false, 'No fields to update');
}

$sql = "UPDATE lost_found SET " . implode(", ", $fields) . " WHERE item_id = ?";
$params[] = $item_id;
$types .= "i";

$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, $types, ...$params);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Item updated successfully');
} else {
    sendResponse(false, 'Error updating item: ' . mysqli_error($conn));
}

mysqli_close($conn);
?>