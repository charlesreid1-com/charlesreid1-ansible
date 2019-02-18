# Quickstart

This quickstart walks through the process of using
Vagrant and running the charlesreid1 playbooks
against a Vagrant machine.

Step 1: Vagrant Setup

Step 2: Run Base Playbook

Step 3: Changing Variables



## Vagrant Setup

Vagrant is a command-line wrapper around
VirtualBox and allows setting up one or more
virtual machines to test out Ansible playbooks
locally.

we have a vagrant file for the role, but if you don't you can do `vagrant init ubuntu/xenial64`

### Start Vagrant Machines

The following commands require a `Vagrantfile`.
Use the provided one or modify it for your needs.

Start a vagrant virtual machine with:

```
vagrant up
```

Run the initial setup play with Ansible using the 
`provision.yml` provision playbook:

```
ANSIBLE_CONFIG="vagrant.cfg" vagrant provision
```

Get info about how to connect to the vagrant machine(s)
via SSH:

```
vagrant ssh-config
```

This information should match what is in the `vagranthosts`
inventory file.



## Run Ansible

### Set Up Vault Secret

Before running Ansible with the Ansible-Vagrant config file,
it will expect the vault secret to be in a file called
`.vault_secret` in the current directory.

Create this file before proceeding.

Example `.vault_secret` file:

```plain
this_is_my_super_strong_password!
```


### Run the Playbook

To run a playbook, use the `ANSIBLE_CONFIG` environment 
variable to specify the Ansible-Vagrant config file, and 
use the `ansible-playbook` command:

```plain
ANSIBLE_CONFIG="vagrant.cfg" ansible-playbook base.yml
```

The config file specifies the inventory file, SSH key,
vault password, and log file to use, among other details.


