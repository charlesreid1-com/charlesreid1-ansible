# Quickstart

## Vagrant

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

If you have an ansible script that should be run
against the Vagrant machines only, this should be
in a `provision.yml` file and can be applied like so:

```
vagrant provision
```

Now get ssh info to put into an inventory file,
so that ansible can connect to the vagrant machine(s):

```
vagrant ssh-config
```

## DigitalOcean


