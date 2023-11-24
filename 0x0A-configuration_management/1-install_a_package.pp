# Manifest installs Flask version 2.1.0 using pip3.

class { 'python':
  version => 'system', # Ensure the system Python is used
}

package { 'python3-pip':
  ensure => 'installed',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
