# Configure server using puppet script
file { '/etc/ssh/ssh_config':
  ensure  => 'present',
  content => '
Host *
    HostName 100.25.104.64
    User ubuntu
    IdentityFile ~/.ssh/school
    PreferredAuthentications publickey
    PasswordAuthentication no
',
  mode    => '0600',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}
