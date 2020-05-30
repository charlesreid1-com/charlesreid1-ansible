strategy for dealing with bot keys:

step 1: encrypt file with ansible-vault

```
$ ansible-vault encrypt server.key
```

step 2: refer to the encrypted file in the copy module

```
---
- hosts: all
  tasks:
    - name: Copy server private key
      copy:
        src: server.key
        dest: /etc/env/server.key
        decrypt: yes
        owner: root
        group: root
        mode: 400
        backup: no
```


