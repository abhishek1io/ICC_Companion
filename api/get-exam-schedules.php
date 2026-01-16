<?php
// =============================================
// GET EXAM SCHEDULES API
// =============================================

include 'config.php';

$type = isset($_GET['type']) ? trim($_GET['type']) : '';

$sql = "SELECT * FROM exam_schedules";
if (!empty($type)) {
    $sql .= " WHERE schedule_type = '" . mysqli_real_escape_string($conn, $type) . "'";
}

$result = mysqli_query($conn, $sql);

$schedules = [];
while ($row = mysqli_fetch_assoc($result)) {
    $schedules[] = $row;
}

sendResponse(true, 'Schedules fetched', $schedules);

mysqli_close($conn);
?>