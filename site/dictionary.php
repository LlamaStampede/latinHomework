<!DOCTYPE html>

<html>

<head>
  <title>Dictionary</title>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="input.css">
  <link rel="stylesheet" type="text/css" href="tabs.css">
  <link rel="icon" href="../favicon/favicon.ico">
</head>

<body>
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
    var i, sections, tablinks;

    sections = document.getElementsByTagName("section");
    for (i = 0; i < sections.length; i++) {
        sections[i].style.display = "none";
    }

    tablinks = document.getElementsByClassName("tab");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].id = "";
    }

    document.getElementById(part).style.display = "block";
    evt.currentTarget.id = "active";
    document.getElementById('submit').style.display = "block";
}
  </script>
  
  <form action="dictionary.php" method="post">
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
          for ($j = 1; $j <= $len; $j++) {array_push($row,$_POST[$id.$j]);}
          
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
      <footer><hr id="bottom"><div id="submit"><input type="Submit"></div></footer>
  </form>
</body>

</html>