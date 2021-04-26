## Table of content

## Header

## Descriptions

SetupandInstallation

Food Page

Drink Page

Support

Troubleshooting

Future Goal

Contrubutions

Authors

Status

Headers
Yelp for Hippy
This is site for hippy.

Description
Using this site, hippies can find food, bar and night life near them. Then after their visit, rate them accordingly.

SetupandInstallation
This part is only frontend where react is used. setted up mostly OSX and Linux

pip install python3
pip install django
pip install psycopg2-binary
pip install react 
startreactproject
FoodPage
Screen Shot 2021-04-25 at 10 14 31 PM

DrinkPage
Screen Shot 2021-04-25 at 10 15 46 PM

Support
please visit https://docs.djangoproject.com/en/3.2/

Troubleshooting
Error: psql: FATAL: role “postgres” does not exist Solution: Check out this https://stackoverflow.com/questions/15301826/psql-fatal-role-postgres-does-not-exist.

Error: psql: error: FATAL: Peer authentication failed for user "postgres" Solution:

Run psql Run SHOW hba_file; Copy the path it returns (something like /etc/postgresql/13/main/pg_hba.conf on Ubuntu) Open pg_hba.conf in a text editor (you will likely need to run the command with sudo) Change this line: local all postgres peer to: local all postgres md5 Restart PostgreSQL: sudo service postgresql restart Now rerun the original command

Futuregoal
Contribution
Pull requests are welcome.

Authors
Tyree Tyler Hengyu Krishna

Please make sure to update tests as appropriate.

License
MIT

Status
Building..Site should be up soon.
