# Puppet manifest to install and configure Nginx with a custom HTTP header

package { 'nginx':
  ensure  => 'installed',
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {\n    listen 80 default_server;\n    add_header X-Served-By ${::hostname};\n}\n",
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
}
