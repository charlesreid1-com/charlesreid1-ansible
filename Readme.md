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

See [AnsiblePlaybooks.md](AnsiblePlaybooks.md)
for a list of all tags for the roles and how to use
the tags.


### Running Playbooks

To run Ansible playbooks, use the `ansible-playbook` command.

You will need to specify:

* A configuration file to set Ansible options, using the
  `ANSIBLE_CONFIG` environment variable

* An inventory file to tell Ansible how to connect to
  remote machines, using the `-i` flag 

* (Optional) a `--tags` flag with a comma-separated list 
  of tags to use to filter which tasks are performed

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

