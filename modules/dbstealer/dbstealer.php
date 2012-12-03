<?php
//////////////////////////////////////////////////
// Android file browser and .db file extractor 	//
// Author: Subho Halder                         //
// Blog: http://subho.me/                       //
// Web: http://subhohalder.com/                 //
// License: GNU GPlv2                           //
// Donot remove this header !                   //
//////////////////////////////////////////////////
echo "Welcome to .db file extractor !!\n\n\n";
//////////se base path --->> //////////////////////////////////
$base = "/data/data/";
//////////////////////////////////////////////////////////////
/////// Getting which OS ////////////////////////////////////
if (strtoupper(substr(PHP_OS, 0, 3)) === 'WIN') {
	$platform = 'windows';
} else if (strtoupper(substr(PHP_OS, 0, 3)) === 'DAR') {
	$platform = 'mac';
} else {
	$platform = 'linux';
}
//////////////////////////////////////////////////////////////////////////////////
////////getting the list of devices attached ////////////////////////////////////
@exec('adb devices');
exec('adb devices', $d);
$extend = "";
device:
$dev = 0;
/////////// Menu of devices!! ////////////////////////////////////
foreach($d as $devices) {
	if($dev==0) {
		echo $devices."\n\n";
		$dev++;
		continue;
	}
	if (empty($devices)) {
		$dev++;
		continue;
	}
	$slc = preg_split("/\s+/", $devices, -1, PREG_SPLIT_NO_EMPTY);
	echo $dev.' '.$slc[0]."\n";
	$dev++;
}
/////////////////Menu choice ////////////////////////////////////
echo "\nChoose Which device you want to work with? (Enter 1,2,3....)\n";
$inp = strtolower(trim(fgets(STDIN))); 
$default = '';
if(empty($inp) || $inp=="\r" || $inp>=$dev-1 || $inp<=0 || !is_numeric($inp)) { 
	goto device; 
} else {
	$tsel = $d[$inp];
	$t2sel = preg_split("/\s+/", $tsel, -1, PREG_SPLIT_NO_EMPTY);
	$device = $t2sel[0];
	$device = trim($device);
}
//////////////////////Devices menu End ////////////////////////////////////

exec('adb -s '.$device.' root');
exec('adb -s '.$device.' shell ls -l '.$base, $m);
///////////////File list menu ////////////////////////////////////////////
menu:

echo "\nFound Files in the ".$base.$extend." Folder! \n\n";
$n=1;
foreach ($m as $line) {
	$slice = preg_split("/\s+/", $line, -1, PREG_SPLIT_NO_EMPTY);
	$end=7;
	if(stristr($slice[0],'d')) {
		$end=6;
	}
	echo $n." ".$slice[$end-1]."\n";
	$n++;
}
echo "\nChoose Which file you want to get? (Enter 1,2,3....)\nEnter R to go back to default directory\nEnter e to exit\nEnter A to get all .db files from this directory\n\n";
$input = strtolower(trim(fgets(STDIN))); 
$default = '';
$final_p = "../../Output/dbstealer/".$device."/";
if($input == 'e' || $input == 'E') {
goto end;
}
if($input == 'a' || $input == 'A') {
goto findall;
}
if($input == 'r' || $input == 'R') {
	$extend = "";
	$m = "";
	exec('adb -s '.$device.' shell ls -l '.$base, $m);
	goto menu;
}
if(empty($input) || $input=="\r" || $input>=$n || $input<=0 || !is_numeric($input)) { 
	goto menu; 
} else {
	$tmp1 = $m[$input-1];
	$files = preg_split("/\s+/", $tmp1, -1, PREG_SPLIT_NO_EMPTY);
	if(stristr($files[0],'d')) {
		$extend = $extend.$files[5]."/";
		$m = "";
		exec('adb -s '.$device.' shell ls -l '.$base.$extend, $m);
		goto menu;
	}
	$file = $files[6];
}
if(!is_dir($final_p)) {
	@mkdir($final_p);
}
if(file_exists($final_p."/".$file)) {
	echo "Remove the db file from the folder to copy !";
} else {
	exec('adb -s '.$device.' pull '.$base.$extend.$file.' '.$final_p);
}
goto menu;
findall:
echo "getting all .db files from ".$base.$extend." directory and beneath it too \n\n...";
@mkdir($final_p);
exec('adb -s '.$device.' shell ls -l '.$base.$extend, $ma);
foreach ($ma as $line) {
	$slice = preg_split("/\s+/", $line, -1, PREG_SPLIT_NO_EMPTY);
	$end=7;
	if(stristr($slice[0],'d')) {
		$end=6;
		scaneer($base.$extend.$slice[$end-1],$device);
	}
	if($end==7) {
		if(stristr($slice[$end-1],'.db')) {
			exec('adb -s '.$device.' pull '.$base.$extend.$slice[$end-1].' '.$final_p);
		}
	}
}
goto menu;
/////////////////////// function to get all .db files inside a specific path ////////////////////////
function scaneer($path,$device) {
$fp = "../../Output/dbstealer/".$device;
exec('adb -s '.$device.' shell ls -l '.$path, $mf);
foreach ($mf as $line) {
	$slice = preg_split("/\s+/", $line, -1, PREG_SPLIT_NO_EMPTY);
	$end=7;
	if(stristr($slice[0],'d')) {
		$end=6;
		scaneer($path.'/'.$slice[$end-1],$device);
	}
	if($end==7) {
		if(stristr($slice[$end-1],'.db')) {
			exec('adb -s '.$device.' pull '.$path.'/'.$slice[$end-1].' '.$fp);
		}
	}
}
}
end:
?>
