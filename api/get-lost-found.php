<?php
// =============================================
// GET LOST AND FOUND API
// =============================================

include 'config.php';

// Get filters from query
$type = isset($_GET['type']) ? trim($_GET['type']) : '';
$category = isset($_GET['category']) ? trim($_GET['category']) : '';
$status = isset($_GET['status']) ? trim($_GET['status']) : 'active';

// Build query
$sql = "SELECT 
            item_id,
            title,
            description,
            category,
            item_type,
            location,
            item_date,
            contact_info,
            image_url,
            status,
            posted_by,
            created_at
        FROM lost_found
        WHERE 1=1";

$params = [];
$types = "";

if (!empty($type)) {
    $sql .= " AND item_type = ?";
    $params[] = $type;
    $types .= "s";
}

if (!empty($category)) {
    $sql .= " AND category = ?";
    $params[] = $category;
    $types .= "s";
}

if (!empty($status)) {
    $sql .= " AND status = ?";
    $params[] = $status;
    $types .= "s";
}

$sql .= " ORDER BY created_at DESC";

$stmt = mysqli_prepare($conn, $sql);

if (!empty($params)) {
    mysqli_stmt_bind_param($stmt, $types, ...$params);
}

mysqli_stmt_execute($stmt);
$result = mysqli_stmt_get_result($stmt);

$items = [];
while ($row = mysqli_fetch_assoc($result)) {
    $items[] = $row;
}

sendResponse(true, 'Items fetched', $items);

mysqli_close($conn);
?>