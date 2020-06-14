<?php

$src = empty($_GET['src']) ? 'sakura' : $_GET['src'];
$dir_src = dirname(__FILE__)."/$src";


if(!file_exists($dir_src)) die("$dir_src 振り分け対象がありません。");

$dir_ok = $dir_src.'-ok';
$dir_ng = $dir_src.'-ng';

if(!file_exists($dir_ok)){
  mkdir($dir_ok);
}

if(!file_exists($dir_ng)){
  mkdir($dir_ng);
}


$m = empty($_GET['m']) ? 'show' : $_GET['m'];

if($m == 'show'){
  $files = glob("./{$src}/*.jpg");

  if(!$files) die("もう画像がありません。");

  $file = $files[0];
  echo "<meta name='viewport' content='width=320'>";
  echo "<img src='$file' width='300'><br>";

  $f = basename($file);
  echo "<a href='index.php?src=$src&$m=ok&f=$f'>[OK]</a> ---";
  echo "<a href='index.php?src=$src&$m=ng&f=$f'>[NG]</a>";

} else if ($m == 'ok' || $m == 'ng') {
  $f = empty($_GET['f']) ? '' : $_GET['f'];
  $file = "$dir_src/$f";
  $moveto = "${dir_src}-{$m}/$f";

  if(!file_exists($file)) die("ファイルがありません。");

  $b = @rename($file, $moveto);

  if(!$b) die("ファイルの移動に失敗しました。");

  header("location: ./index.php?src=$src");
}


?>
