# Quickstart

This quickstart walks through the process of using
Vagrant and running the charlesreid1 playbooks
against a Vagrant machine.


Table of Contents
=================

* [Vagrant Setup](#vagrant-setup)
    * [Start Vagrant Machines](#start-vagrant-machines)
    * [Provision Vagrant Machines](#provision-vagrant-machines)
    * [Configure Ansible-Vagrant SSH Info](#configure-ansible-vagrant-ssh-info)
* [Cloud Node Setup](#cloud-node-setup)
* [Run Ansible](#run-ansible)
    * [Set Up Vault Secret](#set-up-vault-secret)
    * [Run the Base Playbook](#run-the-base-playbook)
* [Change Variables](#change-variables)


## Vagrant Setup

Vagrant is a command-line wrapper around
VirtualBox and allows setting up one or more
virtual machines to test out Ansible playbooks
locally.

To run Vagrant boxes, you need a Vagrantfile.
One is provided in this repo, but if you don't have one
you can run `vagrant init ubuntu/xenial64` to create
a new one.


### Start Vagrant Machines

The following commands require a `Vagrantfile`.
Use the provided one or modify it for your needs.

Start a vagrant virtual machine with:

```
vagrant up
```


### Provision Vagrant Machines

Run the initial setup play with Ansible using the 
`provision.yml` provision playbook:

```
ANSIBLE_CONFIG="vagrant.cfg" vagrant provision
```


### Configure Ansible-Vagrant SSH Info

Vagrant provides info about how to connect to
the Vagrant machine(s) created using the `ssh-config`
verb:

```
vagrant ssh-config
```

Copy this information into the `vagranthosts`
inventory file so that Ansible knows how to
connect to the Vagrant boxes.


## Cloud Node Setup

Different cloud providers set up their compute nodes
differently, but the following is required to do
on a cloud node before you can run Ansible on it.

* Ensure your operating system has a version of
  `python3` available from the command line

* Ensure the public SSH key of the machine from
  which you are running Ansible matches the 
  public SSH key in the authorized keys file that
  will be installed via Ansible

    * The authorized keys file is located in 
      `roles/ssh/files/authorized_keys`

* Ensure the hosts file for this cloud node contains
  a username that actually exists on the remote system


## Run Ansible

### Set Up Vault Secret

!!! warning
    The vault secret should match the
    original secret used to encrypt
    the vault. If you don't have it,
    delete `vault` and start over.

Before running Ansible with the Ansible-Vagrant config file,
it will expect the vault secret to be in a file called
`.vault_secret` in the current directory.

Create this file before proceeding.

Example `.vault_secret` file:

```plain
this_is_my_super_strong_password!
```

To use this file to access variables in the vault,
pass the vault password file using the flag:

```
ansible-playbook \
        --vault-password-file=.vault_secret \
        <other-flags>
```

### Run the Base Playbook

To run a playbook, use the `ANSIBLE_CONFIG` environment 
variable to specify the Ansible-Vagrant config file, and 
use the `ansible-playbook` command:

```plain
ANSIBLE_CONFIG="vagrant.cfg" ansible-playbook \
        --vault-password-file=.vault_secret \
        base.yml
```

The config file specifies the inventory file, SSH key,
vault password, and log file to use, among other details.


## Change Variables

You can modify variables in the 
`group_vars/main.yml` file by 
adding additional variable definitions
in YAML format:

```
$ cat group_vars/main.yml 

...

my_var_1: "red"
my_var_2: "blue"

```

Alternatively, you can pass custom
variable values on the command line.
(This is how we specify the machine
name when running playbooks.) Here,
we set a few example variables:

```
$ ANSIBLE_CONFIG="my_config_file.cfg" \
        ansible-playbook \
        --vault-password-file=.vault_secret \
        -i hosts \
        --extra-vars "my_var_1=red,my_var_2=blue" \
        playbook.yml
```

See [Ansible Playbooks](ansible_playbooks.md)
for next steps.

