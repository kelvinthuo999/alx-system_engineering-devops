# Add capabilities for the user holberton

# Increase the hard limit
exec { 'increase-hard-limit':
  command => 'sed -i "/holberton hard/s/5/45000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increase the soft limit
exec { 'increase-soft-limit':
  command => 'sed -i "/holberton soft/s/5/45000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
