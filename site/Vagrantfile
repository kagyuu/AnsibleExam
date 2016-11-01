# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "centos/7"

  config.vm.define "gitlab" do |server|
    server.vm.hostname = "gitlab"
#    server.vm.network "private_network", ip: "192.168.33.12", virtualbox__intnet: true
#
#    server.vm.network :forwarded_port, id: "ssh", guest: 22, host: 2222
#    server.vm.network "forwarded_port", guest: 80, host: 8080
#    server.vm.network "forwarded_port", guest: 443, host: 8443

    server.vm.network "public_network", bridge: "en0: Wi-Fi (AirPort)"
    server.vm.network :forwarded_port, id: "ssh", guest: 22, host: 2222
  end

  config.vm.define "redmine" do |server|
    server.vm.hostname = "redmine"
#    server.vm.network "private_network", ip: "192.168.33.13", virtualbox__intnet: true
#
#    server.vm.network :forwarded_port, id: "ssh", guest: 22, host: 2223
#    server.vm.network "forwarded_port", guest: 80, host: 9080
#    server.vm.network "forwarded_port", guest: 443, host: 9443

    server.vm.network "public_network", bridge: "en0: Wi-Fi (AirPort)"
    server.vm.network :forwarded_port, id: "ssh", guest: 22, host: 2223
  end

  config.vm.define "ldap" do |server|
    server.vm.hostname = "ldap"
#    server.vm.network "private_network", ip: "192.168.33.13", virtualbox__intnet: true
#
#    server.vm.network :forwarded_port, id: "ssh", guest: 22, host: 2224
#    server.vm.network "forwarded_port", guest: 80, host: 10080
#    server.vm.network "forwarded_port", guest: 389, host: 10389

    server.vm.network "public_network", bridge: "en0: Wi-Fi (AirPort)"
    server.vm.network :forwarded_port, id: "ssh", guest: 22, host: 2224
  end
end
