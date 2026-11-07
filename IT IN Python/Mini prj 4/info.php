<?php
// give  information of  python
$osname = $_POST['os-name'] ?? 'Unknown';
$tzon = $_POST['time-zone'] ?? 'Unknown';
$ip = $_POST['client-ip'] ?? 'Unknown';

// make  arrya  and  change to  json
$data = array(
    "os-name" => $osname, 
    "time-zone" => $tzon, 
    "client-ip" => $ip
);
$jdata = json_encode($data);

// save  files
file_put_contents("data.json", $jdata);

// send  a  massage  if it's correct  
echo "Success! Data saved.";
?>