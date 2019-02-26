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

!!! warning
    You must modify the path to the SSH private
    key, specified in `do.cfg` (the Digital Ocean
    Ansible config file), to match the SSH key that
    you added to the droplet at its creation.

!!! warning
    Once you create your droplet and it is connected
    to the internet via a public IP, you must update
    the file `dohosts` (the Digital Ocean Ansible
    inventory file) to point to the correct IP address
    for the droplet.


## Run provision and base playbooks

Once you have the correct SSH key in `do.cfg`
and the correct droplet IP address in `dohosts`,
you are ready to run the Ansible playbooks.

Run the provision playbook to prepare the droplet for Ansible:

```plain
ANSIBLE_CONFIG="do.cfg" \
        ansible-playbook \
        provision.yml
```

Now you can run the base playbook.

!!! warning
    You must provide a `machine_name` parameter to
    the base playbook. This variable is **_not_**
    defined by default. Define it using the 
    `--extra-vars` flag.

```plain
ANSIBLE_CONFIG="do.cfg" \
        ansible-playbook \
        --extra-vars "machine_name=redbeard" \
        base.yml
```

## Run pod playbooks

Once you've run the base playbook, you can install the
docker pod with the corresponding playbook.

pod-charlesreid1:

```plain
ANSIBLE_CONFIG="do.cfg" \
        ansible-playbook \
        --extra-vars "machine_name=redbeard" \
        podcharlesreid1.yml
```

