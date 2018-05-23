<?php
/*
 * Created By X-Random1971
 * Modified by M4FI4_9R3Y-H4T
*/
function auto($url){
$data = curl_init();
curl_setopt($data, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($data, CURLOPT_URL, $url);
$hasil = curl_exec($data);
curl_close($data);
return $hasil;
}
$access_token= "EAAAA......";
if(file_exists('C3')){ $log=json_encode(file('KupasTrik_Log')); }else{ $log=''; }
$stat=json_decode(auto('https://graph.beta.facebook.com/me/home?fields=id,from&limit=15&access_token='.$access_token),true);
for($i=1;$i<=count($stat[data]);$i++){
if(!ereg($stat[data][$i-1][id],$log)){
$x=$stat[data][$i-1][id]."\n";
$y=fopen('KupasTrik_Log','a');
fwrite($y,$x);
fclose($y);
auto('https://graph.beta.facebook.com/'.$stat[data][$i-1][id].'/likes?method=post&access_token='.$access_token);
echo '<span style="color:#0E0101">'.$stat[data][$i-1][from][name].'</span> <span style="color:green">[SUCCESS]</span><hr/>';
}
}
?>