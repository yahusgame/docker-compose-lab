# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
  config.vm.hostname = "devops-node"
  config.vm.network "private_network", type: "dhcp"

  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.synced_folder "./docker-compose-lab", "/home/vagrant/compose-lab"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
    vb.cpus = 2
  end

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y docker.io
    systemctl enable docker 
    usermod -aG docker vagrant 
  SHELL
end
