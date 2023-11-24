# Manifest: Kill a process called killmenow
exec { 'killmenow_process':
  command     => 'pkill -f killmenow',
  refreshonly => 'true',
}
