aws role (pad.carpentries.org)
=========

This role installs the AWS command line interface and AWS credentials
to use Carpentries AWS resources.

Specifically, this role is tailored to the `pad.carpentries.org`
Carpentries Etherpad server.

Requirements
------------

This uses the `apt` module to install `awscli`, and copies (encrypted) 
AWS API credentials into the target machine. Nothing else is required 
except the password to decrypt the AWS credentials.

Role Variables
--------------

| Name                    | Default | Description                                                                     |
|:------------------------|:--------|:------------------------|
| `aws_access_key_id`     | None    | The AWS API access key. |
| `aws_secret_access_key` | None    | The AWS API secret key. |

These are defined in an encrypted vault.

Dependencies
------------

None

Example Playbook
----------------

How to use the role:

```plain
- name: Install AWS credentials
  hosts: servers
  become: yes
  roles:
    - role: aws
```

Vault Information
------------------

The AWS credentials for The Carpentries are located in 
the vault for the pad playbook, which is located in 
[`../../group_vars/all/`](../../group_vars/all/).


Author Information
------------------

Charles Reid - [@charlesreid1](https://github.com/charlesreid1) - <charles@charlesreid1.com>


