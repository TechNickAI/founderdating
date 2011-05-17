<?php
ini_set('error_reporting', E_ALL);
$dbnew = mysql_connect('localhost', 'founderdating', 'cofounder');
if (!$dbnew) {
    die('Could not connect: ' . mysql_error());
}
mysql_select_db('founderdating', $dbnew);

function resetdb($db){
	mysql_query("TRUNCATE TABLE profiles_fdprofile", $db) || die(mysql_error($db));
	mysql_query("TRUNCATE TABLE profiles_recommendation", $db) || die(mysql_error($db));
	mysql_query("TRUNCATE TABLE profiles_linkedinprofile", $db) || die(mysql_error($db));
	mysql_query("TRUNCATE TABLE profiles_applicant", $db) || die(mysql_error($db));
	mysql_query("DELETE FROM auth_user WHERE id > 3", $db) || die(mysql_error($db));
};

resetdb($dbnew);

// Stuff to figure out
// how to populate initial mugshots?
// what to set initial privacy to
// create auth_user account?
// set all applicants to "past event"?

$dbold = mysql_connect('localhost', 'root', '');
if (!$dbold) {
    die('Could not connect: ' . mysql_error());
}
mysql_select_db('oldfd', $dbold);

$user_id = 3;

// Applicants
$results = mysql_query("SELECT 
	a.submitted,
	a.status,
	COALESCE(u.name, a.name) AS name,
	COALESCE(u.email, a.email) AS email,
	event,
	serialized,
	assigned_user_id,
	username,
	password,
	linkedin_oauth_object,linkedin_profile_raw, linkedin_connections_raw,
	linkedin_profile_picture, linkedin_profile_industry, linkedin_profile_location,
	last_login,
	hide
	FROM applications AS a
	LEFT OUTER JOIN users AS u ON a.assigned_user_id = u.id", $dbold);
if (! $results ) {
    die('mysql error: ' . mysql_error($dbold));
}
$profile_id= 0;
while($row = mysql_fetch_assoc($results)){
	$created_at = date('Y-m-d H:i:s', $row['submitted']);
	switch ($row['status']){
	  case 2: $event_status = 'denied' ; break;
	  case 1: $event_status = 'accepted and attending' ; break;
	  default: $event_status = 'pending'; break;
	} 

	if (preg_match('/San Fran/i', $row['event'])){
		$event_id = 3;
	} else if (preg_match('/seattle/i', $row['event'])){
		$event_id = 4;
	} else  {
		echo "Unrecoginzed event: " . $row['event'];
		continue;
	}
	$user_id++;
	$profile_id++;
	$mugshot = ''; //XXX
	if ($row['hide'] == 1) {
		$privacy = 'closed';
	} else {
		$privacy = 'registered'; 
	}

	if (empty($row['assigned_user_id'])){
		$my_user_id = -1;
	} else {
		$my_user_id = $user_id;
		$sql = "INSERT INTO auth_user VALUES($my_user_id," .
			"'" . mysql_escape_string($row['username']).  "', " .
			"'" . mysql_escape_string($row['name']).  "', " .
			"''," .  // lastname
			"'" . mysql_escape_string($row['email']).  "', " .
			"'" . mysql_escape_string($row['password']).  "', " .
			"0,1,0," . // staff/active/super_user
			"'" .  date('Y-m-d H:i:s', $row['last_login']) . "'," .
			"'$created_at'" .
			")";
		mysql_query($sql, $dbnew) || die ($sql . " " .mysql_error($dbnew));

		// profiles
		$sql = "INSERT INTO profiles_linkedinprofile VALUES(NULL, $profile_id, ".
			"'" . mysql_escape_string($row['linkedin_oauth_object']) . "'," .
			"'" . mysql_escape_string($row['linkedin_profile_raw']) . "'," .
			"'" . mysql_escape_string($row['linkedin_profile_picture']) . "'," .
			"'" . mysql_escape_string($row['linkedin_profile_location']) . "'," .
			"'" . mysql_escape_string($row['linkedin_profile_industry']) . "'," .
			"'$created_at', " .
			"now()," .
			"'" . mysql_escape_string($row['linkedin_connections_raw']) . "'" .
			")";
		mysql_query($sql, $dbnew) || die (substr($sql, 0, 200). " " . mysql_error($dbnew));
	}



	// PHP serialized blog, we need the data and to have in in JSON
	$obj = unserialize(stripslashes($row['serialized']));
	if ($obj === false ){
		echo "Trying to fix...\n";
		$new = preg_replace('/[^(\x00-\x7F)]/', 'XX', $row['serialized']);
		$obj = unserialize($new);
		if ($obj === false ){
			print "error deserializing "; var_export($row['serialized']);
			continue;
		}
	}
	switch($obj['can_start']){
	  case 'Immediately': $can_start = 'immediately'; break;
	  case 'Part-time now, full-time soon': $can_start = 'part now full soon'; break;
	  case 'Part-time now, full-time if it takes off': $can_start = 'part now full if no suck'; break;
	  case "I don't have much for the next several months": $can_start = 'later'; break;
	  case "I don’t have much for the next several months": $can_start = 'later'; break;
	  default: echo "Unrecognized can_start:" . $obj['can_start']; continue;
	}
	switch ($obj['classify']){
	  case "I have an idea that I'm committed to": $idea_status = 'straight'; break;
	  case "I have and idea, but I'm also open to exploring other ideas": $idea_status = 'curious'; break;
	  case "I don't yet have an idea": $idea_status = 'ambiguous'; break;
	  default: print_r($obj); echo "Unrecognized classify:" . $obj['classify']; continue;
	}

	// Interests
	$interests = @$obj['areas_of_interest'];
	if (!empty($obj['areas_of_interest_more'])){
		foreach(explode(',', $obj['areas_of_interest_more']) as $other_interest){
			$interests[] = trim($other_interest);
		}
	}

	if (empty($row['assigned_user_id'])){
		$sql = "INSERT INTO profiles_applicant VALUES(NULL, " .
			"'" . mysql_escape_string($row['name']).  "', " .
			"'" . mysql_escape_string($row['email']).  "', " .
			"'$created_at', " .
			"'$created_at', " .
			"'" . mysql_escape_string(json_encode($obj['primary_skillsets'])) . "', " .
			"'" . mysql_escape_string(json_encode($obj['partner_skillsets'])) . "', " .
			"'" . mysql_escape_string(json_encode($interests)) . "', " .
			"'" . mysql_escape_string($obj['past_experience']).  "', " .
			"'" . mysql_escape_string($obj['bring']) . "', " .
			"'$can_start', " .
			"'$idea_status', " .
			"'" . mysql_escape_string($obj['linkedin']) . "'," .
			"'$event_id', " .
			"'$event_status', " .
			"'" . mysql_escape_string(json_encode(@$obj['recommend'])) . "'" .
			")";
		mysql_query($sql, $dbnew) || die ($sql . " " .mysql_error($dbnew));
	} else {
		$sql = "INSERT INTO profiles_fdprofile VALUES($profile_id, $my_user_id, '$mugshot', '$privacy', $event_id," . 
			"'" . mysql_escape_string(json_encode($obj['primary_skillsets'])) . "', " .
			"'" . mysql_escape_string(json_encode($obj['partner_skillsets'])) . "', " .
			"'" . mysql_escape_string($obj['past_experience']).  "', " .
			"'" . mysql_escape_string($obj['bring']) . "', " .
			"'$can_start', " .
			"'$idea_status', " .
			"'$event_status', " .
			"'$created_at', " .
			"now()," .
			"'" . mysql_escape_string(json_encode($interests)) . "', " .
			"'" . mysql_escape_string($obj['linkedin']) . "'" .
			")";
		mysql_query($sql, $dbnew) || die ($sql . " " .mysql_error($dbnew));

		// Recommendations
		if (!empty($obj['recommend'])){
			foreach($obj['recommend'] as $r) {
				$sql = "INSERT INTO profiles_recommendation VALUES(NULL, $profile_id," .
					"'" . mysql_escape_string($r['name']) . "'," . 
					"'" . mysql_escape_string($r['email']) . "')";
				mysql_query($sql, $dbnew) || die ($sql . " " .mysql_error($dbnew));
			}
		}
	}

	//unset($row['linkedin_profile_raw']);
	//unset($row['linkedin_connections_raw']);
	//print_r($row);	
	//exit;
	echo $row['email'] . " inserted" . "\n";
}
echo "Done";
