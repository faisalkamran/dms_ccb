#!/bin/bash

if [[ -z $1 ]]; then #if empty string
	#ask for user input while also checking null input
	until [[ -n $var1 ]]; do
		echo "Please enter database name"
		read var1
	done

	#set database name
	DATABASE_NAME=$var1

	#run odoo 12 server on the Asus T100 tablet
	source /home/faisal/odoo-dev/odoo12env/bin/activate
	odoo -d $DATABASE_NAME --dev=all
	deactivate
	echo "Odoo server successfully terminated."
	echo "Press Enter key to exit."
	read var2

else
	#set database name
	DATABASE_NAME=$1

	#run odoo 12 server on the Asus T100 tablet
	source /home/faisal/odoo-dev/odoo12env/bin/activate
	odoo -d $DATABASE_NAME --dev=all
	deactivate
	echo "Odoo server successfully terminated."
	echo "Press Enter key to exit."
	read var2
fi