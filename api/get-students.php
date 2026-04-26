<?php
// =============================================
// GET STUDENTS API
// =============================================

include 'config.php';

// Get filters from query
$dept = isset($_GET['dept']) ? trim($_GET['dept']) : '';
$semester = isset($_GET['semester']) ? intval($_GET['semester']) : 0;
$search = isset($_GET['search']) ? trim($_GET['search']) : '';

// Enforce staff scope
$scope = getAdminScope();
if ($scope['dept'] !== 'all') $dept = $scope['dept'];
if ($scope['sem'] !== 'all') $semester = intval($scope['sem']);

// Build query
$sql = "SELECT 
            student_id,
            roll_number,
            name,
            dob,
            email,
            phone,
            dept_code,
            semester,
            created_at
        FROM students
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

if (!empty($search)) {
    $sql .= " AND (roll_number LIKE ? OR name LIKE ?)";
    $searchTerm = "%" . $search . "%";
    $params[] = $searchTerm;
    $params[] = $searchTerm;
    $types .= "ss";
}

$sql .= " ORDER BY roll_number";

$stmt = mysqli_prepare($conn, $sql);

if (!empty($params)) {
    mysqli_stmt_bind_param($stmt, $types, ...$params);
}

mysqli_stmt_execute($stmt);
$result = mysqli_stmt_get_result($stmt);

$students = [];
while ($row = mysqli_fetch_assoc($result)) {
    $students[] = $row;
}

sendResponse(true, 'Students fetched', $students);

mysqli_close($conn);
?>