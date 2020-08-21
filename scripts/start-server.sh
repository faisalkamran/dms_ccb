#!/bin/bash

if [[ -z $1 ]]; then #if empty string
	#ask for user input while also checking null input
	until [[ -n $var1 ]]; do
		echo "Please enter database name"
		read var1
	done

	#set database name
	DATABASE_NAME=$var1

	#run odoo 12 server
	source ~/odoo-dev/odoo12env/bin/activate
	~/odoo-dev/src/odoo/odoo-bin -d $DATABASE_NAME

else
	#set database name
	DATABASE_NAME=$1

	#run odoo 12 server
	source ~/odoo-dev/odoo12env/bin/activate
	~/odoo-dev/src/odoo/odoo-bin -d $DATABASE_NAME
fi
