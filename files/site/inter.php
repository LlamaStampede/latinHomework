<!DOCTYPE html>

<html>

<head>
<meta charset="utf-8">
<title>Constructor</title>
<link rel="stylesheet" type="text/css" href="sheet.css">
<link rel="stylesheet" type="text/css" href="styles.css">
<link rel="icon" href="../favicon/favicon.ico">
  <style>.hidden {display: none;}</style>
</head>

<body>
<ul id="test">
<li><a href="output.php">Home</a></li><li>
<a href="dictionary.php">Dictionary</a></li><li>
<a class = "current" href="input.html">Input</a></li><li>
<a href="#">Dream of Scipio<img src= "https://image.flaticon.com/icons/png/512/60/60995.png" width = "13" height = "13"></a>
<ul>
<li><a href="chapter16.php">Chapter 16</a></li><li>
<a href="chapter17.php">Chapter 17</a></li><li>
<a href="#">Chapter 18</a></li><li>
<a href="#">Chapter 19</a></li><li>
<a href="#">Chapter 20</a></li>
</ul>
</li>
</ul>

<?php
    if ($_SERVER[REQUEST_METHOD] == "POST") {
        $rawText = fopen("../code/rawText.txt","w");
        fwrite($rawText,$_POST[rawText]);
        fclose($rawText);
    }

    echo exec("cd ../code\npython superclone.py");

    $filename = $_POST[filename];
    if ($filename != "output") {
    $pagename = $filename.".php";
    $txtname = $filename.".txt";
    $empty = copy("output.php",$pagename);
    $empty = copy("sheet.txt",$txtname);
  }
  ?>
  <script>//location = "<?php echo $filename; ?>";</script>
  <h1><form method="post" action="">
    <input class="yeah" type="text" value="<?php echo $filename ?>" name="filename"><br>
    <textarea class="hidden"><?php echo $_POST[rawText] ?></textarea>
    <button class="submit">RECOMPILE</button>
  <form></h1>
  <h2><a href="<?php echo $pagename ?>" target="<?php echo ucfirst($filename) ?>">View</a></h2>
  
</body>

</html>
