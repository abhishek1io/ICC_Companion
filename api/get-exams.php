<?php
// =============================================
// GET EXAMS API
// =============================================

include 'config.php';

// Get filters from query
$dept = isset($_GET['dept']) ? trim($_GET['dept']) : '';
$semester = isset($_GET['semester']) ? intval($_GET['semester']) : 0;
$exam_type = isset($_GET['type']) ? trim($_GET['type']) : '';

// Build query
$sql = "SELECT 
            e.exam_id,
            sub.subject_code,
            sub.subject_name,
            sub.dept_code,
            sub.semester,
            e.exam_date,
            e.start_time,
            e.end_time,
            e.room,
            e.exam_type
        FROM exams e
        JOIN subjects sub ON e.subject_id = sub.subject_id
        WHERE e.exam_date >= CURDATE()";

$params = [];
$types = "";

if (!empty($dept)) {
    $sql .= " AND sub.dept_code = ?";
    $params[] = $dept;
    $types .= "s";
}

if ($semester > 0) {
    $sql .= " AND sub.semester = ?";
    $params[] = $semester;
    $types .= "i";
}

if (!empty($exam_type)) {
    $sql .= " AND e.exam_type = ?";
    $params[] = $exam_type;
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