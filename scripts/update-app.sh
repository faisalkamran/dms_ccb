#!/bin/bash

DATABASE_NAME=$1
APP_NAME=$2

#run odoo 12 server
source ~/odoo-dev/odoo12env/bin/activate
~/odoo-dev/src/odoo/odoo-bin -d $DATABASE_NAME -u $APP_NAME
