# Digital Ocean Quickstart

This quickstart walks through the process
of setting up a Digital Ocean droplet
using these Ansible playbooks.


Table of Contents
=================

* [Droplet setup](#droplet-setup)
* [Run provision and base playbooks](#run-provision-and-base-playbooks)
* [Run pod playbooks](#run-pod-playbooks)


## Droplet setup

Start by logging in to your digital ocean account
and creating a droplet. You should be able to 
create or specify an SSH key. 

You must do the following first:

**Modify the SSH key in do.cfg (the digital ocean
ansible config file) to match the SSH key you added
to the droplet at creation.**

**Modify the host file dohosts (the digital ocean
inventory file) to have an IP address matching
your droplet.**


## Run provision and base playbooks

Now you're ready to run the Ansible playbooks.

Run the provision playbook to prepare the droplet for Ansible:

```
ANSIBLE_CONFIG="do.cfg" \
        ansible-playbook \
        provision.yml
```

Now you can run the base playbook.

**NOTE: You must provide a `machine_name` parameter using the `--extra-vars` flag.**

```
ANSIBLE_CONFIG="do.cfg" \
        ansible-playbook \
        --extra-vars "machine_name=redbeard" \
        base.yml
```

## Run pod playbooks

Once you've run the base playbook, you can install the docker pod
with the corresponding playbook.

pod-charlesreid1:

```
ANSIBLE_CONFIG="do.cfg" \
        ansible-playbook \
        --extra-vars "machine_name=redbeard" \
        podcharlesreid1.yml
```

