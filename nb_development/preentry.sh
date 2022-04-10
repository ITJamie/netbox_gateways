#!/bin/bash
set -e

source /opt/netbox/venv/bin/activate
cd /opt/plugin_source
python3 setup.py develop

cd /opt/netbox/netbox
exec "$@"