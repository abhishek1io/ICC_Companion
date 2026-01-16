<?php
// =============================================
// GET ANNOUNCEMENTS API
// =============================================

include 'config.php';

// Get limit from query
$limit = isset($_GET['limit']) ? intval($_GET['limit']) : 50;

// Build query
$sql = "SELECT 
            announcement_id,
            title,
            description,
            priority,
            target_dept,
            target_semester,
            posted_by,
            created_at
        FROM announcements
        ORDER BY 
            CASE priority 
                WHEN 'high' THEN 1 
                WHEN 'medium' THEN 2 
                ELSE 3 
            END,
            created_at DESC
        LIMIT ?";

$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "i", $limit);
mysqli_stmt_execute($stmt);
$result = mysqli_stmt_get_result($stmt);

$announcements = [];
while ($row = mysqli_fetch_assoc($result)) {
    $announcements[] = $row;
}

sendResponse(true, 'Announcements fetched', $announcements);

mysqli_close($conn);
?>