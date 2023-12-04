# Puppet manifest to install and configure Nginx with a custom HTTP header

# Ensure apt is up-to-date
package { 'apt-update':
  ensure => latest,
}

# Install Nginx
package { 'nginx':
  ensure => installed,
  require => Package['apt-update'],
}

# Custom HTTP header value
$custom_header_value = $facts['hostname']

# Define Nginx site configuration with custom HTTP header
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;
    add_header X-Served-By $custom_header_value;
    location / {
        try_files \$uri \$uri/ =404;
    }
    location /redirect_me {
        rewrite ^ https://youtube.com/watch?v=QH2-TGUlwu4 permanent;
    }
    error_page 404 /404.html;
    location = /404.html {
        internal;
    }
}",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Nginx service configuration
service { 'nginx':
  ensure  => running,
  enable  => true,
}

# Notify systemd to reload Nginx when the site configuration changes
exec { 'reload_nginx':
  command     => 'systemctl reload nginx',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}
