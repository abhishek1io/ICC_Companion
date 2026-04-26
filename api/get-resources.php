<?php
// =============================================
// GET RESOURCES API
// =============================================

include 'config.php';

$dept = isset($_GET['dept']) ? trim($_GET['dept']) : '';
$semester = isset($_GET['semester']) ? trim($_GET['semester']) : '';
$type = isset($_GET['type']) ? trim($_GET['type']) : '';
$subject_id = isset($_GET['subject_id']) ? intval($_GET['subject_id']) : 0;

// Admin Scope Filtering
$scope = getAdminScope();
if ($scope['dept'] !== 'all') {
    $dept = $scope['dept'];
}
if ($scope['sem'] !== 'all') {
    $semester = $scope['sem'];
}

$sql = "SELECT r.*, s.subject_name 
        FROM resources r
        LEFT JOIN subjects s ON r.subject_id = s.subject_id
        WHERE 1=1";

$params = [];
$types = "";

if (!empty($dept) && $dept !== 'all') {
    $sql .= " AND r.dept_code = ?";
    $params[] = $dept;
    $types .= "s";
}

if (!empty($semester) && $semester !== 'all') {
    $sql .= " AND r.semester = ?";
    $params[] = $semester;
    $types .= "s";
}

if (!empty($type)) {
    $sql .= " AND r.resource_type = ?";
    $params[] = $type;
    $types .= "s";
}

if ($subject_id > 0) {
    $sql .= " AND r.subject_id = ?";
    $params[] = $subject_id;
    $types .= "i";
}

$sql .= " ORDER BY r.created_at DESC";

$stmt = mysqli_prepare($conn, $sql);

if (!empty($params)) {
    mysqli_stmt_bind_param($stmt, $types, ...$params);
}

mysqli_stmt_execute($stmt);
$result = mysqli_stmt_get_result($stmt);

$resources = [];
while ($row = mysqli_fetch_assoc($result)) {
    $resources[] = $row;
}

sendResponse(true, 'Resources fetched', $resources);

mysqli_close($conn);
?>
