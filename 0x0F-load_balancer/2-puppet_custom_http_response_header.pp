# Define a class to manage custom HTTP header configuration
class custom_http_response_header {

  # Install nginx package
  package { 'nginx':
    ensure  => installed,
    require => Package['apt'],
  }

  # Define the custom nginx configuration
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('load_balancer/nginx_custom_header.erb'),
    notify  => Service['nginx'],
  }

  # Ensure nginx service is running and enabled
  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/sites-available/default'],
    require   => Package['nginx'],
  }
}

