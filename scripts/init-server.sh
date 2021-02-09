#!/bin/bash

echo "Enter database name"
read var1

#if empty string
if [[ -z $var1 ]]; then 
	until [[ -n $var1 ]]; do
		echo "Please enter database name"
		read var1
	done

	DBNAME=$var1
	DBFILTERNAME=$var1$

	# echo $DBNAME
	# echo $DBFILTERNAME

	#initialize odoo 12 database
	source /home/odoo12/odoo-dev/odoo12env/bin/activate
	odoo --database=$DBNAME --db-filter=$DBFILTERNAME -i INIT
#if not empty string
else
	source /home/odoo12/odoo-dev/odoo12env/bin/activate
	odoo --database=$DBNAME --db-filter=$DBFILTERNAME -i INIT
fi
