include apache
include apache::mod::wsgi

class webserver::sources {

  class { "apache":
    default_mods        => true,
    default_confd_files => true,
    default_vhost       => false,
  }

  apache::mod { 'rewrite': }
  apache::mod { 'actions': }
  #apache::mod { 'wsgi': }
  apache::mod { 'ssl': }

  class { 'apache::mod::wsgi':
    wsgi_python_home => "/home/${user}/virtualenvs/${domain_name}",
    wsgi_python_path => "/home/${user}/virtualenvs/${domain_name}/site-packages"
  }

  apache::vhost { "${domain_name}":
    servername          => "${domain_name}",
    port                => '80',
    ip                  => '*',
    docroot             => '/vagrant/agenda',
    docroot_owner       => 'vagrant',
    docroot_group       => 'www-data',
    error_log           => true,
    error_log_file      => 'project.log',
    access_log          => true,
    access_log_file     => '/var/log/apache2/project-access.log',
    wsgi_daemon_process => 'wsgi',
    wsgi_import_script  => '/vagrant/agenda/wsgi.py',
    wsgi_process_group  => 'wsgi',
    wsgi_script_aliases => {
      '/' => '/vagrant/agenda/wsgi.py'
    },
    wsgi_chunked_request => 'On',
  }

}

class webserver {

  include webserver::sources

}
