# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

require "yaml"
# Load project config file
current_dir = File.dirname(File.expand_path(__FILE__))
vpdj_config = YAML.load_file("#{current_dir}/config.yaml")
connection  = vpdj_config['connection'][vpdj_config['connection']['use']]

# require additional plugins
unless Vagrant.has_plugin?("vagrant-bindfs")
  raise 'vagrant-bindfs is not installed! Type "vagrant plugin install vagrant-bindfs" to install.'
end

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    config.vm.box = "ubuntu/trusty64"
    config.vm.hostname = "#{vpdj_config['domain_name']}"

    config.vm.network "forwarded_port", guest: 22, host: 9831, auto_correct: true
    config.vm.network "forwarded_port", guest: 80, host: 9832, auto_correct: true
    config.vm.network "forwarded_port", guest: 3306, host: 9833, auto_correct: true
    config.vm.network "forwarded_port", guest: 8000, host: 9834, auto_correct: true

    config.ssh.port = 9831

    config.vm.network "private_network", type: "dhcp"
    config.vm.network "public_network",
        bridge: connection['interface'],
        ip: connection['public_ip']

    config.vm.provider "virtualbox" do |vb|
        vb.name = "#{vpdj_config['hostname']}"
        vb.memory = 1024
    end

    if Vagrant.has_plugin?("vagrant-vbguest")
        config.vbguest.auto_update = false
    end

    config.vm.synced_folder ".", "/vagrant", :nfs => true

    if Vagrant.has_plugin?("vagrant-puppet-install")
        config.puppet_install.puppet_version = "3.7.4"
    end

    if Vagrant.has_plugin?("vagrant-bindfs")
        config.bindfs.bind_folder "/vagrant", "/vagrant",
            :owner => "vagrant",
            :group => "www-data",
            :perms => "775"
    end

    config.vm.provision :puppet do |puppet|
        puppet.manifests_path = "puppet/provision/manifests"
        puppet.manifest_file = "default.pp"
        puppet.module_path = ["puppet/provision/modules","~/.puppet/modules"]
        puppet.hiera_config_path = "puppet/provision/hiera.yaml"
        puppet.facter = {
            "user"        => vpdj_config["user"],
            "domain_name" => vpdj_config["domain_name"],
        }
        puppet.options = "--verbose --graph --debug"
    end

    config.push.define "heroku" do |push|
        push.app = "my-agenda"
        push.remote = "heroku"
    end
end
