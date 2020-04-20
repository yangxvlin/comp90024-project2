#!/usr/bin/env bash

. ./group-03-openrc.sh; ansible-playbook --ask-become-pass docker.yaml -i inventory/hosts.ini
