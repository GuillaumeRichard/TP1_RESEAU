<?php
include 'toolbar.php';


if($_SERVER["REQUEST_METHOD"] === 'POST'){
    if(empty($_POST["search"])){
        $errormsg = "Impossible de rechercher le néan";
    }
    else{
        $errormsg = "Aucun résultat pour ".$_POST["search"];
    }
}

?>

<form action="recherche.php" method="POST">
    <label for="search">Recherche: </label><br/>
    <input id="search" type="text" name="search" /><br/>
    <input type="submit" value="Recherche" />
</form>


<?php

if($errormsg != ""){
    echo "<p class='error'>".$errormsg."</p>";
}

?>