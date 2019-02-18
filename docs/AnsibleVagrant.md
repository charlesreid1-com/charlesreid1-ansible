# Local Ansible Testing with Vagrant

Vagrant is a command-line wrapper around
VirtualBox and allows setting up one or more
virtual machines to test out Ansible playbooks
locally.

The repo contains a Vagrantfile (created with
the command `vagrant init ubuntu/xenial64`) that
has been modified to work with Ansible.

## Start Vagrant Machine

Start a Vagrant virtual machine using the `Vagrantfile`
by running the following command in this directory:

```plain
vagrant up
```

This will start a Ubuntu xenial (16.04) machine.


## Provision Vagrant Machine (Setup Step)

Ansible can be used to provision the vagrant machine,
which is basically a step that gets it ready for
the "real" Ansible playbook.

(Specifically, the provision step installs `/usr/bin/python`,
which is not included by default in Ubuntu 16.04+).

Use the Ansible configuration file that is intended
for use with Vagrant, `vagrant.cfg`, when running
the vagrant provision command:

```plain
ANSIBLE_CONFIG="vagrant.cfg" vagrant provision
```


## Set Vagrant Configuration File

Now get info about how to SSH into the vagrant machines
and provide this information in the `vagranthosts`
Ansible inventory file:

```
vagrant ssh-config
```

Add information about the location of the
private key file, and any other details,
into `vagrant.cfg`:

**`vagrant.cfg`:**

```plain
[defaults]
inventory = vagranthosts
remote_user = vagrant
private_key_file = ~/.vagrant.d/insecure_private_key
host_key_checking = False
vault_password_file = .vault_secret
command_warnings = False
log_path=ansible_vagrant.log
```

This example points to a vault secret contained
in the file `.vault_secret`.

See [AnsibleVault.md](AnsibleVault.md) for more info
about vault secrets.


