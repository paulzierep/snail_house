Requirements:

sudo apt-get install python-virtualenv 							#virual python env
pip freeze -l 													#check what you got in the env

sudo apt-get install postgresql postgresql-client libpq-dev 	#db setup

###db stuff init

create user snail;
ALTER USER snail WITH PASSWORD 'snail';
GRANT ALL PRIVILEGES ON DATABASE schnecken TO snail;
