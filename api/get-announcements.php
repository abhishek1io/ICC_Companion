<?php
// =============================================
// GET ANNOUNCEMENTS API
// =============================================

include 'config.php';

// Get filters
$limit = isset($_GET['limit']) ? intval($_GET['limit']) : 0;
$dept = isset($_GET['dept']) ? trim($_GET['dept']) : '';
$semester = isset($_GET['semester']) ? trim($_GET['semester']) : '';

// Build query
$sql = "SELECT * FROM announcements WHERE 1=1";

if (!empty($dept) && $dept !== 'all') {
    $sql .= " AND (target_dept = 'all' OR target_dept = '" . mysqli_real_escape_string($conn, $dept) . "')";
}

if (!empty($semester) && $semester !== 'all') {
    $sql .= " AND (target_semester = 'all' OR target_semester = '" . mysqli_real_escape_string($conn, $semester) . "')";
}

$sql .= " ORDER BY created_at DESC";

if ($limit > 0) {
    $sql .= " LIMIT " . $limit;
}

$result = mysqli_query($conn, $sql);

$announcements = [];
while ($row = mysqli_fetch_assoc($result)) {
    $announcements[] = $row;
}

sendResponse(true, 'Announcements fetched', $announcements);

mysqli_close($conn);
?>