<?php

header("Content-Type: application/json");

$data = json_decode(file_get_content("php://input"));

echo "Hello $data->name, your email is $data->email";

?>

