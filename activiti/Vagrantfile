# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "centos/7"

  config.vm.define "activiti" do |server|
    server.vm.hostname = "activiti"
    server.vm.network "forwarded_port", guest: 8080, host: 18080
    server.vm.network "forwarded_port", guest: 8443, host: 18443
    server.vm.network "forwarded_port", guest: 5432, host: 15432
  end
end
