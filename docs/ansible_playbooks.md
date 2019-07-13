# Ansible Playbooks

This page covers what playbooks are in this directory
and how to run them.


Table of Contents
=================

* [provision\.yml: Provision Your Remote Node](#provisionyml-provision-your-remote-node)
* [base\.yml: the base plays](#baseyml-the-base-plays)
* [podcharlesreid1\.yml: charlesreid1 docker pod play](#podcharlesreid1yml-charlesreid1-docker-pod-play)
* [charlesreid1hooks\.yml: webhooks server docker pod play](#charlesreid1hooksyml-webhooks-server-docker-pod-play)
* [charlesreid1bots\.yml: bots docker pod play](#charlesreid1botsyml-bots-docker-pod-play)
* [List of Tags](#list-of-tags)


## provision.yml: Provision Your Remote Node

The provision playbook is a preparation step to ensure
Ansible has the software it needs to run. Specifically,
Ubuntu distributions do not come with `/usr/bin/python`
by default (only `/usr/bin/python3`), so the provision
step installs `/usr/bin/python`.

```plain
ANSIBLE_CONFIG="vagrant.cfg" vagrant provision
```

Running plays against a Digital Ocean node requires
the provision playbook to be run explicitly with the
command:

```plain
ANSIBLE_CONFIG="do.cfg" ansible-playbook provision.yml
```

Also see the Provision sections of the 
[ansible_vagrant.md](ansible_vagrant.md)
and [ansible_do.md](ansible_do.md) pages.


## base.yml: the base plays

The base.yml playbook contains a base set of plays for all
charlesreid1.com nodes. This includes setup, tooling, dotfiles,
user accounts, SSH keys, and so on.

**This playbook does not define a machine name.** It is not
usually run explicitly, except in tests, so machine name must
be defined manually. To do that, use the `--extra-vars` flag:

```plain
ANSIBLE_CONFIG="vagrant.cfg" \
        ansible-playbook \
        --vault-password-file=.vault_secret \
        --extra-vars "machine_name=yoyo" \
        base.yml
```

To run on Digital Ocean, use the same command
but specify the corrsponding config file:

```plain
ANSIBLE_CONFIG="do.cfg" \
        ansible-playbook \
        --vault-password-file=.vault_secret \
        --extra-vars "machine_name=yoyo" \
        base.yml
```


## podcharlesreid1.yml: charlesreid1 docker pod play

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
        ansible-playbook \
        --vault-password-file=.vault_secret \
        podcharlesreid1.yml
```

To set a custom hostname, use the `--extra-vars` flag as above:

```plain
ANSIBLE_CONFIG="vagrant.cfg" \
        ansible-playbook \
        --vault-password-file=.vault_secret \
        --extra-vars "machine_name=yoyo" \
        podcharlesreid1.yml
```

**Example:** Deploy the charlesreid1 docker pod play
to a Digital Ocean droplet.

```plain
ANSIBLE_CONFIG="do.cfg" \
        ansible-playbook \
        --vault-password-file=.vault_secret \
        --extra-vars "machine_name=yoyo" \
        podcharlesreid1.yml
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
scripts to keep some Twitter bots going:

- Ginsberg bot flock
- Milton bot flock
- Apollo Space Junk bot flock


## List of Tags

(Incomplete)

Each role has a tag associated with it, so you can
run each role in isolation:

* `aws`
* `init-root`
* `install-stuff`
* `goenv`
* `pyenv`
* `docker`
* `init-nonroot`
* `sshkeys`
* `dotfiles`
* `vim`
* `pod-charlesreid1`


### Base Playbook Tags

The base playbook `base.yml` includes the majority of
the roles, whose tags are listed here:

* `aws`
* `init-root`
* `install-stuff`
* `goenv`
* `pyenv`
* `docker`
* `init-nonroot`
* `sshkeys`
* `dotfiles`
* `vim`

The base playbook also uses the following tags
for sub-groups of tasks, or for groups of tasks
that cross roles:

* `aws_tools` (aws command line tools and libraries only)
* `aws_creds` (aws credentials only)
* `pip` (all tasks installing packages using pip)
* `apt` (all tasks installing packages using apt)
* `docker-no-compose` (docker-only tasks)
* `docker-compose`  (docker-compose-only tasks)
* `root-ssh` (setup of ssh keys for root user)
* `nonroot-ssh` (setup of ssh keys for nonroot user)

### pod-charlesreid1 Playbook Tags

The pod-charlesreid1 playbook contains the docker pod
playbook for charlesreid1.com. This is a single role.
The entire role is run with the tag:

* `pod-charlesreid1`

Subtasks are grouped as follows:

* `pod-charlesreid1-services` (runs tasks that start the docker service and the pod service)
* `pod-charlesreid1-gitea` (set up gitea for pod-charlesreid1)
* `pod-charlesreid1-mw` (set up mediawiki for pod-charlesreid1)

