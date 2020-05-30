# Secrets

Two kinds of secrets:

- secret variables (in secrets vault)
- secret files (encrypted and kept in `secrets/` directory)

## Secret Variables

Use `ansible-vault edit` command.

## Secret Files

Encrypt a file using `ansible-vault encrypt` command.

Standard procedure is to add .enc extension to filename.

```
$ ansible-vault encrypt --vault-password-file .vault_secret hello.txt --output hello.txt.enc
```
