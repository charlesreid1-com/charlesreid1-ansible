# Ansible Cowsay

This page covers the `cowsay` command and all the cows
that show up when you run ansible.


Table of Contents
=================

* [Wat](#wat)
* [Turn off cows](#turn-off-cows)
* [Weird cows](#weird-cows)


## Wat

One of the first things you notice about ansible is that
it tells you what's going on via a series of cows:

```plain
____________
< PLAY [all] >
------------
       \   ^__^
        \  (oo)\_______
           (__)\       )\/\
               ||----w |
               ||     ||
```

That's because Ansible is wrapping log messages with the
program cowsay, which prints out text in a text bubble
accompanied by a cow.


## Turn off cows

To turn off the cows, set `ANSIBLE_NOCOWS=1`:

```
ANSIBLE_NOCOWS=1 \
ANSIBLE_CONFIG="vagrant.cfg" \
        ansible-playbook \
        base.yml
```

which is boring:

```
GATHERING FACTS *************************************************************** 
ok: [127.0.0.1]
```

## Weird cows

Fortunately, cowsay comes with many kinds of cows:

```plain
$ cowsay -l
Cow files in /usr/local/Cellar/cowsay/3.04/share/cows:
beavis.zen blowfish bong bud-frogs bunny cheese cower daemon default dragon
dragon-and-cow elephant elephant-in-snake eyes flaming-sheep ghostbusters
head-in hellokitty kiss kitty koala kosh luke-koala meow milk moofasa moose
mutilated ren satanic sheep skeleton small sodomized stegosaurus stimpy
supermilker surgery telebears three-eyes turkey turtle tux udder vader
vader-koala www
```

...so many questions.

To specify a particular cow, set the `ANSIBLE_COW_SELECTION` variable:

```plain
ANSIBLE_COW_SELECTION=vader
```

gives you

```
 ___________________________
< PLAY [Initial setup root] >
 ---------------------------
        \    ,-^-.
         \   !oYo!
          \ /./=\.\______
               ##        )\/\
                ||-----w||
                ||      ||

               Cowth Vader

 ________________________
< TASK [Gathering Facts] >
 ------------------------
        \    ,-^-.
         \   !oYo!
          \ /./=\.\______
               ##        )\/\
                ||-----w||
                ||      ||

               Cowth Vader

```

Here is `ANSIBLE_COW_SELECTION=tux`:

```plain
< GATHERING FACTS >
 -----------------
   \
    \
        .--.
       |o_o |
       |:_/ |
      //   \ \
     (|     | )
    /'\_   _/`\
    \___)=(___/
```

