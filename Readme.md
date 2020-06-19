# charlesreid1-ansible

Ansible playbooks for charlesreid1.com infrastructure.


Table of Contents
=================

* [Docker Pods](#docker-pods)
* [Playbooks](#playbooks)
* [Roles](#roles)
* [Getting Started with Playbooks](#getting-started-with-playbooks)


## Docker Pods

These docker pods are collections of related charlesreid1.com
services. The Ansible playbooks prepare remote nodes so they
are ready to run these docker pods.

| Pod              | Link                                                 |
|------------------|------------------------------------------------------|
| pod-charlesreid1 | <https://git.charlesreid1.com/docker/pod-charlesreid1> |

## Playbooks

There is one playbook per docker pod, plus a base playbook
and a provision playbook.

| Playbook               | Description                                                                                                          |
|------------------------|----------------------------------------------------------------------------------------------------------------------|
| `podcharlesreid1.yml`  | Playbook to install and run the charlesreid1.com docker pod (<https://git.charlesreid1.com/docker/pod-charlesreid1>) |
| `bots.yml`             | Playbook to install and run the apollo, ginsberg, and milton bot flocks. See <https://bots.charlesreid1.com>.        |
| `base.yml`             | Base playbook run by all of the pod playbooks above.                                                                 |
| `provision.yml`        | Playbook to provision new Ubuntu machines with `/usr/bin/python`.                                                    |


## Roles


### Playbook Roles

The following roles carry out groups of tasks for setting up the base machine
to run charlesreid1.com infrastructure.

**Base roles:**

| Role Name             | Description                                               |
|-----------------------|-----------------------------------------------------------|
| init-root             | Prepare root user account                                 |
| init-nonroot          | Prepare nonroot user account(s)                           |
| dotfiles              | Install and configure dotfiles for nonroot user           |
| install-stuff         | Install stuff with aptitude                               |
| letsencrypt           | Install letsencrypt                                       |
| postfix               | Install postfix mail server                               |
| pyenv                 | Install pyenv for nonroot user                            |
| goenv                 | Install goenv for nonroot user                            |
| sshkeys               | Set up ssh keys for all users                             |
| vim                   | Set up vim for nonroot user                               |

**Machine-specific roles:**

| Role Name             | Description                                                             |
|-----------------------|-------------------------------------------------------------------------|
| bots                  | Install and run the apollo, ginsberg, and milton bot flocks. See <https://bots.charlesreid1.com>. |
| pod-charlesreid1      | Install the charlesreid1.com pod <https://github.com/charlesreid1-docker/pod-charlesreid1>). |
| uptime                | Install the uptime bot (<https://github.com/charlesreid1-bots/uptime>). |


## Getting Started with Playbooks

| Documentation Page                                 | Description                                                     |
|----------------------------------------------------|-----------------------------------------------------------------|
| [docs/index.md](docs/index.md)                     | Documentation index                                             |
| [docs/quickstart.md](docs/quickstart.md)           | Quick start for the impatient (uses Vagrant)                    |
| [docs/ansible_do.md](docs/ansible_do.md)           | Guide for running charlesreid1.com playbooks on Digital Ocean   |
| [docs/ansible_vagrant.md](docs/ansible_vagrant.md) | Guide for running charlesreid1.com playbooks on Vagrant         |

See [docs/ansible_playbooks.md](docs/ansible_playbooks.md) for a list of all
playbooks in this directory and how to run them, as well as a list 
of all tags.

