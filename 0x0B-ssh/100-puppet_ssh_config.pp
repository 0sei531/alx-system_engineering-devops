# Set up SSH client configuration
file { '/etc/ssh/ssh_config':
  ensure  => file,
  content => template('ssh_config.erb'),
}

# Manage password authentication setting
file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}

# Manage identity file setting
file_line { 'Declare identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
}

