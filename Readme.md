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
| pod-charlesreid1 | https://git.charlesreid1.com/docker/pod-charlesreid1 |
| pod-bots         | https://git.charlesreid1.com/docker/pod-bots         |
| pod-webhooks     | https://git.charlesreid1.com/docker/pod-webhooks     |

## Playbooks

There is one playbook per docker pod, plus a base playbook
and a provision playbook.

| Playbook                  | Description                                                                                                          |
|---------------------------|----------------------------------------------------------------------------------------------------------------------|
| `charlesreid1pod.yml`     | Playbook to install and run the charlesreid1.com docker pod (<https://git.charlesreid1.com/docker/pod-charlesreid1>) |
| `charlesreid1hooks.yml`   | Playbook to install and run the webhooks pod (<https://git.charlesreid1.com/docker/pod-webhooks>)                    |
| `charlesreid1bots.yml`    | Playbook to install and run the bot pod (<https://git.charlesreid1.com/docker/pod-bots>)                             |
| `base.yml`                | Base playbook run by all of the pod playbooks above.                                                                 |
| `provision.yml`           | Playbook to provision new Ubuntu machines with `/usr/bin/python`.                                                    |


## Roles

The following roles carry out groups of related tasks.

| Role Name             | Description                                               |
|-----------------------|-----------------------------------------------------------|
| init-root             | Prepare root user account                                 |
| init-nonroot          | Prepare nonroot user account(s)                           |
| install-stuff         | Install stuff with aptitude                               |
| pyenv                 | Install pyenv for nonroot user                            |
| goenv                 | Install goenv for nonroot user                            |
| sshkeys               | Set up ssh keys for all users                             |
| vim                   | Set up vim for nonroot user                               |
| dotfiles              | Install and configure dotfiles for nonroot user           |


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

