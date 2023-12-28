<head>
        <meta http-equiv="content-type" content="text/html">
        <meta charset="UTF-16">
        <meta name="generator" content="WebSite PRO 4.3">
        <title>JS</title>
		<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
  <div id="Main">
  <?php include 'header.php';?>
  <div id ="info">
  <center>
    <h2> Contact </h2>
</center>
    <p> If you must...</p>
    <a href="https://www.youtube.com/channel/UCf6hxjn9Dpwhi3BdtQXvQTw">
  <img src="YouTube-Icon-Full-Color-Logo.wine.svg" alt="" style="width:128px;height:128px;">
</a>
<a href="https://github.com/freq-mod">
  <img src="25231.png" alt="" style="width:128px;height:128px;">
</a>
<br>
<center>
    <h3> E-mail </h3>
</center>
<p> Solve the following:</p> <br>
<p> Ball and paddle cost 1.10 USD altogether. The paddle is 1 USD more expensive than the ball. How much does the ball cost? <small> note for retards: 1 usd = 100 cents </small><p>
<form action="contact.php" method="post">
<input type="text" name="inputbox" value="0" />
<input type="submit">
</form>
<?php
$inputval = @$_POST["inputbox"];
if ($inputval==5 or $inputval==0.05)
echo "nwd937172@gmail.com";
elseif ($inputval==0) echo "";
else  echo "jubao@people.cn";
?>
</div>
</div>
</body>
</html>