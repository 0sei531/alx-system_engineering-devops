# Description: Create a file in /tmp with specific permissions, owner, and content
# Author: Your Name
# Date: March 22, 2024

file { '/tmp/school':
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => "I love Puppet\n",
}

