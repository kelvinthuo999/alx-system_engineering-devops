# File: custom_header_setup.pp

class custom_header_setup {

  $custom_header_name = 'X-Served-By'
  $custom_header_value = $::hostname

  # Install Nginx package
  class { 'nginx':
    manage_repo => true,
  }

  # Define the default site configuration
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('custom_header_setup/default_site.erb'),
    require => Class['nginx'],
    notify  => Service['nginx'],
  }

  # Define the Nginx service
  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => File['/etc/nginx/sites-available/default'],
  }

}

# File: templates/default_site.erb

server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;
    add_header <%= @custom_header_name %> <%= @custom_header_value %>;
    location / {
        try_files $uri $uri/ =404;
    }
    location /redirect_me {
        rewrite ^ https://youtube.com/watch?v=QH2-TGUlwu4 permanent;
    }
    error_page 404 /404.html;
    location = /404.html {
        internal;
    }
}
