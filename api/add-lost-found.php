<?php
// =============================================
// ADD LOST/FOUND ITEM API (with image upload)
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
$image_url = '';

// Validate
if (empty($title) || empty($item_type) || empty($location) || empty($contact_info)) {
    sendResponse(false, 'Please fill all required fields');
}

// Handle image upload if present
if (isset($_FILES['image']) && $_FILES['image']['error'] === UPLOAD_ERR_OK) {
    $uploadDir = '../uploads/lost-found/';

    // Create directory if not exists
    if (!file_exists($uploadDir)) {
        mkdir($uploadDir, 0777, true);
    }

    // Get file info
    $fileName = $_FILES['image']['name'];
    $fileTmp = $_FILES['image']['tmp_name'];
    $fileExt = strtolower(pathinfo($fileName, PATHINFO_EXTENSION));

    // Allowed extensions (images only)
    $allowed = ['jpg', 'jpeg', 'png', 'gif', 'webp'];

    if (!in_array($fileExt, $allowed)) {
        sendResponse(false, 'Invalid image type. Allowed: JPG, PNG, GIF, WebP');
    }

    // Check file size (max 5MB)
    if ($_FILES['image']['size'] > 5 * 1024 * 1024) {
        sendResponse(false, 'Image too large. Maximum 5MB allowed.');
    }

    // Generate unique filename
    $newFileName = 'item_' . time() . '_' . rand(1000, 9999) . '.' . $fileExt;
    $uploadPath = $uploadDir . $newFileName;

    if (move_uploaded_file($fileTmp, $uploadPath)) {
        $image_url = 'uploads/lost-found/' . $newFileName;
    }
}

// Insert item
$sql = "INSERT INTO lost_found (title, item_type, category, location, item_date, description, contact_info, image_url, posted_by, status) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'active')";

$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "sssssssss", $title, $item_type, $category, $location, $item_date, $description, $contact_info, $image_url, $posted_by);

if (mysqli_stmt_execute($stmt)) {
    sendResponse(true, 'Item added successfully', [
        'item_id' => mysqli_insert_id($conn)
    ]);
} else {
    sendResponse(false, 'Failed to add item: ' . mysqli_error($conn));
}

mysqli_close($conn);
?>