<!DOCTYPE html>

<html>

<head>
<meta charset="utf-8">
<title>Constructor</title>
<link rel="stylesheet" type="text/css" href="css/menu.css">
<link rel="stylesheet" type="text/css" href="css/inter.css">
<link rel="icon" href="../favicon/favicon.ico">
</head>

<body>
<nav><ul>
<li><a href="output.php">Home</a></li>
<li><a href="dictionary.php">Dictionary</a></li>
<li><a class="current" href="input.html">Input</a></li>
</ul></nav>

<?php
    $rawText = fopen("../code/rawText.txt","w");
    fwrite($rawText,$_POST[rawText]); //I may need to add <textarea class="hidden"> if this doesn't work
    fclose($rawText);
    $afile = fopen("../code/address.txt","w");
    fwrite($afile,$_POST[address]); //Same with this for <input class="hidden">
    fclose($afile);
    
    echo exec("cd ../code\npython main.py");
    
    $address = $_POST[address];
  ?>
  
  <form method="post" action="#">
    <?php echo $_SERVER[REQUEST_METHOD] ?>
    <h1>Analysis Sheet Constructor</h1>
    <input id="filename" type="text" value="<?php echo $address ?>" name="address"><br>
    <textarea class="hidden" name="rawText"><?php echo $_POST[rawText] ?></textarea>
    <button class="submit">RECOMPILE</button>
    <h2><a href="output.php?address=<?php echo $address ?>" target="<?php echo $address ?>">View</a></h2>
  </form>
  
</body>

</html>
