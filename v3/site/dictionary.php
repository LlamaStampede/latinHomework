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
        <li><span class="a">Dream of Scipio</span>
            <ul>
                <li><a href="chapter16.php">Chapter 16</a></li>
                <li><a href="chapter17.php">Chapter 17</a></li>
                <li><a href="chapter18.php">Chapter 18</a></li>
                <li><a href="chapter19.php">Chapter 19</a></li>
                <li><a href="chapter20.php">Chapter 20</a></li>
            </ul>
        </li>
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
      $names = [];
      $files = [];
      foreach ($ids as $part) {
          array_push($files, "../dictionary/".$part.".txt");
          if ($part == "adjs") {
              $part = "adjectives";
          }
          array_push($names, ucfirst($part));
      }
      for ($i = 0; $i < 3; $i++) {
          $part = $ids[$i];
          $len = [4,4,5][$i];
          $id = trim($part);
          echo "<section id='".$id."'>";
          if ($_SERVER[REQUEST_METHOD] == "POST" and $_POST[$id.$len] != "") {
              $gloss = fopen("../dictionary/$part.txt", "a");
              $row = [];
              for ($j = 1; $j <= $len; $j++) {
                  array_push($row, $_POST[$id.$j]);
              }
          
              if ($_POST[$id."1"] == "") {
                  $empty = array_shift($row);
              }
              fwrite($gloss, "\n" . implode("\t", $row));
              fclose($gloss);
          }
        
          $gloss = fopen("../dictionary/".$id.".txt", "r");
          echo "<table><tr><th colspan='".$len."'>".$names[$i]."</th></tr>";
          while (!feof($gloss)) {
              $row = explode("\t", fgets($gloss));
              if (sizeof($row) == 3) {
                  array_unshift($row, "");
              }
              echo "<tr><td>" . implode("</td><td>", $row) . "</td></tr>";
          }
          echo "<tr>";
          $first = " id='focus-$part'";
          for ($j = 1; $j <= $len; $j++) {
              echo "<td><input$first type='text' name='$id$j'></td>";
              $first = "";
          }
          echo "</tr></table></section>";
          fclose($gloss);
      }
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