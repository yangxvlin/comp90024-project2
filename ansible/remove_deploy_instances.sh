#!/usr/bin/env bash

. ./group-03-openrc.sh; ansible-playbook --ask-become-pass remove_deploy_instances.yaml