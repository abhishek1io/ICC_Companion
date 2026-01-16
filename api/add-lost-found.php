<?php
// =============================================
// ADD LOST/FOUND ITEM API
// =============================================

include 'config.php';

// Get POST data
$title = isset($_POST['title']) ? trim($_POST['title']) : '';
$item_type = isset($_POST['item_type']) ? trim($_POST['item_type']) : '';
$category = isset($_POST['category']) ? trim($_POST['category']) : 'other';
$location = isset($_POST['location']) ? trim($_POST['location']) : '';
$item_date = isset($_POST['item_date']) ? trim($_POST['item_date']) : date('Y-m-d');
$description = isset($_POST['description']) ? trim($_POST['description']) : '';
$contact_info = isset($_POST['contact_info']) ? trim($_POST['contact_info']) : '';
$posted_by = isset($_POST['posted_by']) ? trim($_POST['posted_by']) : 'admin';

// Validate
if (empty($title) || empty($item_type) || empty($location) || empty($contact_info)) {
    sendResponse(false, 'Please fill all required fields');
}

// Insert item
$sql = "INSERT INTO lost_found (title, item_type, category, location, item_date, description, contact_info, posted_by, status) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'active')";

$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "ssssssss", $title, $item_type, $category, $location, $item_date, $description, $contact_info, $posted_by);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Item added successfully', [
        'item_id' => mysqli_insert_id($conn)
    ]);
} else {
    sendResponse(false, 'Failed to add item: ' . mysqli_error($conn));
}

mysqli_close($conn);
?>