# A script that kills the process killmenow

exec { 'process_killer':
  command => 'pkill -f killmenow',
}
