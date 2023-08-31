# Puppet manifest configuration

# Install Nginx package
package { 'nginx':
	ensure => installed,
}

# Configure index.html
file { '/var/www/html/index.html':
	ensure  => file,
	content => 'Hello World!',
	require => Package['nginx'],
}

# Configure redirect_me
file { '/etc/nginx/sites-available/default':
	ensure  => file,
	content => "
server {
	listen 80;
	listen [::]:80 default_server;

	server_name _;

	location / {
		root /var/www/html;
		index index.html index.htm;
	}

	location /redirect_me/ {
		return 301 https://github/injili;
	}

}
",
	require => Package['nginx'],
	notify  => Service['nginx'],
}

# Restart Nginx
service { 'nginx':
	ensure  => running,
	enable  => true,
	require => Package['nginx'],
}
