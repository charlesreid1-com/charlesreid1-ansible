# Ansible Vault

This page contains instructions for using the Ansible vault.

Link: [Ansible vault documentation](https://docs.ansible.com/ansible/2.4/vault.html#creating-encrypted-files)


Table of Contents
=================

* [What is Ansible Vault?](#what-is-ansible-vault)
* [Where is the vault file?](#where-is-the-vault-file)
* [How to view the vault file?](#how-to-view-the-vault-file)
* [How to create a vault file?](#how-to-create-a-vault-file)
* [How to edit the vault file?](#how-to-edit-the-vault-file)
* [How to use the vault file?](#how-to-use-the-vault-file)


## What is Ansible Vault?

Ansible provides a "vault" function that allows sensitive data
(passwords, sensitive info, or certificate files) to be encrypted,
so it can be stored in a repository with the rest of the playbook.

The vault is an ordinary YAML file that defines variables, except
that the variables it defines are sensitive. These variables can
be used elsewhere in the playbook.

Ansible provides an `ansible-vault` command to interact with 
vault files.


## Where is the vault file?

There is currently one vault file that applies to all servers.
It is located in the repository at `group_vars/all/vault`.


## How to view the vault file?

To view the contents of the vault file, use the view action:

```
ansible-vault edit my_vault_file
```


## How to create a vault file?

No new vault files should be needed for this repository, but to create
a new vault file called `my_vault_file`, use the create action:

```plain
ansible-vault create my_vault_file
```


## How to edit the vault file?

To edit the contents of the vualt file, use the edit action

```plain
EDITOR="vim" ansible-vault edit my_vault_file
```


## How to use the vault file?

Vault files are used by ansible in the process of running playbooks.
The user can provide Ansible with the vault password either on the
command line (via an interactive prompt), or the user can put the
vault password into a file, and point Ansible to the vault password
file when it is run.

We do that latter, putting the vault password in the file `.vault_secret`.

To tell ansible wehre to find the vault password, we set `vault_password_file`
in the configuration file. In both configuration files, we have:

```plain
vault_password_file = .vault_secret
```

Put your password into the file `.vault_secret` and use this
configuration file (by pointing to it with the `ANSIBLE_CONFIG`
environment variable when running ansible).

