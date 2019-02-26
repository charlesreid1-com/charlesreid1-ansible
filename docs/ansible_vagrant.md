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

This will start a Ubuntu Xenial (16.04) machine.


## Provision Vagrant Machine (Setup Step)

Ansible can be used to provision the vagrant machine,
which is basically a step that gets it ready for
the "real" Ansible playbook.

(Specifically, the provision step installs `/usr/bin/python`,
which is not included by default in newer versions of
Ubuntu.)

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
log_path = ansible_vagrant.log
command_warnings=False
vault_password_file = .vault_secret
```

This example points to a vault secret contained
in the file `.vault_secret` as seen in the last line.

See [Ansible Vault](ansible_vault.md) for more info
about vault secrets.


