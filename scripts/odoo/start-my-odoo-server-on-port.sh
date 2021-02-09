#!/bin/bash

source ~/odoo-9.0/bin/activate
#~/odoo-code/odoo-9.0/odoo.py start --path=~/odoo-code/my-odoo

~/odoo-code/odoo-9.0/odoo.py start --path=~/odoo-code/my-odoo --xmlrpc-port=$1