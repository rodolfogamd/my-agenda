include apt

class system::sources {

  class { 'apt':
    purge  => {
      'sources.list'  => false,
      'source.list.d' => false,
      'preferences'   => false,
      'preferences.d' => false
    },
    update => {
      'frequency' => 'always',
      'timeout'   => undef
    }
  }
}

class system::essential {

  package { [
    'software-properties-common',
    'build-essential',
    ]:
    ensure => present
  }

}

class system::ppa {

  file { '/etc/apt/sources.list.d/multiverse.list':
    source => 'puppet:///modules/system/multiverse.list',
    owner  => 'root',
    group  => 'root',
    notify => Exec['apt_update']
  }

  apt::ppa { 'ppa:git-core/ppa': }

  package { [
    'git-core',
    'git',
    ]:
    ensure  => present,
    require => Exec['apt_update']
  }

}

class system::utilities {

  package { [
    'bindfs',
    'vim',
    'libssl-dev',
    'zlib1g-dev',
    'libbz2-dev',
    'libreadline-dev',
    'libsqlite3-dev',
    'libmysqlclient-dev',
    'wget',
    'curl',
    'llvm',
    'mcrypt',
    ]:
    ensure => present
  }

  package { [
    'python-dev',
    'python',
    'python-mysql.connector',
  ]:
    ensure => present
  }

  exec { 'install-pip':
    command => 'curl https://bootstrap.pypa.io/get-pip.py | python',
    path    => '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin',
    require => Package['python']
  }

}

class system {

  include system::sources
  include system::essential
  include system::ppa
  include system::utilities

}
