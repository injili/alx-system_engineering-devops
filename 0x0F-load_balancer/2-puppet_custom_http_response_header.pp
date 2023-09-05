# Puppet manifext cofiguration

# Install updates and nginx
exec { 'update':
	command => '/usr/bin/apt-get update',
}

# install package
package { 'nginx':
	ensure => installed,
}
-> Exec['update']

# replace file line
file_line { '/etc/nginx/nginx.conf':
	path  => '/etc/nginx/nginx.conf',
	line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
	match => 'http {',
}
-> Package['nginx']

# restart nginx
exec { 'start':
	command => '/usr/sbin/service nginx start',
}
-> File_line['/etc/nginx/nginx.conf']
