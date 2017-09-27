<?php
include 'toolbar.php';

$errormsg = "";

if($_SERVER["REQUEST_METHOD"] === 'POST'){
    if(empty($_POST["user"]) || empty($_POST["password"])){
        $errormsg = "Vous devez remplir tout les champs.";
    }
    else{
        if($_POST["user"] != "admin"){
            $errormsg = "L'utilisateur ".$_POST["user"]." n'est pas valide.";
        }
        elseif($_POST["password"] != "royalcanin"){
            $errormsg = "Mot de passe invalide.";
        }
        else{
            $_SESSION["loggedIn"] = true;
            $_SESSION["user"] = $_POST["user"];
            header("Location: index.php");
        }
    }
}

?>
<link href="css/login.css" rel="stylesheet" type="text/css">

<form action="login.php" method="POST">
    <label for="user">Username: </label><br/>
    <input id="user" type="text" name="user" /><br/>
    <label for="password">Password: </label><br/>
    <input id="password" type="text" name="password" /><br/>
    <input type="submit" value="Login" />
</form>

<?php

    if($errormsg != ""){
        echo "<p class='error'>".$errormsg."</p>";
    }

?>
