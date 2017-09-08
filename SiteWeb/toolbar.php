<?php
session_start();
?>

<a href="index.php">Home</a>
<a href="contact.php">Contact</a>
<a href="recherche.php">Recherche</a>

<?php
    if(isset($_SESSION["loggedIn"])){
        echo "<a href=\"profile.php\">Profile</a> ";
        echo "<a href=\"logout.php\">Logout</a>";
    }
    else {
        echo "<a href=\"login.php\">Login</a>";
    }
?>

<br />