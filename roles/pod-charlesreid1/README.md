pod-charlesreid1 ansible role
=============================

This ansible role installs pod-charlesreid1, a docker pod that runs charlesreid1.com.

Requirements
------------

???

Tasks
-----

phase 1:

- clone pod contents

phase 2:

- /www setup
  - server_name_default top level domain clone
- docker and docker compose checks
- mediawiki prep
- gitea prep

phase 3:

- construct the pod (docker-compose build)
- install service
- (port mapping in Dockerfile)
- (letsencrypt cert check)
- enable service

Role Variables
--------------

List of role variables (set in `defaults/main.yml`):

- `username`
- `pod_install_dir`
- `admin_email`
- `server_name_default`
- `nginx_subdomains_ip`
- `port_default`
- `port_gitea`
- `port_ssl_default`
- `port_ssl_gitea`
- `gitea_app_name`
- `gitea_domain`
- `gitea_secret_key`
- `gitea_internal_token`
- `mysql_password`
- `mediawiki_secretkey`

Most of these have default values set from top-level Ansible variables
prefixed with `charlesreid1`:

- `nonroot_user` (used to set `username`)
- `charlesreid1_admin_email`
- `charlesreid1_server_name_default`
- `charlesreid1_nginx_subdomains_ip`
- `charlesreid1_port_default`
- `charlesreid1_port_gitea`
- `charlesreid1_port_ssl_default`
- `charlesreid1_port_ssl_gitea`
- `charlesreid1_gitea_secret_key`
- `charlesreid1_gitea_internal_token`
- `charlesreid1_mysql_password`
- `charlesreid1_mediawiki_secretkey`

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
