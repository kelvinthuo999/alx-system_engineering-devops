# Add stable version of nginx
exec { 'add nginx stable repo':
  command => 'sudo add-apt-repository ppa:nginx/stable',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# Update software packages list
exec { 'update packages':
  command => 'apt-get update',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  require => Exec['add nginx stable repo'],
}

# Install nginx
package { 'nginx':
  ensure => 'installed',
  require => Exec['update packages'],
}

# Allow HTTP
exec { 'allow HTTP':
  command => "ufw allow 'Nginx HTTP'",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => '! dpkg -l nginx | egrep \'îi.*nginx\' > /dev/null 2>&1',
}

# Change folder rights
file { '/var/www':
  ensure => 'directory',
  mode   => '0755',
}

# Create index file
file { '/var/www/html/index.html':
  content => "Hello World!\n",
}

# Create 404 page
file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page\n",
}

# Add redirection and error page
file { '/etc/nginx/sites-enabled/default':
  ensure  => 'file',
  content => template('path/to/your/nginx_config.erb'),
  require => Package['nginx'],
}

# Restart nginx
service { 'nginx':
  ensure     => 'running',
  enable     => true,
  subscribe  => [Exec['add nginx stable repo'], Exec['update packages'], Package['nginx']],
}

# Notify exec to restart nginx if the configuration changes
exec { 'restart nginx':
  command   => 'service nginx restart',
  refreshonly => true,
  subscribe => File['/etc/nginx/sites-enabled/default'],
}
