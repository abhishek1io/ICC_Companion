<?php
// =============================================
// GET ROUTINES API
// =============================================

include 'config.php';

// Get filters
$dept = isset($_GET['dept']) ? trim($_GET['dept']) : '';
$semester = isset($_GET['semester']) ? trim($_GET['semester']) : '';
$type = isset($_GET['type']) ? trim($_GET['type']) : '';

// Build query
$sql = "SELECT * FROM routines WHERE 1=1";

if (!empty($dept) && $dept !== 'all') {
    $sql .= " AND (dept_code = 'all' OR dept_code = '" . mysqli_real_escape_string($conn, $dept) . "')";
}

if (!empty($semester) && $semester !== 'all') {
    $sql .= " AND (semester = 'all' OR semester = '" . mysqli_real_escape_string($conn, $semester) . "')";
}

if (!empty($type)) {
    $sql .= " AND routine_type = '" . mysqli_real_escape_string($conn, $type) . "'";
}

$sql .= " ORDER BY created_at DESC";

$result = mysqli_query($conn, $sql);

$routines = [];
while ($row = mysqli_fetch_assoc($result)) {
    $routines[] = $row;
}

sendResponse(true, 'Routines fetched', $routines);

mysqli_close($conn);
?>