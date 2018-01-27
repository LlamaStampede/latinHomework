<!DOCTYPE html>

<html>

<head>
  <meta charset="utf-8">
  <title>Latin ~ Middleman</title>
  <link rel="stylesheet" type="text/css" href="sheet.css">
</head>

<body>
  <?php
  if ($_SERVER[REQUEST_METHOD] == "POST") {
    $rawText = fopen("../code/rawText.txt","w");
    fwrite($rawText,$_POST[rawText]);
    fclose($rawText);
  }
  
  echo exec("cd ../code\npython superclone.py");
  
  $filename = $_POST[filename];
  $pagename = $filename.".php";
  $txtname = $filename.".txt"
  copy("output.php",$pagename);
  copy("sheet.txt",$txtname)
  ?>
  <script>//location = "<?php echo $filename; ?>";</script>
  <h1><a href="">RECOMPILE</a></h1>
  
</body>

</html>
