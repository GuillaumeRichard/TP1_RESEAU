<?php
include 'toolbar.php';

$errormsg = "";

if($_SERVER["REQUEST_METHOD"] === 'POST'){
    if(empty($_POST["email"]) || empty($_POST["title"])){
        $errormsg = "Vous devez remplir les champs Email et Titre.";
    }
    else{
        $errormsg = "Email envoyé!";
    }
}

?>
<link href="css/login.css" rel="stylesheet" type="text/css">

<form action="contact.php" method="POST">
    <label for="email">Email: </label><br/>
    <input id="email" type="text" name="email" /><br/>
    <label for="title">Titre: </label><br/>
    <input id="title" type="text" name="title" /><br/>
    <label for="description">Description: </label><br/>
    <textarea id="description" name="description"></textarea><br/>
    <input type="submit" value="Envoyer" />
</form>


<?php

if($errormsg != ""){
    echo "<p class='error'>".$errormsg."</p>";
}

?>