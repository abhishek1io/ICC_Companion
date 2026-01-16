<?php
// =============================================
// GET SUBJECTS API
// =============================================

include 'config.php';

// Get filters
$dept = isset($_GET['dept']) ? trim($_GET['dept']) : '';
$semester = isset($_GET['semester']) ? intval($_GET['semester']) : 0;

// Build query
$sql = "SELECT subject_id, subject_code, subject_name, dept_code, semester 
        FROM subjects 
        WHERE 1=1";

$params = [];
$types = "";

if (!empty($dept)) {
    $sql .= " AND dept_code = ?";
    $params[] = $dept;
    $types .= "s";
}

if ($semester > 0) {
    $sql .= " AND semester = ?";
    $params[] = $semester;
    $types .= "i";
}

$sql .= " ORDER BY subject_name";

$stmt = mysqli_prepare($conn, $sql);

if (!empty($params)) {
    mysqli_stmt_bind_param($stmt, $types, ...$params);
}

mysqli_stmt_execute($stmt);
$result = mysqli_stmt_get_result($stmt);

$subjects = [];
while ($row = mysqli_fetch_assoc($result)) {
    $subjects[] = $row;
}

sendResponse(true, 'Subjects fetched', $subjects);

mysqli_close($conn);
?>