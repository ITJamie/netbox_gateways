#!/bin/bash
set -e
cd /opt/netbox/netbox
export DEBUG=True
python3 manage.py runserver 0.0.0.0:8080
