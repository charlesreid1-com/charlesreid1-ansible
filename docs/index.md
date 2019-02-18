# charlesreid1-ansible

Ansible playbooks for charlesreid1.com infrastructure.

## What is here?

**Docker Pods:**

These docker pods are collections of related charlesreid1.com
services. The Ansible playbooks prepare remote nodes so they
are ready to run these docker pods.

| Pod              | Link                                                 |
|------------------|------------------------------------------------------|
| pod-charlesreid1 | https://git.charlesreid1.com/docker/pod-charlesreid1 |
| pod-bots         | https://git.charlesreid1.com/docker/pod-bots         |
| pod-webhooks     | https://git.charlesreid1.com/docker/pod-webhooks     |

**Playbooks:**

There is one playbook per docker pod, plus a base playbook
and a provision playbook.

| Playbook                  | Description                                                                                                          |
|---------------------------|----------------------------------------------------------------------------------------------------------------------|
| `charlesreid1pod.yml`     | Playbook to install and run the charlesreid1.com docker pod (<https://git.charlesreid1.com/docker/pod-charlesreid1>) |
| `charlesreid1hooks.yml`   | Playbook to install and run the webhooks pod (<https://git.charlesreid1.com/docker/pod-webhooks>)                    |
| `charlesreid1bots.yml`    | Playbook to install and run the bot pod (<https://git.charlesreid1.com/docker/pod-bots>)                             |
| `base.yml`                | Base playbook run by all of the pod playbooks above.                                                                 |
| `provision.yml`           | Playbook to provision new Ubuntu machines with `/usr/bin/python`.                                                    |


**Roles:**

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



## Playbooks

See [ansible_playbooks.md](ansible_playbooks.md) for a list of all
playbooks in this directory, list of a ll tags,
and info about how to use the playbooks.


### Quick Start




### Running Playbooks

To run Ansible playbooks, use the `ansible-playbook` command.

You will need to specify:

* A configuration file to set Ansible options, using the
  `ANSIBLE_CONFIG` environment variable

* An inventory file to tell Ansible how to connect to
  remote machines, using the `-i` flag 

Here's how the `ansible-playbook` command should look:

```plain
ANSIBLE_CONFIG="my_config_file.cfg" ansible-playbook -i myhosts   base.yml
^^^^^^^^^^^^^^                                       ^^^^^^^^^^   ^^^^^^^^
specify config file                                  specify the  the ansible
with this env var                                    inventory    playbook
                                                     file
```

Use the **Vagrant configuration file** `vagrant.cfg` to run 
playbooks against local Vagrant virtual machines (local testing).
Edit the `vagranthosts` file to match info printed by the
`vagrant ssh-config` command.

```plain
# Run ansible playbook on vagrant machines
ANSIBLE_CONFIG="vagrant.cfg" ansible-playbook -i vagranthosts base.yml
```

Use the **DigitalOcean configuration file** `do.cfg` to run
playbooks against DigitalOcean nodes. Edit the `dohosts` file to point
to the correct SSH key and remote host IP address.

```plain
# Run ansible playbook on DigitalOcean machines
ANSIBLE_CONFIG="do.cfg" ansible-playbook -i dohosts base.yml
```

### Running Select Tasks with Tags

To run a specific task, you can filter tasks using tags.
Use the `--tags` flag with the `ansible-playbook` command:

```plain
ANSIBLE_CONFIG="asdf.cfg" ansible-playbook -i hosts base.yml --tags tag1
ANSIBLE_CONFIG="asdf.cfg" ansible-playbook -i hosts base.yml --tags tag1,tag2,tag3
```

Find a full list of tags at [ansible_playbooks.md](ansible_playbooks.md).


## Secrets and Sensitive Information

See [ansible_vault.md](ansible_vault.md) for details about how to use
the Ansible vault to view/edit secrets and sensitive information.

**NOTE:** THe vault and vault secret should be set up before 
running playbooks against either Vagrant or AWS machines.


## Vagrant Testing

See [ansible_vagrant.md](ansible_vagrant.md) for instructions on how to set up
a Vagrant virtual machine to run the Ansible playbook
against, for testing purposes.


## DigitalOcean Deployment

See [ansible_do.md](ansible_do.md) for instructions on how to set up an DigitalOcean
node to run the Ansible playbook against.

