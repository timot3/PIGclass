<?php
  // Directory for file uploads
  $uploaddir = '/var/www/html/files/';

  // Random file name
  $rand = str_replace(".", "", uniqid('', true));
  $id = $rand . '.pdf';
  $uploadfile = $uploaddir . basename($id);

  // Upload files to Ubuntu server
  if (move_uploaded_file($_FILES['userfile']['tmp_name'], $uploadfile)) {
    // TODO: run the jar file to convert the pdf to json

    // Run Python script to upload to S3
    $command = escapeshellcmd('python3 /var/www/html/upload.py ' . $id);
    $output = shell_exec($command);
    echo $output;

    // Redirect to complete page
    header('Location: uploadComplete.html?' . $rand);
  } else {
     header('Location: error/uploadFailed.html');
  }
?>
