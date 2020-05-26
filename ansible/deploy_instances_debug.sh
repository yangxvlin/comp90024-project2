#!/usr/bin/env bash

. ./group-03-openrc.sh; ansible-playbook --ask-become-pass deploy_instances.yaml --check -vvv
