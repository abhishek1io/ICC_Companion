<?php
// =============================================
// GET EXAMS API (updated for new exam types)
// =============================================

include 'config.php';

// Get filters from query
$dept = isset($_GET['dept']) ? trim($_GET['dept']) : '';
$semester = isset($_GET['semester']) ? intval($_GET['semester']) : 0;
$type = isset($_GET['type']) ? trim($_GET['type']) : '';

// Admin Scope Filtering
$scope = getAdminScope();
if ($scope['dept'] !== 'all') {
    $dept = $scope['dept'];
}
if ($scope['sem'] !== 'all') {
    $semester = intval($scope['sem']);
}

// Build query with join to get subject details
$sql = "SELECT 
            e.exam_id,
            e.exam_date,
            e.start_time,
            e.end_time,
            e.room,
            e.exam_type,
            e.attachment_url,
            s.subject_id,
            s.subject_name,
            s.subject_code,
            s.dept_code,
            s.semester
        FROM exams e
        JOIN subjects s ON e.subject_id = s.subject_id
        WHERE e.exam_date >= CURDATE()";

$params = [];
$types = "";

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

if (!empty($type)) {
    $sql .= " AND e.exam_type = ?";
    $params[] = $type;
    $types .= "s";
}

$sql .= " ORDER BY e.exam_date, e.start_time";

$stmt = mysqli_prepare($conn, $sql);

if (!empty($params)) {
    mysqli_stmt_bind_param($stmt, $types, ...$params);
}

mysqli_stmt_execute($stmt);
$result = mysqli_stmt_get_result($stmt);

$exams = [];
while ($row = mysqli_fetch_assoc($result)) {
    $exams[] = $row;
}

sendResponse(true, 'Exams fetched', $exams);

mysqli_close($conn);
?>