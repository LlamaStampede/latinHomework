<!DOCTYPE html>

<html>

<head>
  <title>aiden - dictionary</title>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="input.css">
  <link rel="stylesheet" type="text/css" href="tabs.css">
</head>

<body>
  <form action="dictionary.php" method="post">
    <h1 id="dct"><a href="">Dictionary</a></h1>
    <input type="Submit">
    
    <label><input type="radio" name="part" id="tabA"><span>Adjectives</span></label>
    <label><input type="radio" name="part" id="tabN"><span>Nouns</span></label>
    <label><input type="radio" name="part" id="tabV"><span>Verbs</span></label>
    <script>
    //Code to make sections appear when tab clicked.
    </script>
      
      <?php
      $ids = ["adjs","nouns","verbs"];
      $names = [];
      $files = [];
      foreach ($ids as $part) {
        array_push($files,"../dictionary/".$part.".txt");
        if ($part == "adjs") {$part = "adjectives";}
        array_push($names,ucfirst($part));
      }
      for ($i = 0; $i < 3; $i++) {
        $len = [4,4,5][$i];
        $id = trim($ids[$i]);
        echo "<section id='".$id."'>";
        if ($_SERVER[REQUEST_METHOD] == "POST" and $_POST[$id.$len] != "") {
          $gloss = fopen("../dictionary/".$ids[$i].".txt", "a");
          $row = [];
          for ($j = 1; $j <= $len; $j++) {array_push($_POST[$id.$j]);}
          
          if ($_POST[$id."1"] == "") {$empty = array_shift($row);}
          fwrite($gloss, "\n" . implode("\t",$row));
          fclose($gloss);
        }
        
        $gloss = fopen("../dictionary/".$id.".txt", "r");
        echo "<table><tr><th colspan='".$len."'>".$names[$i]."</th></tr>";
        while (!feof($gloss)) {
          $row = explode("\t",fgets($gloss));
          if (sizeof($row) == 3) {array_unshift($row,"");}
          echo "<tr><td>" . implode("</td><td>",$row) . "</td></tr>";
        }
        echo "<tr>";
        for ($j = 1; $j <= $len; $j++) {echo "<td><input type='text' name='".$id.$j."'></td>";}
        echo "</tr></table></section>";
        fclose($gloss);
      }
      ?>
    </section>
  </form>
</body>

</html>