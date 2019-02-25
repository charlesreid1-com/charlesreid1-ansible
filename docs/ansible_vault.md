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
* [Adding new secret variables](#adding-new-secret-variables)


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


## Adding new secret variables

Suppose we have a role that utilizes a variable that is sensitive
and should remain secret. To do this, we set up a series of
variable definitions that allow the secret defined in the vault
to be used for different roles.

Suppose we have a role that uses an API key in a command. The role
utilizes a variable `{{ api_key }}` like so:

`roles/my-role/tasks/main.yml`:

```
---
- name: A simple example task using a secret variable
  command: "python script.py --api-key={{ api_key }}"
```

If the variable `api_key` is defined in the task default variable 
values, this command will be run but with an invalid API key.
If the above command should _only_ be run with a valid API key,
you can leave `api_key` out of the default variable values.

Here is what that would look like, if you defined the API key 
to be an empty string by default:

`roles/my-role/defaults/main.yml`:

```
---
api_key: ""
```

To set the real `api_key` value, override the default variable
value in the playbook(s) that run that role. For example, if
the role `my-role` is called from a playbook `main.yml`,

`main.yml`:

```
---
- name: Run my-role
  roles:
    - role: my-role
      api_key: "{{ charlesreid1_api_key }}"
```

This specifies that the `api_key` variable should be set to the 
value of the variable `charlesreid1_api_key`.

The prefix `charlesreid1` indicates a site-specific variable setting.
Those variables are contained in `group_vars/all/main.yml`.
The variable is defined there, but it is also defining the variable
to be set to another variable value:

`group_vars/all/main.yml`:

```
---
charlesreid1_api_key: "{{ vault_api_key }}"
```

The last step is to define the variable in the vault.
This is where we use the `ansible-vault` command to edit
the vault file:

```
ANSIBLE_CONFIG="my_config.cfg" ansible-vault edit group_vars/all/vault
```

This is where you put the real API key:

`group_vars/all/vault`:

```
---
vault_api_key: "ABCXYZ123456"
```

