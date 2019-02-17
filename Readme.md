# charlesreid1-ansible

Ansible playbooks for charlesreid1.com infrastructure.

## What is here?

Playbooks:
- charlesreid1pod.yml
- charlesreid1hooks.yml
- charlesreid1bots.yml


Roles:
- init root - system stuff (x)
- init charles - user stuff (x)
- dotfiles (x)
- vim (x)
- pyenv (x)
- goenv (x)
- packages (x)
- ssh keys (x)
- docker (x)

Docker pods:
- pod-charlesreid1
- pod-bots
- pod-webhooks

## Playbooks

See [AnsiblePlaybooks.md](AnsiblePlaybooks.md) for a list of all
playbooks in this directory, list of a ll tags,
and info about how to use the playbooks.


### Running Playbooks

To run Ansible playbooks, use the `ansible-playbook` command.

You will need to specify:

* A configuration file to set Ansible options, using the
  `ANSIBLE_CONFIG` environment variable

* An inventory file to tell Ansible how to connect to
  remote machines, using the `-i` flag 

Here's how the `ansible-playbook` command should look:

```
ANSIBLE_CONFIG="my_config_file.cfg" ansible-playbook -i myhosts   main.yml
^^^^^^^^^^^^^^                                       ^^^^^^^^^^   ^^^^^^^^
specify config file                                  specify the  the ansible
with this env var                                    inventory    playbook
                                                     file
```

Use the **Vagrant configuration file** `vagrant.cfg` to run 
playbooks against local Vagrant virtual machines (local testing).
Edit the `vagranthosts` file to match info printed by the
`vagrant ssh-config` command.

```
# Run ansible playbook on vagrant machines
ANSIBLE_CONFIG="vagrant.cfg" ansible-playbook -i vagranthosts main.yml
```

Use the **AWS configuration file** `aws.cfg` to run
playbooks against AWS nodes. Edit the `awshosts` file to point
to the correct SSH key and remote host IP address.

```
# Run ansible playbook on AWS machines
ANSIBLE_CONFIG="aws.cfg" ansible-playbook -i awshosts main.yml
```

## Running Select Tasks with Tags

To run a specific task, you can filter tasks using tags.
Use the `--tags` flag with the `ansible-playbook` command:

```
ansible-playbook -i hosts main.yml --tags mysql_role
ansible-playbook -i hosts main.yml --tags etherpad_role
```

Find a full list of tags at [AnsiblePlaybooks.md](AnsiblePlaybooks.md).


## Secrets and Sensitive Information

See [AnsibleVault.md](AnsibleVault.md) for details about how to use
the Ansible vault to view/edit secrets and sensitive information.

**NOTE:** THe vault and vault secret should be set up before 
running playbooks against either Vagrant or AWS machines.


## Vagrant Testing

See [AnsibleVagrant.md](AnsibleVagrant.md) for instructions on how to set up
a Vagrant virtual machine to run the Ansible playbook
against, for testing purposes.


## AWS Deployment

See [AnsibleAWS.md](AnsibleAWS.md) for instructions on how to set up an AWS
node to run the Ansible playbook against.

