<?php
  if(isset($_POST["Submit"])){
    if ($_POST['username'] == 'admin' && $_POST['password'] == 'password'){
        header("Location: benvenuto.php");
    }
  }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login PHP</title>
</head>
<body>
    <form method="POST">
        <input type="text" name="username" placeholder="username"><br>
        <input type="text" name="password" placeholder="password"><br>
        <input type="submit" name="Submit" value="Submit"><br>
    </form>
</body>
</html>
