<?php
// =============================================
// GET EXAM SCHEDULES API
// =============================================

include 'config.php';

$type = isset($_GET['type']) ? trim($_GET['type']) : '';
$dept = isset($_GET['dept']) ? trim($_GET['dept']) : '';
$semester = isset($_GET['semester']) ? intval($_GET['semester']) : 0;

// Admin Scope Filtering
$scope = getAdminScope();
if ($scope['dept'] !== 'all') {
    $dept = $scope['dept'];
}
if ($scope['sem'] !== 'all') {
    $semester = intval($scope['sem']);
}

$sql = "SELECT * FROM exam_schedules WHERE 1=1";
$params = [];
$types = "";

if (!empty($type)) {
    $sql .= " AND schedule_type = ?";
    $params[] = $type;
    $types .= "s";
}

if (!empty($dept)) {
    $sql .= " AND (dept_code = ? OR dept_code IS NULL)";
    $params[] = $dept;
    $types .= "s";
}

if ($semester > 0) {
    $sql .= " AND (semester = ? OR semester IS NULL)";
    $params[] = $semester;
    $types .= "i";
}

$stmt = mysqli_prepare($conn, $sql);
if (!empty($params)) {
    mysqli_stmt_bind_param($stmt, $types, ...$params);
}

mysqli_stmt_execute($stmt);
$result = mysqli_stmt_get_result($stmt);

$schedules = [];
while ($row = mysqli_fetch_assoc($result)) {
    $schedules[] = $row;
}

sendResponse(true, 'Schedules fetched', $schedules);

mysqli_close($conn);
?>