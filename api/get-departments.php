<?php
include 'config.php';

$sql = "SELECT * FROM departments ORDER BY dept_name ASC";
$result = mysqli_query($conn, $sql);

$departments = [];
while ($row = mysqli_fetch_assoc($result)) {
    $departments[] = $row;
}

sendResponse(true, 'Departments fetched', $departments);
mysqli_close($conn);
?>
