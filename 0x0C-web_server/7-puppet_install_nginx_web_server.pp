# Define package and service resources for Nginx
package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  hasstatus => true,
  hasrestart => true,
}

# Create index.html file with "Hello World!" content
file { '/var/www/html/index.html':
  ensure  => present,
  content => "Hello World!\n",
}

# Create Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "\
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html;
    location / {
        try_files \$uri \$uri/ =404;
    }
    location /redirect_me {
        return 301 http://www.example.com;
    }
}",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure Nginx is listening on port 80
file { '/etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

