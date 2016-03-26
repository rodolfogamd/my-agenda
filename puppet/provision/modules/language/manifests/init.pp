
class language::essential {

  # Prepare user's project directories
  file { [
    "/home/${user}/virtualenvs",
  ]:
    ensure  => directory,
    owner   => "${user}",
    group   => "${user}",
    before  => Package['virtualenv'],
    require => Class['system']
  }

  package { [
    'virtualenv',
    'virtualenvwrapper'
  ]:
    ensure   => present,
    provider => pip,
    require  => Class['system']
  }

  exec { 'create virtualenv':
    command => "virtualenv --always-copy ${domain_name}",
    path    => '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin',
    cwd     => "/home/${user}/virtualenvs",
    user    => $user,
    require => Package['virtualenv']
  }

  # Copy requirements files
  file { "/home/${user}/virtualenvs/${domain_name}/requirements.txt":
    ensure  => file,
    source  => 'puppet:///modules/language/requirements.txt',
    owner   => "${$user}",
    group   => "${$user}",
    require => Exec['create virtualenv']
  }
  
  file { "/home/${user}/virtualenvs/${domain_name}/local.txt":
    ensure  => file,
    source  => 'puppet:///modules/language/local.txt',
    owner   => "${$user}",
    group   => "${$user}",
    require => Exec['create virtualenv']
  }

}

class language {

  include language::essential

}
