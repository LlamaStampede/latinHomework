<!DOCTYPE html>

<html>

<head>
<meta charset="utf-8">
<title>Constructor</title>
<link rel="stylesheet" type="text/css" href="menu.css">
<link rel="icon" href="../favicon/favicon.ico">
<style>
  body {background-color: #aaeae9}
  .hidden {display: none;}
  #filename {padding: 4px; font-family: georgia, serif; font-size: 11pt; background-color: lightgray;}
  .submit {font-size: inherit;}
  form {position: absolute; top: 60px; left: 40px;}
  form * {margin: 20px;}
</style>
</head>

<body>
<nav><ul>
<li><a href="output.php">Home</a></li><li>
<a href="dictionary.php">Dictionary</a></li><li>
<a class = "current" href="input.html">Input</a></li><li>
<a href="#">Dream of Scipio</a>
<ul>
<li><a href="chapter16.php">Chapter 16</a></li><li>
<a href="chapter17.php">Chapter 17</a></li><li>
<a href="chapter18.php">Chapter 18</a></li><li>
<a href="chapter19.php">Chapter 19</a></li><li>
<a href="chapter20.php">Chapter 20</a></li>
</ul>
</li>
</ul></nav>

<?php
    if ($_SERVER[REQUEST_METHOD] == "POST") {
        $rawText = fopen("../code/rawText.txt","w");
        fwrite($rawText,$_POST[rawText]);
        fclose($rawText);
    }

    echo exec("cd ../code\npython superclone.py");

    $filename = $_POST[filename];
    if ($filename != "output") {
      $pagename = "$filename.php";
      $txtname = "$filename.txt";
      $empty = copy("output.php",$pagename);
      
      if (file_exists($txtname)) {
        $file1 = fopen("sheet.txt","r"); // Recompiled Sheet
        $from = [];
        while(!feof($file1)) {array_push($from,explode("\t",chop(fgets($file1),"\n")));}
        fclose($file1);
        
        $file2 = fopen($txtname,"r"); // Original Sheet
        $to = []; // -> $txtname
        $c1 = 0;
        $phase = "";
        while(!feof($file2)) {
          $line = explode("\t",chop(fgets($file2),"\n"));
          if ($line[0][0] == "#") {
            $phase = $line[0];
            $newline = $line;
          } else if ($phase == "#Sheet") {
            $newline = [];
            for ($c2 = 0; $c2 < 6; $c2++) {
              if ($line[$c2] == "") {array_push($newline,$from[$c1][$c2]);}
              else {array_push($newline,$line[$c2]);}
              if (count($line) == $c2 + 1) {break;}
            }
          } else if ($line == "") {
            $newline = $from[$c1];
          } else {
            $newline = $line;
          }
          array_push($to,$newline);
          $c1++;
        }
        fclose($file2);
        
        $file3 = fopen($txtname,"w"); // Combined Sheet
        foreach ($to as $line) {fwrite($file3,implode("\t",$line)."\n");}
        fclose($file3);
      } else {
        $empty = copy("sheet.txt",$txtname);
      }
    }
  ?>
  
  <form method="post" action="#">
    <?php echo $_SERVER[REQUEST_METHOD] ?>
    <h1>Analysis Sheet Constructor</h1>
    <input id="filename" type="text" value="<?php echo $filename ?>" name="filename"><br>
    <textarea class="hidden" name="rawText"><?php echo $_POST[rawText] ?></textarea>
    <button class="submit">RECOMPILE</button>
    <h2><a href="<?php echo $pagename ?>" target="<?php echo ucfirst($filename) ?>">View</a></h2>
  </form>
  
</body>

</html>
