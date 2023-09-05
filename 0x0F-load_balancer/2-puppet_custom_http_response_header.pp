# Puppet manifext cofiguration

# Install updates and nginx
exec { 'update':
	command => '/usr/bin/apt-get update',
}

# install package
package { 'nginx':
	ensure => installed,
}

# replace file lin
file _line { '/etc/nginx/nginx.conf':
	path  => '/etc/nginx/nginx.conf',
	line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
	match => 'http {',
}

# restart nginx
exec { 'start':
	command => 'usr/sbin/service nginx start',
}
