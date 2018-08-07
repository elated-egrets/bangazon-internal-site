# !/bin/bash

# Joe's tutorial on this command/ running faker
# https://github.com/nashville-software-school/bangazon-llc/blob/master/DB_RESET_SEED_SYSTEM.md
# For Mac users, save this file as django_data.sh in usr/local/bin
# (Which is at your machine's root, not your Users folder)


# The name of the django app that contains the models you want to add to the db schema/update

# The name of the custom command file. If my app was called bangazon_api, then I would type

# django_data.sh bangazon_api faker_factory

find . -path "/$1/migrations/*.py" -not -name "__init__.py" -delete; #deletes all of the .py files in the migrations directory except for the __init__.py file.
find . -path "/$1/migrations/*.pyc"  -delete; #deletes all of the .pyc files in the migrations directory.
rm db.sqlite3; #deletes the database file.
python manage.py makemigrations $1; #creates the migration and the new db file.
python manage.py migrate; #runs the migration.
python manage.py $2 #runs the custom command to generate fake data and populate your tables with it