Project management site recipe (SORRY UNDER COUNSTRUCTION NOW!)
======================
This is an ansible-playbook for building project management site.
This playbook creates following services on CentOS7 (or RHEL7 family):
- [GitLab Community Edition](http://www.gitlab.com) 8.12
- [Redmine](http://www.redmine.org) 3.2
- [Jenkins](https://jenkins.io) 2.26
- [Alfresco Community Edition](https://www.alfresco.com) 5.1
- [OpenLDAP](www.openldap.org/) 2.4.44
- [PWM](https://github.com/pwm-project/pwm) 1.8

You don't need to build full of them. You can build some of them that you want to use.

Usage
------
### 1. Prepare IA64 Server ###

- At the start point, you need to prepare 5 minimum installed CentOS7s as the base of services. The Ansible requests that these machines has sshd service and python2. We recommend these machines are real machines or virtual machines on the cloud service such as inhouse OpenStack or AWS.

- But instantly, you can use Vagrantfile to build VMs for trial use or small project.
  1. Install [Oracle VM VirtualBox](https://www.virtualbox.org/) and [Vagrant by HashiCorp](https://www.vagrantup.com/) on your machine.
  1. Modify Vagrantfile
    - This Vagrantfile creates VMs these are connected to the public network (LAN) toward physical NIC. So, you must change NIC name for bridge on the Vagrantfile, if your machine is not Macbook Pro. You can also delete the NIC name, if do so, Vagrant ask you select NIC during `vagrant up` command.
    - This Vagrantfile supposed that the ip address of a VM is supplied from DHCP server, and you can lookup VMs by mDNS (avahi/apple's bonjour). So, if you want to change network settings, you must rewrite Vagrantfile drastically.
  1. Wakeup VMs
    - Wakeup all VMs. `$ vagrant up`
    - Wakeup an individual VM.`$ vagrant up redmine`

### 2. Access settings for Ansible ###

- (If you use Vagrant, you need not modify access settings.)
- group_vars/vagrant.yml

  ```yaml
  ---
  ansible_ssh_user: vagrant
  ```

- host_vars/gitlab.yml

  ```yaml
  ---
  ansible_ssh_host: 127.0.0.1
  ansible_ssh_port: 2222
  ansible_ssh_private_key_file: .vagrant/machines/gitlab/virtualbox/private_key
  ```

- host_vars/redmine.yml

  ```yaml
  ---
  ansible_ssh_host: 127.0.0.1
  ansible_ssh_port: 2223
  ansible_ssh_private_key_file: .vagrant/machines/redmine/virtualbox/private_key

  db_passwd_redmine : a9EtesfPqJm3
  ```

- host_vars/ldap.yml

    ```yaml
    ---
    ansible_ssh_host: 127.0.0.1
    ansible_ssh_port: 2224
    ansible_ssh_private_key_file: .vagrant/machines/ldap/virtualbox/private_key
    ```

- (if you need proxy settings,) delete comment out mark "#" on proxy.yml and modify it.

  ```yaml
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
  ```

### 3. Manual settings ###

- Gitlab
  - you need nothing to do.
- Redmine
  - 1.set locale for redmine
  - 2.download plugins
  - for more details, see [Details of Redmine](#redmine)
- OpenLDAP & PWM
  - 1.set domain-name and admin's password before running ansible-playbook. for more details, see [Details of OpenLDAP](#ldap)
  - 2.you need to setup PWM (ldap management application) after running ansible-playbook. for more details, see [Details of PWM](#pwm)

### 4. Install services ###

- Setup all services. `$ ansible-playbook site.yml`
- Setup individual service. `$ ansible-playbook site.yml -l redmine`
- If you fail to connect ssh, try `$ ansible-playbook -c paramiko site.yml`. "-c paramiko" means use "paramiko" Python module for ssh connection instead of OpenSSH clinet.

Details
----------------
### Gitlab ###

### <a name="redmine">Redmine</a> ###

- About Locale
  - <span style="color:red">Change redmine_locale variablie</span> in  /roles/redmine/vars/main.yml

    ```yaml
    ---
    redmine_dir : /var/lib/redmine
    redmine_locale : ja
    ```

  - The locale of initial redmine data on postgresql is {{ redmine_locale }}. Frankly, ``bundle exec rake redmine:load_default_data REDMINE_LANG="{{ redmine_locale }}"`` will be invoked.
- Free plugins
  - these are automatically installed by ths ansible-playbook
  - Ticket
    - [Issue Template](https://github.com/akiko-pusu/redmine_issue_templates.git)
    - [Excel Export](https://github.com/two-pack/redmine_xls_export.git)
    - [Default Custome Query](https://github.com/hidakatsuya/redmine_default_custom_query.git)
    - [Backlogs](https://github.com/backlogs/redmine_backlogs.git) (Kanban)
  - Wiki
    - [Wiki Extensions](https://bitbucket.org/haru_iida/redmine_wiki_extensions)
    - [Knowledgebase](https://github.com/alexbevi/redmine_knowledgebase.git)
    - [Lightbox2](https://github.com/paginagmbh/redmine_lightbox2.git) (Preview attached images)
    - [Clipboard image paste](https://github.com/peclik/clipboard_image_paste.git) (Attach an image on clipbard to wiki)
    - [Embedded Flash](https://github.com/fcrespel/redmine_embedded_flash.git) ({{flash(<attached file>|<URL>,width,height)}})
    - [Wiki Lists](https://github.com/tkusukawa/redmine_wiki_lists.git) (show tickets on wiki {{ref_issues(condition formula..., expression formula...)}})        
  - Usability
    - [Theme Changer](https://bitbucket.org/haru_iida/redmine_theme_changer)
    - [Local Avator](https://github.com/ncoders/redmine_local_avatars.git)
    - [Sidebar hide](https://github.com/bdemirkir/sidebar_hide.git)
    - [Banner](https://github.com/akiko-pusu/redmine_banner.git) (show maintenance message etc.)
    - [View Customize](https://github.com/onozaty/redmine-view-customize.git) (add any css/javascript to a page)
- Commercial Free plugins
  - <span style="color:red">These are free, but you need to register email and downlowd zip files.</span> If you don't download these plugins, this ansible-playbook simply ignore these, i.e. the install process not abend (abnormal-end).
  - Easy Redmine Plugins
    - [Gantt](https://www.easyredmine.com/redmine-gantt-plugin)
    - [WBS](https://www.easyredmine.com/redmine-wbs-plugin)
    - download EasyGanttFree.zip and EasyWBSFree.zip. Then put these on the directory '/roles/redmine/files/'
  - Redmine CRM Plugins
    - https://www.redminecrm.com/
    - Favorite Porjects : Shortcut selectbox to projects
    - Questions : QA Forum
    - Zen Edit : Full screen editor
    - download redmine_favorite_projects-2_0_3-light.zip, redmine_questions_0_0_7-light.zip and redmine_zenedit-0_0_2-light.zip. Then put these on the directory '/roles/redmine/files/'
  - [RM+](http://rmplus.pro/en) creates cool plugins, but these conflicts with  the backlogs plugin ;-).

### <a name="ldap">LDAP</a> ###

- About Domain-name and password
  - <span style="color:red">Change following variablie</span> in  /roles/ldap/vars/main.yml

    ```yaml
    ---
    # DOMAIN must be the first dc of the SUFFIX.
    ROOT_PWD: secret
    DOMAIN: example
    SUFFIX: dc=example,dc=com
    ORG: production site
    ```
- Settings by ansible-playbook
  - OpenLDAP 2.3 or higher is OLC(On-Line Configuration). So, we must write settings for OpenLDAP itself to following directory tree.
    - cn=config
       - dc=schema
       - olcDatabase={0}config
       - olcDatabase={2}bdb
  - Schema : The playbook set following schema to cn=config,dc=schema
    - core.schema   (required) : basic attribute. "cn", "ou", etc.
    - cosine.schema (required) : x500/COSINE tree figure data structure
    - inetorgperson.schema     : name, group, email, etc.
    - memberof : memberof overlay. Make OpenLDAP add memberof attribute to the search result of person node like RDB's view-table. For example, if you create admin-gruop and admin-user ichiro, ichiro's memberOf attribute(s) is resolved by OpenLDAP automatically when ldapsearch was invoked.

      ```
      # admin user
      dn: cn=ichiro,ou=People,dc=example,dc=com
      objectClass: inetOrgPerson
      cn: ichiro
      sn: suzuki
      userPassword: ichiro123

      # admin group
      dn: cn=admin,ou=Group,dc=example,dc=com
      objectClass: groupOfNames
      cn: admin
      member: cn=ichiro,ou=People,dc=example,dc=com
      ```

      ```shell
      $ ldapsearch -x -LLL -H ldap:/// -b cn=ichiro,ou=People,dc=example,dc=com dn memberof
      dn: cn=ichiro,ou=People,dc=example,dc=com
      memberOf: cn=admin,ou=Group,dc=example,dc=com
      ```
  - Data directory : The playbook create following tree
    - dc=com
      - dc=example
        - Group (organizationalUnit)
          - admin (groupOfNames)
            - admin.member = cn=ichiro,ou=People,dc=example,dc=com
        - People (organizationalUnit)
          - ichiro (inetOrgPerson)
              - ichiro.userPassword=ichiro123
          - jiro (inetOrgPerson)
            - jiro.userPassword=jiro123
  - Access authentication : The playbook set following access auth settings to olcDatabase={2}bdb.

| Attribute    | User        | Auth         |
|:-------------|:------------|:------------:|
| userPassword |cn=Manager,dc=example,dc=com|manage        |
|              |self         |write         |
|              |anonymous    |auth          |
|              |* (other)    |none          |
| * (other)    |cn=Manager,dc=example,dc=com|manage        |
|              |self         |write         |
|              |* (other)    |none          |
  - Appendex. About typical attibutes

| Attribute    | Note        |
|:-------------|:------------|
|dn            |a location of tree. Ex. cn=ichiro,ou=People,dc=example,dc=com|
|dc            |domain component. Ex. dc=example, dc=com|
|c             |country|
|o             |organization. Ex. a company|
|ou            |organization unit. Ex. a division in the company|
|cn            |lastname (family-name)|
|sn            |firstname (given-name)|
|uid           |user id|
|userPassword  |password. You shoud store hash value of password. Don't put plain text.|

### <a name="pwm">PWM</a> ###

### Jenkins ###

### Alfresco ###

License
----------
Copyright &copy; 2016 A.HO
Licensed under the  [MIT License][mit].

[MIT]: http://www.opensource.org/licenses/mit-license.php
