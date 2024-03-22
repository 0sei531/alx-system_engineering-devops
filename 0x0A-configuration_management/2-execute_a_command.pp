# Description: Kill a process called 'killmenow'
# Author: Your Name
# Date: March 22, 2024

exec { 'kill `killmenow` process':
  command => '/usr/bin/pkill -9 -f killmenow',
  onlyif  => '/usr/bin/pgrep -f killmenow',
}

