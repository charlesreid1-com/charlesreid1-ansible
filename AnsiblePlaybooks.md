# Ansible Playbooks

This covers how to run the playbooks in this directory.

## provision.yml: Provision Your Remote Node

The provision playbook is a preparation step to ensure
Ansible has the software it needs to run. Specifically,
Ubuntu distributions do not come with `/usr/bin/python`
by default (only `/usr/bin/python3`), so the provision
step installs `/usr/bin/python`.

The `provision.yml` file will be used automatically by
Vagrant, but running plays against an AWS node requires
the provision playbook to be run explicitly with the
command:

```plain
ANSIBLE_CONFIG="aws.cfg" ansible-playbook -i awshosts provision.yml
```

See "Provision" section of [AnsibleAWS.md](AnsibleAWS.md)
or [AnsibleVagrant.md](AnsibleVagrant.md) for more info
about the provision step.

## charlesreid1pod.yml: charlesreid1 docker pod play

The charlesreid1 docker pod runs the following:
- nginx
- letsencrypt/certs
- mediawiki
- gitea
- files/etc


## charlesreid1hooks.yml: webhooks server docker pod play

The webhooks server docker pod runs the following:
- captain hook webhook server
- hooks.charlesreid1.com domain
- static site hosting for pages.charlesreid1.com
- pages.charlesreid1.com domain


## charlesreid1bots.yml: bots docker pod play

The bots docker pod runs several Python 
scripts to keep some Twitter bots going.
- Ginsberg bot flock
- Milton bot flock
- Apollo Space Junk bot flock



## List of Tags

Tags associated with roles:
* `base-setup`
    * `init-root`
    * `install-stuff`
    * `goenv`
    * `pyenv`
    * `docker`
    * `init-nonroot`
    * `sshkeys`
    * `dotfiles`
    * `vim`

charlesreid1pod:
* `pod-charlesreid1`


