#!/bin/bash

cd ~
source ~/odoo-9.0/bin/activate
cd ~/odoo-code/odoo-9.0/
python odoo.py -d odoo-test --addons-path=addons --db-filter=odoo-test$