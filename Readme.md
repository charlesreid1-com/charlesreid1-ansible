# charlesreid1-ansible

Ansible playbooks for charlesreid1.com infrastructure.

## What is here?

Playbooks:
- fardaa
- bluebear

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
- pod-charlesreid1 (x)
- pod-bots
- pod-webhooks

## Where are playbooks run?

Playbooks can be run as follows:
- against Vagrant machines, for local testing
- against machines in the cloud

See below for details.

## How to use the playbooks?

See [Quickstart](Quickstart.md).

For instructions on running playbooks on a local machine
with Vagrant, see
[Quickstart#Vagrant](Quickstart.md#Vagrant).

For instructions on running playbooks on DigitalOcean
nodes, see
[Quickstart#DigitalOcean](Quickstart.md#DigitalOcean).


