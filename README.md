Introduction
===========

Building an API with Vagrant, Puppet or standalone with Django.

# Without vagrant

1. Install mysql server
2. Install python and pip
3. Create a virtualenv
4. Activate the virtualenv with the following command
`source (virtualenv)/bin/activate`
5. Run the command:
`pip install -r puppet/provision/modules/language/files/local.txt`
6. Verify all the packages with yolk:
`yolk -l`
7. Modify manage.py like 'Run the application' section

# Using Vagrant

## Prerequisites

+ [Vagrant](http://www.vagrantup.com/downloads.html)
+ [Vagrant BindFS](https://github.com/gael-ian/vagrant-bindfs)
+ [Vagrant Puppet Install](https://github.com/petems/vagrant-puppet-install)

Modules for puppet:

+ puppetlabs-apache v1.5.0
+ puppetlabs-apt v2.1.1
+ puppetlabs-mysql v3.4.0
+ puppetlabs-reboot v1.1.0

To install puppet modules, execute the following command:

+ `puppet module install puppetlabs-apache`
+ `puppet module install puppetlabs-apt`
+ `puppet module install puppetlabs-mysql`
+ `puppet module install puppetlabs-reboot`

To install vagrant plugins, execute the following command:

+ `vagrant plugin install vagrant-bindfs`
+ `vagrant plugin install vagrant-puppet-install`
+ `vagrant plugin install vagrant-vbguest`

## Getting Started

This is a fairly simple project to get up and running.
The procedure for starting up is as follows:

1. Clone the project. (There’s only master branch.)
2. Run the command `vagrant up` from the directory
3. Open your browser to http://localhost:9834

## Run the application

1. Modify the following line at manage.py:
+ `os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BFA_Agenda.settings")`
For local development:
+ `os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BFA_Agenda.settings.local")`
For production:
+ `os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BFA_Agenda.settings.production")`

For changing this manual change, we need to use virtualenvwrapper.

2. For running the application the first time:
`python manage.py migrate`

3. For running django server
`python manage.py runserver 0.0.0.0:8000`
