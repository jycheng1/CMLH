<?php
include('../../secureHtdocs/conn.php'); // connect to socius database
$data_missing = array();

// deals with comments
  // trim white space
  $comm = trim($_POST['comments']);

// deals with org name box
  if(empty($_POST['organization'])){
    // Add org name to array
    $data_missing[] = 'organization';  
  } else{
    // trim white space
    $org = trim($_POST['organization']);
  }

// deals with address box
  if(empty($_POST['address'])){
    // Add address to array
    $data_missing[] = 'address';  
  } else{
    // trim white space
    $add = trim($_POST['address']);
  }
// deals with request dropdown
  if($_POST['request'] == "sel"){
    // add request to array
    $data_missing[] = 'request';  
  } else{
    // trim white space
    $req = trim($_POST['request']);
  }

// enters this if no data is missing
  if(empty($data_missing)){
    $a = array();
 
    // insert into sql database
    
    $query = "INSERT INTO resources(requestDate, request, organization, 
            address, comments, lattitude, longitude, priority)  
            VALUES (NOW(), ?, ?, ?,?,0,0,1)";

    $query1 = "UPDATE reqAgg SET quantity = quantity + 1 WHERE request = ?";

    $stmt = mysqli_prepare($conn, $query);
    $stmt1 = mysqli_prepare($conn, $query1);
    mysqli_stmt_bind_param($stmt, "ssss", $req, $org, $add, $comm);
    mysqli_stmt_bind_param($stmt1, "s", $req);
    mysqli_stmt_execute($stmt);
    mysqli_stmt_execute($stmt1);
    $affected_rows = mysqli_stmt_affected_rows($stmt);

    if(!$affected_rows == 1){
      echo 'Error Occured<br />';
      echo mysqli_error();
      mysqli_stmt_close($stmt);
      mysqli_close($conn);
    }
    mysqli_close($conn);

    $a = array( 'isFilled' => true,
        'message' => "none");

  }
  // missing data is not empty, so you have missing form elements
  else{
    $message = "You need to enter the following data: \n";
    foreach($data_missing as $missing){
      $message = $message . $missing . "\n";
    }
    $a = array( 'isFilled' => false,
      'message' => $message);
    mysqli_close($conn);
  }
  echo json_encode($a);
?>
