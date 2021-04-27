<img width="300" alt="Screen Shot 2021-04-27 at 12 56 04 AM" src="https://user-images.githubusercontent.com/79564250/116187341-5a77da80-a6f3-11eb-82f9-e636cc46895d.png">
## Table of content

[Header](#Hippy)  

[Descriptions](#description)  

[SetupandInstallation](#setupandinstallation) 

[FoodList](#foodlist)  

[DrinkList](#drinklist)  

[Support](#support)  

[Apps](#apps)  

[Frameworks](#frameworks)

[Troubleshooting](#troubleshooting) 

[Future Goal](#futuregoal) 

[Contrubutions](#contribution) 

[Authors](#authors)

[Status](#status) 


## Description
This is backend of the original project of Yelp. Here you'll find information about how the backend was use to create this Yelp website.

## SetupandInstallation 
setted up in OSX and Linux

`pip install django` 
`pip install djangorestframework`
`pip install psycopg2-binary` 
`django-admin startproject`

## Apps
<img width="233" alt="Screen Shot 2021-04-26 at 11 34 37 PM" src="https://user-images.githubusercontent.com/79564250/116181074-f865a800-a6e7-11eb-9c02-b502bf2e6f13.png">


## FoodsList!
<img width="864" alt="Screen Shot 2021-04-26 at 11 38 49 PM" src="https://user-images.githubusercontent.com/79564250/116181406-8fcafb00-a6e8-11eb-8f5c-f48b7ca04abc.png">

## Drinklist
<img width="1208" alt="Screen Shot 2021-04-26 at 11 40 32 PM" src="https://user-images.githubusercontent.com/79564250/116181553-cc96f200-a6e8-11eb-8f29-2c25ef6b9bf2.png">



## frameworks
`Django REST framework` 

`Serializations`

`Views`

`Models`

## Support
please visit https://docs.djangoproject.com/en/3.2/

## Troubleshooting
Error: psql: FATAL: role “postgres” does not exist 
<br />
Solution: Check out this https://stackoverflow.com/questions/15301826/psql-fatal-role-postgres-does-not-exist.

Error: psql: error: FATAL: Peer authentication failed for user "postgres" 
Solution: Run psql Run SHOW hba_file; Copy the path it returns (something like /etc/postgresql/13/main/pg_hba.conf on Ubuntu)
Open pg_hba.conf in a text editor (you will likely need to run the command with sudo)
Change this line: local all postgres peer to: local all postgres md5 Restart PostgreSQL: sudo service postgresql
restart Now rerun the original command

## Futuregoal
can be added more lists 

## Contribution
Pull requests are welcome.

## Authors
Tyree Tyler Hengyu Krishna

Please make sure to update tests as appropriate.

## License MIT

## Status 
Building..Site should be up soon.
