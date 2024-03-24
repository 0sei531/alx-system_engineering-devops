# Set up SSH client configuration
file { '/etc/ssh/ssh_config':
  ensure  => file,
  content => template('ssh_config.erb'),
}

# Template for SSH client configuration
# /etc/ssh/ssh_config.erb
# Standard SSH client configuration

# Turn off password authentication
<% if file_line['Turn off passwd auth'] == 'ensure' -%>
PasswordAuthentication no
<% end -%>

# Specify identity file
<% if file_line['Declare identity file'] == 'ensure' -%>
IdentityFile ~/.ssh/school
<% end -%>

