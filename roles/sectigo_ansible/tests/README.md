# Usage instructions for the test suite

This document provides instructions on how to prepare the environments to run the test suite for the `sectigo_certificate` module.
We assume you have a working installation of Ansible.

## Install the required roles

Execute the following commands:

```bash
ansible-galaxy install robertdebock.bootstrap
```

## Install the required packages

If you want to use FreeBSD, the suggested ssh client is `paramiko`.
You can easily install paramiko with pip:

```bash
pip install paramiko
```

The setup playbooks require to provide passwords before the hosts are setup for public key access only.
Ansible requires `sshpass` to be installed on the Ansible controller node to be able to use passwords. 
On an Ubuntu machine this can be accomplished with the following command:

```bash
sudo apt-get install sshpass
```


## Update the bootstrap role

The bootstrap role has a couple of bugs for ubuntu and freebsd.

For FreeBSD we need to remove the xz package from the list of packages to install in FreeBSD (xz is part of the default install in FreeBSD 11.3 and 12.0).
This can be achieved commenting the `xz` package in the `FreeBSD` group under the role `vars/main.yml` file (line `159` at the time of writing).
You shouldn't need any change if you are on FreeBSD 11.2.

For Ubuntu you need to disable the preview packages (i.e.: set the variable `bootstrap_preview=no`) if you want to use the `18.04 LTS` version. 


## Setup your ansible controller
First run the playbook to prepare the ansible controller

```bash
ansible-playbook -i localhost prepare-controller.yml --ask-become
```

NOTE: If you are planning to use virtual environments you might have to give your virtual environment access to the system packages.
With the mkvirtualenvwrapper you can achieve this using the following syntax:
`mkvirtualenv --python=python3.6 --system-site-packages sectigo`
This will help avoid problems to find python libraries that are not available in pypy but necessary for some ansible modules (e.g.: apt)


## Prepare the managed nodes

This can be achieved, thanks to the setup-hosts.yml playbook:

```bash
ansible-playbook -i /home/jdoe/inventories/test-hosts.yml -e keypair_path="/home/jdoe/.ssh/ender" -e bootstrap_preview=no -e bootstrap_remote_user=jdoe setup-hosts.yml --become --ask-become --ask-pass -u jdoe
```

After the execution of the playbook your hosts are ready for the test suite!


