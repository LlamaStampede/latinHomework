<!DOCTYPE html>

<html>

<head>
  <title><?php
  $pagename = end(explode("/",__FILE__));
  $filename = substr($pagename,0,strlen($pagename)-4);
  $txtname = $filename.".txt";
  if ($txtname == "output.txt") {$txtname = "sheet.txt";}
  echo ucfirst($filename);
  ?></title>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="sheet.css">
  <link rel="icon" href="../favicon/favicon.ico">
  <link rel="stylesheet" type="text/css" href="menu.css">
</head>

<body>

<nav><ul>
<li><a href="output.php">Home</a></li><li>
<a href="dictionary.php">Dictionary</a></li><li>
<a href="input.html">Input</a></li><li>
<a class = "current">Dream of Scipio</a>
<ul>
<li><a href="chapter16.php">Chapter 16</a></li><li>
<a href="chapter17.php">Chapter 17</a></li><li>
<a href="chapter18.php">Chapter 18</a></li><li>
<a href="chapter19.php">Chapter 19</a></li><li>
<a class = "current">Chapter 20</a></li>
</ul>
</li>
</ul></nav>
<h1 class="plain"><a href="">Analysis Sheet</a></h1>
<p id="Center">Center</p><input type="checkbox" checked>
<p id="Embed">Embed Errors</p><input type="checkbox">
  <form action="<?php echo $pagename ?>" method="post" id="auto">
    <p id="Parse">Parse</p><input type="checkbox" name="parsing" checked>
    <p id="Show">Show Errors</p><input type="checkbox" name="show_errors" checked>
    <header>
      <input type="submit" value="Save">
    </header>
    <?php
    echo "<h1>" . $_SERVER[REQUEST_METHOD] . "</h1>";
    if ($_SERVER[REQUEST_METHOD] == "POST") {
      $sheet = $report = [];
      $source = fopen($txtname,"w");
      fwrite($source,"#Info\n");
      if ($_POST[parsing] == "on") {fwrite($source,"y\t"); $parsing = "y";} else {fwrite($source,"n\t"); $parsing = "n";}
      if ($_POST[show_errors] == "on") {fwrite($source,"y\n"); $show_errors = "y";} else {fwrite($source,"n\n"); $show_errors = "n";}
      fwrite($source,"#Sheet");
      for ($x = 1; $x <= 1000; $x++) {
        if (!array_key_exists($x."_2",$_POST)) {break 1;}
        $line = [];
        for ($y = 1; $y <= 5; $y++) {
          array_push($line, $_POST[$x . "_" . $y]);
        }
        if (array_key_exists($x."_6",$_POST)) {
          $error = [$_POST[$x."_0"]];
          array_push($line,$_POST[$x ."_6"]);
          array_push($error,$_POST[$x ."_6"]);
          if ($_POST[$x."_6"] == "Conflict:") {
            for ($z = 7; $z <= 11; $z ++) {
              if (array_key_exists($x . "_" . $z, $_POST)) {
                array_push($error,$_POST[$x . "_" . $z]);
                array_push($line,$_POST[$x . "_" . $z]);
              } else {break 1;}
            }
          }
          array_push($report,$line[0] + $error);
        }
        fwrite($source,"\n" . implode("\t",$line));
      }
      foreach ($report as $error)
      fclose($source);
    }
    $sheet = $report = [];
    $source = fopen($txtname,"r");
    while (!feof($source)) {
      $line = chop(fgets($source),"\n");
      if ($line[0] == "#") {
        $phase = $line;
      } else {
        $line = explode("\t",$line);
        switch ($phase) {
          case "#Info":
            $parsing = $line[0];
            $show_errors = $line[1];
            break 1;
          case "#Sheet":
            if ($line != "") {array_push($sheet,$line);}
            break 1;
          case "#Report":
            array_push($report,$line);
            break 1;
        }
      }
    }
    fclose($source);
    
    /*foreach ([$sheet,$report] as $list) {
      foreach ($list as $entry) {
        foreach($entry as $row) {
          echo " ", $row;
        }
        echo "<br>";
      }
      echo "<br>";
    }*/
    
    echo "<div id='sheet'>";
    $counter = 0;
    foreach ($sheet as $col) {
      echo "<ul id='".++$counter."'>";
      $subcounter = 0;
      $error = [];
      foreach ($col as $row) {
        if (++$subcounter == 3 and $parsing == "n") {
          echo "<li><input type='text' name='".$counter."_".$subcounter."' value='".$row."'></li>";
        } elseif ($subcounter == 1) { /*Delete to allow editing the first line*/
          echo "<li>".$row."<input class='hidden' name='".$counter."_1' value='".$row."'></li>";
        } elseif ($subcounter <= 5) {
          echo "<li><input type='text' name='".$counter."_".$subcounter."' value='".$row."'></li>";
        } else {
          array_push($error,$row);
        }
        if ($error !== []) {echo "<li class='error'>".implode("\t",$error)."</li>";}
          
      }
      echo "</ul>";
    }
    echo "<hr class='vert'></div><div id='report'><ul>";
    foreach ($report as $error) {
      echo "<li>".implode(":",$error)."</li>";
    }
    echo "</ul></div>";
    ?>
  </form>
</body>