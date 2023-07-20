Role Name
=========

Role for issuing client (SMIME) and server SSL certificates using the Sectigo CA. 

Requirements
------------

The sectigo_certificate role relies on the sectigo_ansible module, shipped as part of the role itself.
The full list of requirements to properly run this role is provided in the integration guide.
This role makes also use of the [openssl_csr](https://docs.ansible.com/ansible/latest/modules/openssl_csr_module.html) and [openssl_privatekey](https://docs.ansible.com/ansible/latest/modules/openssl_privatekey_module.html) and inherits the requirements of these modules.

Role Variables
--------------

Full information is provided in the integration guide.
The full list of variables for the role is available in the defaults file.

Dependencies
------------

None.

Example Playbook
----------------

The Sectigo Ansible role can be used in a playbook using the following structure:

```yaml
---
- hosts: localhost
  roles:
    - sectigo_ansible
  vars:
    sectigo_cm_base_url: 'https://myca.cert-manager.com/api/ssl/v1'
    sectigo_csr_subject: "C=CA/ST=ON/L=Ottawa/O=MyOrg/OU=Research/CN=myorg.com/emailAddress=example@myorg.com"
    sectigo_ssl_cert_file_path: "./mysslcerts"
    sectigo_ssl_cert_file_name: "test_ssl"
    sectigo_ssl_cert_type: 51
    sectigo_ssl_cert_validity: 365
    sectigo_ssl_cert_num_servers: 1
    sectigo_ssl_cert_server_type: -1
    sectigo_ssl_cert_expiry_window: 7
    sectigo_auto_renew: true
    sectigo_ssl_cert_format_type: x509CO
    sectigo_max_timeout: 600
    sectigo_loop_period: 30
    sectigo_ssl_cert_comments: "Test certificate for Sectigo: {{ sectigo_ssl_cert_file_name }}"

```

In the tests directory, we provide four individual sample playbooks which demonstrate how the Sectigo Ansible role can be used. The four playbooks are the following:
tests/test-ssl.yml
tests/test-ssl-revoke.yml
tests/test-client.yml
tests/test-client-revoke.yml

Additionally, there's a file that can be used to export your SCM-specific environment variables:
tests/example.env

In order to make use of these samples:

Navigate into the tests directory using: "$ cd tests"
Add your SCM credentials to the example.env file.
Source the environment variables using: "$ source example.env"
Modify the variables in the applicable sample yml file (e.g. test-ssl.yml).
Run the playbook (e.g. test-ssl.yml) using: "$ ansible-playbook test-ssl.yml"

License
-------

BSD

Author Information
------------------

This role is provided by [Sectigo](https://sectigo.com/).
