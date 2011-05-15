<?php 
ini_set('error_reporting', E_ALL|E_STRICT);
ini_set('display_errors', 'on');


/**
 * Pulled from old founder dating code for generating passwords
 */
class Auth_Core {

	public $salt_pattern = Array('1','3', '5', '9', '14', '15', '20', '21', '28', '30');

	/**
	 * Creates a hashed password from a plaintext password, inserting salt
	 * based on the configured salt pattern.
	 *
	 * @param   string  plaintext password
	 * @return  string  hashed password string
	 */
	public function hash_password($password, $salt = FALSE)
	{
		if ($salt === FALSE)
		{
			// Create a salt seed, same length as the number of offsets in the pattern
			$salt = substr($this->hash(uniqid(NULL, TRUE)), 0, count($this->salt_pattern));
		}

		// Password hash that the salt will be inserted into
		$hash = $this->hash($salt.$password);

		// Change salt to an array
		$salt = str_split($salt, 1);

		// Returned password
		$password = '';

		// Used to calculate the length of splits
		$last_offset = 0;

		foreach ($this->salt_pattern as $offset)
		{
			// Split a new part of the hash off
			$part = substr($hash, 0, $offset - $last_offset);

			// Cut the current part out of the hash
			$hash = substr($hash, $offset - $last_offset);

			// Add the part to the password, appending the salt character
			$password .= $part.array_shift($salt);

			// Set the last offset to the current offset
			$last_offset = $offset;
		}

		// Return the password, with the remaining hash appended
		return $password.$hash;
	}

	/**
	 * Perform a hash, using the configured method.
	 *
	 * @param   string  string to hash
	 * @return  string
	 */
	public function hash($str) {
		return hash('sha1', $str);
	}

        public function find_salt($password)
        {
                $salt = '';

                foreach ($this->salt_pattern as $i => $offset)
                {
                        // Find salt characters, take a good long look...
                        $salt .= $password[$offset + $i];
                }

                return $salt;
        }


} // End Auth

if (sizeof($argv) == 2){
	$Auth = new Auth_Core();
	echo $Auth->hash_password($argv[1]);
} else if (sizeof($argv) == 3){
	$Auth = new Auth_Core();
	$salt = $Auth->find_salt($argv[2]);
	$new_hash = $Auth->hash_password($argv[1], $salt);
	if ($argv[2] == $new_hash){
		echo "valid";
		exit(0);
	} else {
		echo "invalid " . $argv[2] . " != ". $new_hash;
		exit(1);
	}
} else {
	echo 'Usage: ' .  $argv[0] . ' $password [$hash], and it will print valid or invalid, along with 0/1 for the exit code. If only one argument is supplied, it just prints the hash for that password' . "\n";
	exit(1);
}
