# Automation: installs and configures Nginx with a custom HTTP header response

exec { 'update':
  command => '/usr/bin/apt-get update',
} ->

package { 'nginx':
  ensure => installed,
} ->

file_line { 'header_served_by':
  path     => '/etc/nginx/sites-available/default',
  match    => '^server {',
  line     => "server {\n\tadd_header X-Served-By \"${hostname}\";",
  multiple => false,
} ->

exec { 'restart_nginx':
  command => '/usr/sbin/service nginx restart',
}

