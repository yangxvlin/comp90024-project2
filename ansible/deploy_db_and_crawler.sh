#!/usr/bin/env bash
. ./group-03-openrc.sh; ansible-playbook --ask-become-pass deploy_db_and_crawler.yaml -i inventory/application_hosts.ini