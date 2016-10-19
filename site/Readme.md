Project management site recipe (SORRY UNDER COUNSTRUCTION NOW!)
======================
This is an ansible-playbook for building project management site.
This playbook creates following services on CentOS7 (or RHEL7 family):
- [GitLab Community Edition](http://www.gitlab.com) 8.12
- [Redmine](http://www.redmine.org) 3.2
- [Jenkins](https://jenkins.io) 2.26
- [Alfresco Community Edition](https://www.alfresco.com) 5.1
- [OpenLDAP](www.openldap.org/) 2.4.44

You don't need to build full of them. You can build some of them that you want to use.

Usage
------
### 1. Prepare IA64 Server ###

- At the start point, you need to prepare 5 minimum installed CentOS7s as the base of services. The Ansible requires that these machines has sshd service and python2. We recommend thease machines are real machines or virtual machines on the cloud service such as inhouse OpenStack or AWS.

- But instantly, you can use Vagrantfile to build VMs for trial use or small project.
  1. Install [Oracle VM VirtualBox](https://www.virtualbox.org/) and [Vagrant by HashiCorp](https://www.vagrantup.com/) on your machine.
  1. Modify Vagrantfile
    - This Vagrantfile creates VMs thease are connectd to the public network (LAN) toward physical NIC. So, you must change NIC name for bridge on the Vagrantfile, if your machine is not Macbook Pro. You can also delete the NIC name, if do so, Vagrant ask you select NIC during `vagrant up` command.
    - This Vagrantfile supposed that the ip address of a VM is supplied from DHCP server, and you can lookup VMs by mDNS (avahi/apple's bonjour). So, if you want to change network settings, you must rewrite Vagrantfile drastically.
  1. Wakeup VMs
    - Wakeup all VMs. `$ vagrant up`
    - Wakeup an individual VM.`$ vagrant up redmine`

### 2. Access settings for Ansible ###

- If you use Vagrant, you need not modify access settings.
- group_vars/vagrant.yml

      ---
      ansible_ssh_user: vagrant

- host_vars/gitlab.yml

      ---
      ansible_ssh_host: 127.0.0.1
      ansible_ssh_port: 2222
      ansible_ssh_private_key_file: .vagrant/machines/gitlab/virtualbox/private_key

- host_vars/gitlab.yml

      ---
      ansible_ssh_host: 127.0.0.1
      ansible_ssh_port: 2223
      ansible_ssh_private_key_file: .vagrant/machines/redmine/virtualbox/private_key

      db_passwd_redmine : a9EtesfPqJm3

- (if you need proxy settings,) delete comment out mark "#" on proxy.yml and modify it.

      ---
      #http_proxy_host: proxy.foo.com
      #http_proxy_port: 3128
      #http_proxy_username: john@foo.com
      #http_proxy_password: password

      #http_proxy: http://{{ http_proxy_host }}:{{ http_proxy_port }}
      #http_proxy: http://{{ http_proxy_username | urlencode() }}:{{ http_proxy_password }}@{{ http_proxy_host }}:{{ http_proxy_port }}

      proxy_env :
        no_proxy: 127.0.0.1,localhost
        http_proxy: "{{ http_proxy | default(None) }}"
        https_proxy: "{{ http_proxy | default(None) }}"

### 3. Download commercial plugins ###

- see [Redmine Commercial Free plugins](#redmine_plugins)

### 4. Install services ###

- Setup all services. `$ ansible-playbook site.yml`
- Setup individual service. `$ ansible-playbook site.yml -l redmine`
- If you fail to connect ssh, try `$ ansible-playbook -c paramiko site.yml`. "-c paramiko" means use "paramiko" Python module for ssh connection instead of OpenSSH clinet.

Details
----------------
### Gitlab ###

### Redmine ###

- Free plugins
  - Thease are automatically installed by ths ansible-playbook
  - RM+ Coomon library
    - https://bitbucket.org/dkuk/a_common_libs.git
  - Knowledgebase
    - https://github.com/alexbevi/redmine_knowledgebase.git
  - Time logger
    - https://github.com/speedy32129/time_logger.git
  - Default Custome Query
    - https://github.com/hidakatsuya/redmine_default_custom_query.git
  - Issue Template
    - https://github.com/akiko-pusu/redmine_issue_templates.git
  - Backlogs (Kanban)
    - https://github.com/backlogs/redmine_backlogs.git
  - Lightbox2
    - https://github.com/paginagmbh/redmine_lightbox2.git
  - Theme Changer
    - https://bitbucket.org/haru_iida/redmine_theme_changer
  - Local Avator
- <a name="redmine_plugins"> Commercial Free plugins </a>
  - <span style="color:red">Thease are free, but you need to register email and downlowd zip files.</span>
  - Easy Gantt

### OpenLDAP ###

### Jenkins ###

### Alfresco ###

License
----------
Copyright &copy; 2016 A.HO
Licensed under the  [MIT License][mit].

[MIT]: http://www.opensource.org/licenses/mit-license.php
