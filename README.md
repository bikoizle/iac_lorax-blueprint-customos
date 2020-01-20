CustomOS Blueprint
==================

# Description

This Lorax Blueprint contains configuration for generating CustomOS OpenStack images
based on Fedora.

Installs Clam antivirus, Zabbix monitoring agent and cloud-init service
to have automatic VM configuration in OpenStack. 

In addition, customos user account is configured in order to grant access to VMs.

Optionally a root key can be inserted by changing "ROOT_KEY" word.

# Requirements

Lorax > 31
