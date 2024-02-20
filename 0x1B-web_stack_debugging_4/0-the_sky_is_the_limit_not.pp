# Adjusting ULIMIT for Nginx to handle more traffic.

# Fix ULIMIT for Nginx
exec { 'fix-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

# Restart Nginx
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
