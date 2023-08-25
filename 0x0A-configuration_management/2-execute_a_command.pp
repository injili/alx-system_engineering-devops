# A script that kills the process killmenow

exec { 'process_killer':
  command => 'usr/bin/pkill -f killmenow',
}
