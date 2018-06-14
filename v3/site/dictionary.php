<!DOCTYPE html>

<html>

<head>
  <title>Dictionary</title>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="input.css">
  <link rel="stylesheet" type="text/css" href="tabs.css">
  <link rel="stylesheet" type="text/css" href="menu.css">
  <link rel="icon" href="../favicon/favicon.ico">
  <style>
  #toTop {display: none; position: fixed; bottom: 70px; left: 50px;}
  footer p {margin: -3em 0 1em; height: 2em; font-family: monospace; letter-spacing: -0.5px; font-size: 11pt;}
</style>
</head>

<body>
  <nav>
    <ul>
        <li><a href="output.php">Home</a></li>
        <li class="current"><a href="dictionary.php">Dictionary</a></li>
        <li><a href="input.html">Input</a></li>
    </ul>
  </nav>
  
  <header>
    <h1 id="dct"><a href="">Dictionary</a></h1>
    <div id="tabs">
      <button class="tab" onclick='showTab(event,"adjs");'>Adjectives</button>
      <button class="tab" onclick='showTab(event,"nouns");'>Nouns</button>
      <button class="tab" onclick='showTab(event,"verbs");'>Verbs</button>
    </div>
    <p><a href="#bottom">Skip to Bottom</a></p>
  </header>

  <script>
    function showTab(evt, part) {
      // Declare all variables
      var sections = document.getElementsByTagName("section");
      for (var i = 0; i < sections.length; i++) {
          sections[i].style.display = "none";
      }
      var tablinks = document.getElementsByClassName("tab");
      for (i = 0; i < tablinks.length; i++) {
          tablinks[i].id = "";
      }
      document.getElementById(part).style.display = "block";
      evt.currentTarget.id = "active";
      document.getElementById('submit').style.display = "block";
      document.getElementById("focus-"+part).focus();
      document.getElementById("toTop").style.display = "inline-block";
    }
  </script>
    
  <form action="dictionary.php" method="post">
      <?php
      
      $ids = ["adjs","nouns","verbs"];
      $allCols = ["adjs"=>["term1","term2","term3","trn"],"nouns"=>["nom","gen","gender","trn"],"verbs"=>["pp1","pp2","pp3","pp4","trn"]];
      
      try {
        $conn = new PDO("mysql:host=127.0.0.1; dbname=TLD_DCT", "tld_main", "paramus");
        // set the PDO error mode to exception
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        
        if ($_SERVER[REQUEST_METHOD] == "POST" and $_POST["${part}_trn"] !== "") {
          foreach ($ids as $part) {
            if ($_POST["${part}_trn"] !== "") {break;}
          }
          
          $cols = $allCols[$part];
          if ($_POST["${part}_term1"] === "") {array_shift($cols);}
          $values = [];
          foreach ($cols as $col) {array_push($values,":$col");}
          $colString = join(",",$cols);
          $valueString = join(",",$values);
          var_dump($valueString);
          
          $stmt = $conn->prepare("INSERT INTO $part ($colString) VALUES ($valueString);");
          $inputs = $_POST;
          var_dump($_POST);
          echo "<br><br><br>";
          foreach ($values as $value) {
            $col = substr($value,1); // w/o the initial ":"
            if ($inputs["${part}_$col"] === "") {$inputs["${part}_$col"] = null;}
            $stmt->bindParam($value,$inputs["${part}_$col"]);
            echo "${part}_$col", $value;
            var_dump($inputs["${part}_$col"]);
            echo "<br>";
          }
          $stmt->execute();
        }
        
        foreach ($ids as $part) {
          $colString = join(", ", $allCols[$part]);
          $table = $conn->query("SELECT $colString FROM $part")->fetchAll();
          //var_dump($table);
          $title = ["adjs"=>"Adjectives", "nouns"=>"Nouns", "verbs"=>"Verbs"][$part];
          $width = count($allCols[$part]);
          $tableString = "<section id='$part'><table><thead><tr><th colspan='$width'>$title</th></tr></thead><tbody>";
          
          foreach ($table as $row) {
            $newRow = [];
            foreach ($allCols[$part] as $col) {
              if ($col == "gender") {$col = ["n","m","f","c"][$row[$col]];}
              else {$col = $row[$col];}
              array_push($newRow,$col);
            }
            $tableString .= "<tr><td>" . join("</td><td>",$newRow) . "</td></tr>";
          }
          
          $tableString .= "<tr>";
          $first = " id='focus-$part'";
          foreach ($allCols[$part] as $col) {
            $tableString .= "<td><input$first type='text' name='${part}_$col'></td>";
            $first = "";
          }
          $tableString .= "</tr></tbody></table></section>";
          echo $tableString;
        }
        
      } catch (PDOException $e) {
        echo "$sql<br>" . $e->getMessage();
      }
      $conn = null;
      
      ?>
      <div id="submit"><input type="Submit"></div>
    <footer><p><a id="toTop" href="#top">Return to Top</a></p><hr id="bottom"></footer>
    
  </form>
  
  <script>
    window.onscroll = function() {
      if (document.documentElement.scrollTop < 225) {
        document.getElementById("toTop").style.display = "none";
      } else { // Alternatively ...scrollTop == 0
        document.getElementById("toTop").style.display = "block";
      }
    };
  </script>
  
</body>

</html>