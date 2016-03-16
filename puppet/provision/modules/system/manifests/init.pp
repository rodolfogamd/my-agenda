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

  apt::source { "ubuntu_trusty":
        location => "http://archive.ubuntu.com/ubuntu/",
        release  => "trusty",
        repos    => "main restricted universe multiverse",
    }

    apt::source { "ubuntu_trusty-updates":
        location => "http://archive.ubuntu.com/ubuntu/",
        release  => "trusty-updates",
        repos    => "main restricted universe multiverse",
    }

    apt::source { "ubuntu_trusty-security":
        location => "http://archive.ubuntu.com/ubuntu/",
        release  => "trusty-security",
        repos    => "main restricted universe multiverse",
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
