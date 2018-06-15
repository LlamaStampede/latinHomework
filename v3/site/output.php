<!DOCTYPE html>

<html>

<head>
  <title><?php
  $method = $_SERVER[REQUEST_METHOD];
  /*if ($method == "POST") {$address = $_POST["address"];}
  else {$address = $_GET["address"];}*/
  $address = htmlspecialchars($_REQUEST["address"]);
  echo $address;?></title>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="css/sheet.css">
  <link rel="stylesheet" type="text/css" href="css/menu.css">
  <link rel="icon" href="../favicon/favicon.ico">
</head>

<body>
  <nav><ul>
      <li class="current"><a href="">Home</a></li>
      <li><a href="dictionary.php">Dictionary</a></li>
      <li><a href="input.html">Input</a></li>
  </ul></nav>
      
  <h1 class="plain"><a href="output.php?address=<?php echo $address ?>">Analysis Sheet</a></h1>
  <p id="Center">Center</p><input type="checkbox">
  <p id="Embed">Embed Errors</p><input type="checkbox">
  <p id="Study">Study mode</p><input type="checkbox">
  
  <form action="output.php" method="post" id="auto"> 
    <p id="Parse">Parse</p><input type="checkbox" name="parsing" checked>
    <p id="Show">Show Errors</p><input type="checkbox" name="show_errors" checked>
    <input type="submit" value="Save">
    <input class="hidden" name="address" value="<?php echo $address; ?>">
    <?php
    $conn = new PDO("mysql:host=127.0.0.1; dbname=TLD_SHT", "tld_main", "paramus");
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    //echo "<h1>" . $_SERVER[REQUEST_METHOD] /*or $method*/ . "</h1>";
    //Include: <input name="address" value="$address"> ... <button type="submit">Change</button>
    $cols = ["trm","dct","prs","trn","cmt"];
    if ($method == "POST") {
      try {
        
        $sheet = $report = [];
        $stmt = $conn->prepare("UPDATE ${address}_main SET trm=:trm, dct=:dct, prs=:prs, trn=:trn, cmt=:cmt WHERE id=:id;"); //Similar security problems
        $stmt->bindParam(":id",$id);
        foreach ($cols as $col) {
          $stmt->bindParam(":$col",$GLOBALS[$col]);
        }
        
        $id = 1;
        while(array_key_exists("${id}_dct",$_POST)) {
          foreach ($cols as $col) {
            $input = $_POST["${id}_$col"];
            if ($input === "") {$GLOBALS[$col] = null;}
            else {$GLOBALS[$col] = $input;}
          }
          
          //list($trm,$dct,$prs,$trn,$cmt) = 
          $stmt->execute();
          $id++;
        }
        //TODO: error-editing
      } catch (PDOException $e) {
        echo $e->getMessage();
      }
    }
    try {
      //This doesn't work:
      //$stmt = $conn->prepare("SELECT trm, dct, prs, trn, cmt FROM :table;");
      //$stmt->bindParam(":table",$table);
      //$table = "${address}_main";
      //But this does:
      $stmt = $conn->prepare("SELECT trm, dct, prs, trn, cmt FROM ${address}_main;");
      //However, I think it might be unsafe (SQL Injection)
      
      $stmt->execute();
      $sheet = $stmt->fetchAll(PDO::FETCH_ASSOC);
      $sheetString = "<div id='sheet'>";
      $i = 1; //counter
      
      foreach ($sheet as $col) {
        $sheetString .= "<ul id='$i'>";
        $j = 0; //subcounter
        foreach ($col as $row) { // null automatically becomes "", no need to change manually
          if ($j == 0) {
            $sheetString .= "<li>$row<input class='hidden' type='text' name='${i}_trm' value='$row'></li>";
            //TODO: (Not here) Change parsing mode to topline-editing mode //Either checkbox on the side or doubleclick the topline
          } else {
            $key = $cols[$j];
            $sheetString .= "<li><input type='text' name='${i}_$key' value='$row'></li>";
          }
          $j++;
        }
        //Line about error
        $sheetString .= "</ul>";
        $i++;
      }
      $sheeString .= "</div>";
      echo $sheetString;
    } catch (PDOException $e) {
      echo $e->getMessage();
    }
    
    //TODO: Main Error Report
    
    $conn = null;
    ?>
  </form>
</body>

</html>