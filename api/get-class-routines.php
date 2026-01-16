<?php
// =============================================
// GET CLASS ROUTINES API
// =============================================

include 'config.php';

$dept = isset($_GET['dept']) ? trim($_GET['dept']) : '';
$semester = isset($_GET['semester']) ? trim($_GET['semester']) : '';

$sql = "SELECT * FROM class_routines WHERE 1=1";

if (!empty($dept)) {
    $sql .= " AND dept_code = '" . mysqli_real_escape_string($conn, $dept) . "'";
}

if (!empty($semester)) {
    $sql .= " AND semester = '" . mysqli_real_escape_string($conn, $semester) . "'";
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