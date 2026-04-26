<?php
// =============================================
// GET SUBJECTS API
// =============================================

include 'config.php';

// Get filters
$dept = isset($_GET['dept']) ? trim($_GET['dept']) : '';
$semester = isset($_GET['semester']) ? intval($_GET['semester']) : 0;

// Enforce staff scope
$scope = getAdminScope();
if ($scope['role'] !== 'faculty') {
    if ($scope['dept'] !== 'all') $dept = $scope['dept'];
    if ($scope['sem'] !== 'all') $semester = intval($scope['sem']);
}

// Build query
$sql = "SELECT s.subject_id, s.subject_code, s.subject_name, s.dept_code, s.semester 
        FROM subjects s";

$params = [];
$types = "";

// If Faculty, only show their assigned subjects
if ($scope['role'] === 'faculty') {
    $sql .= " JOIN faculty_subjects fs ON s.subject_id = fs.subject_id WHERE fs.admin_id = ?";
    $params[] = $scope['id'];
    $types .= "i";
} else {
    $sql .= " WHERE 1=1";
}

if (!empty($dept)) {
    $sql .= " AND s.dept_code = ?";
    $params[] = $dept;
    $types .= "s";
}

if ($semester > 0) {
    $sql .= " AND s.semester = ?";
    $params[] = $semester;
    $types .= "i";
}

$sql .= " ORDER BY s.subject_name";

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