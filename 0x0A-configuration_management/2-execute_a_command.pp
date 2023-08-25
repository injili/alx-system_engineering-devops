# A script that kills the process killmenow

exec {
  command => 'pkill -f killmenow',
}
