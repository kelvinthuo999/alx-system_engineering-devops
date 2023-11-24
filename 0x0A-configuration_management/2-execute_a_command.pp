# Manifest: Kill a process called killmenow
exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
