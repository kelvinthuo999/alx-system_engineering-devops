# Manifest: Install Flask using pip3

class { 'python':
  version => 'system',
}
package { 'python3-pip':
  ensure => 'installed',
}
exec { 'install_flask':
  command     => '/usr/bin/pip3 install Flask==2.1.0',
  path        => '/usr/local/bin:/usr/bin:/bin',
  refreshonly => 'true',
  subscribe   => 'Package['python3-pip']',
}
