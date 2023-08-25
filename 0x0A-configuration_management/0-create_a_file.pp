# The script that creates a file.

file { '/tmp/school':
	mode => '744',
	owner => 'www-data',
	group => 'www-data',
	content => 'I love Puppet',
}
