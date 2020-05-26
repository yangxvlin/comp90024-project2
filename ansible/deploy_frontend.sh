#!/usr/bin/env bash
. ./group-03-openrc.sh; ansible-playbook --ask-become-pass deploy_frontend.yaml -i inventory/application_hosts.ini