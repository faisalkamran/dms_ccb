#!/bin/bash

source /home/odoo12/odoo-dev/odoo12env/bin/activate
odoo --config ~/odoo-dev/library/12-library.conf --addons-path="~/odoo-dev/odoo/addons,~/odoo-dev/library" --database=12-library --db-filter=12-library$ --save --stop