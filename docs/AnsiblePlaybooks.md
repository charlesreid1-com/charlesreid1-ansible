# Ansible Playbooks

This covers how to run the playbooks in this directory.

## provision.yml: Provision Your Remote Node

The provision playbook is a preparation step to ensure
Ansible has the software it needs to run. Specifically,
Ubuntu distributions do not come with `/usr/bin/python`
by default (only `/usr/bin/python3`), so the provision
step installs `/usr/bin/python`.

```plain
ANSIBLE_CONFIG="vagrant.cfg" vagrant provision
```

Running plays against an AWS node requires
the provision playbook to be run explicitly with the
command:

```plain
ANSIBLE_CONFIG="aws.cfg" ansible-playbook -i awshosts provision.yml
```

See "Provision" section of [AnsibleAWS.md](AnsibleAWS.md)
or [AnsibleVagrant.md](AnsibleVagrant.md) for more info
about the provision step.


## base.yml: the base plays

The base.yml playbook contains the base set of plays for all
charlesreid1.com nodes. This includes setup, tooling, dotfiles,
user accounts, SSH keys, and so on.

**This playbook does not define a machine name.** It is not
usually run explicitly, except in tests, so machine name must
be defined manually. To do that, use the `--extra-vars` flag:

```plain
ANSIBLE_CONFIG="vagrant.cfg" \
  ansible-playbook -i vagranthosts base.yml \
  --extra-vars "machine_name=yoyo"
```

## charlesreid1pod.yml: charlesreid1 docker pod play

**host: krash**

**host: redbeard**

The charlesreid1 docker pod runs the following:

- nginx
- letsencrypt/certs
- mediawiki
- gitea
- files/etc

**Example:** Deploy the charlesreid1 docker pod play
on a Vagrant machine.

To do this, specify the Ansible-Vagrant configuration file 
and the vagrant hosts file:

```plain
ANSIBLE_CONFIG="vagrant.cfg" \
  ansible-playbook -i vagranthosts charlesreid1pod.yml
```

To set a custom hostname, use the `--extra-vars` flag as above:

```plain
ANSIBLE_CONFIG="vagrant.cfg" \
  ansible-playbook -i vagranthosts charlesreid1pod.yml \
  --extra-vars "machine_name=yoyo"
```

**Example:** Deploy the charlesreid1 docker pod play
to a Digital Ocean droplet.

```plain
ANSIBLE_CONFIG="do.cfg" \
  ansible-playbook -i dohosts charlesreid1pod.yml \
  --extra-vars "machine_name=redbeard"
```


## charlesreid1hooks.yml: webhooks server docker pod play

**host: bluebear**

**host: bluebeard**

The webhooks server docker pod runs the following:
- captain hook webhook server
- hooks.charlesreid1.com domain
- static site hosting for pages.charlesreid1.com
- pages.charlesreid1.com domain


## charlesreid1bots.yml: bots docker pod play

**host: bluebear**

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


