tinc-dorky ansible role
=============================

This ansible role installs tinc VPN onto a remote host,
& copies the tinc host file to the local ansible runner.

The operator then copies that host file onto dorky/the VPN server.

The operator fainlly re-runs the recipe in restart mode.
