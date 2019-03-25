# charlesreid1-ansible

Ansible playbooks for charlesreid1.com infrastructure.

Table of Contents
=================

* [Docker Pods](#docker-pods)
* [Playbooks](#playbooks)
* [Roles](#roles)
* [Getting Started with Playbooks](#getting-started-with-playbooks)
* [Running Playbooks](#running-playbooks)
  * [Running Select Tasks with Tags](#running-select-tasks-with-tags)
* [Secrets and Sensitive Information](#secrets-and-sensitive-information)
* [Vagrant Testing](#vagrant-testing)
* [DigitalOcean Deployment](#digitalocean-deployment)


## Docker Pods

These docker pods are collections of related charlesreid1.com
services. The Ansible playbooks prepare remote nodes so they
are ready to run these docker pods.

| Pod              | Link                                                   |
|------------------|--------------------------------------------------------|
| pod-charlesreid1 | <https://git.charlesreid1.com/docker/pod-charlesreid1> |
| pod-webhooks     | <https://git.charlesreid1.com/docker/pod-webhooks>     |
| pod-bots         | <https://git.charlesreid1.com/docker/pod-bots>         |

## Playbooks

There is one playbook per docker pod, plus a base playbook
and a provision playbook.

| Playbook               | Description                                                                                                          |
|------------------------|----------------------------------------------------------------------------------------------------------------------|
| `podcharlesreid1.yml`  | Playbook to install and run the charlesreid1.com docker pod (<https://git.charlesreid1.com/docker/pod-charlesreid1>) |
| `podwebhooks.yml`      | (TBA) Playbook to install and run the webhooks pod (<https://git.charlesreid1.com/docker/pod-webhooks>)                    |
| `podbots.yml`          | (TBA) Playbook to install and run the bot pod (<https://git.charlesreid1.com/docker/pod-bots>)                             |
| `base.yml`             | Base playbook run by all of the pod playbooks above.                                                                 |
| `provision.yml`        | Playbook to provision new Ubuntu machines with `/usr/bin/python`.                                                    |


## Roles


### Base Playbook Roles

The following roles carry out groups of tasks for setting up the base machine
to run charlesreid1.com infrastructure.

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


### Pod-Specific Roles

The following roles are run by playbooks specific to the
respective docker pod.

| Role Name             | Description                                                  |
|-----------------------|--------------------------------------------------------------|
| pod-charlesreid1      | Role specific to the charlesreid1.com docker pod             |
| pod-webhooks          | Role specific to \{hooks,pages\}.charlesreid1.com docker pod |
| pod-bots              | Role specific to bots docker pod                             |


## Getting Started with Playbooks

| Documentation Page                            | Description                                                     |
|-----------------------------------------------|-----------------------------------------------------------------|
| [docs/index.md](index.md)                     | Documentation index                                             |
| [docs/quickstart.md](quickstart.md)           | Quick start for the impatient (uses Vagrant)                    |
| [docs/ansible_do.md](ansible_do.md)           | Guide for running charlesreid1.com playbooks on Digital Ocean   |
| [docs/ansible_vagrant.md](ansible_vagrant.md) | Guide for running charlesreid1.com playbooks on Vagrant         |

See [Ansible Playbooks](ansible_playbooks.md) for a list of all
playbooks in this directory, list of all tags,
and info about how to use the playbooks.


## Running Playbooks

To run Ansible playbooks, use the `ansible-playbook` command.

You will need to specify:

* A configuration file to set Ansible options, using the
  `ANSIBLE_CONFIG` environment variable

* An inventory file to tell Ansible how to connect to
  remote machines, using the `-i` flag 

Here is an example call to `ansible-playbook`
to show how it should look:

```plain
ANSIBLE_CONFIG="my_config.cfg" ansible-playbook -i myhosts   main.yml
^^^^^^^^^^^^^^                                  ^^^^^^^^^^   ^^^^^^^^
specify config file                             specify the  the ansible
with this env var                               inventory    playbook
                                                file
```

Use the **Vagrant configuration file** `vagrant.cfg` to run 
playbooks against local Vagrant virtual machines (local testing).
Edit the `vagranthosts` file to match info printed by the
`vagrant ssh-config` command.

```plain
# Run ansible playbook on vagrant machines
ANSIBLE_CONFIG="vagrant.cfg" ansible-playbook -i vagranthosts main.yml
```

Use the **DigitalOcean configuration file** `do.cfg` to run
playbooks against DigitalOcean nodes. Edit the `dohosts` file to point
to the correct SSH key and remote host IP address.

```plain
# Run ansible playbook on DigitalOcean machines
ANSIBLE_CONFIG="do.cfg" ansible-playbook -i dohosts main.yml
```

### Running Select Tasks with Tags

To run a specific task, you can filter tasks using tags.
Use the `--tags` flag with the `ansible-playbook` command:

```plain
ANSIBLE_CONFIG="my_config.cfg" ansible-playbook -i hosts main.yml --tags tag1
ANSIBLE_CONFIG="my_config.cfg" ansible-playbook -i hosts main.yml --tags tag1,tag2,tag3
```

Find a full list of tags at [docs/ansible_playbooks.md](ansible_playbooks.md).


## Secrets and Sensitive Information

See [Ansible Vault](ansible_vault.md) for details about how to use
the Ansible vault to view/edit secrets and sensitive information.

**NOTE:** THe vault and vault secret should be set up before 
running playbooks against either Vagrant or AWS machines.


## Vagrant Testing

See [Ansible Vagrant](ansible_vagrant.md) for instructions on how to set up
a Vagrant virtual machine to run the Ansible playbook
against, for testing purposes.


## DigitalOcean Deployment

See [Ansible Digital Ocean](ansible_do.md) for instructions on how to set up an DigitalOcean
node to run the Ansible playbook against.

