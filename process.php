<?php

$integers = $_GET['integers'] ?? null;
$threshold = $_GET['threshold'] ?? null;

if (is_null($integers) || is_null($threshold)) {
    echo "<p>Error: Please provide both integers and a threshold in the URL.</p>";
    exit;
}

$integers = escapeshellarg($integers);
$threshold = escapeshellarg($threshold);

echo "Python Execution" . "<br>";

$output = shell_exec("python3 bitwise_operations.py $integers $threshold");

if ($output === null) {
    echo "<p>Error executing Python script.</p>";
} 

else {
    echo "<p>Result: " . nl2br(htmlspecialchars(trim($output)))."</p>";
}

?>