[![CircleCI](https://circleci.com/gh/kdakis/customer-managment-system/tree/main.svg?style=svg)](https://circleci.com/gh/kdakis/customer-managment-system/tree/main)

# Customer Managment System

This project help you manage your customers.

### Project link
https://sheltered-shore-96619.herokuapp.com/

#### Backend:
* Python
* Django
* PostgreSql
    
#### Frontend:
* HTML
* CSS

**also i use the some third party app. requirements.txt include these apps

## INSTALLATION
##### - Clone repo

##### - fill the "cms/env.example" with your own information and rename it to ".env"

##### - You can use virtual enviroment (recomended)

###### 1- Install requirements.txt
  ```
  pip install -r requirement.txt
  ```
###### 2- Create database
  ```
  CREATE DATABASE db_name

  CREATE USER user WITH PASSWORD 'password';

  GRANT ALL PRIVILEGES ON DATABASE db_name TO user
  ```
  **After that define your database informations to ".env" file.

###### 3- You can create superuser (not necassery)
  ```
  python manage.py createsuperuser 
  ```
###### 4- Migrate your database
  ```
  python manage.py migrate
  ```
###### 5- Load 10 customer information from fixtures to database (optional)
  ```
  python manage.py loaddata customer
  ```
###### 6- Run server 
  ```
  python manage.py runserver 
  ```

#### IF YOU WANT DOCKERIZE YOUR PROJECT

Install docker (you can find instroduction for install docker in dockr official site).

and follow commands

###### 1- build your container
  ```
  docker-compose build
  ```
###### 2- Up server 
  ```
  docker-compose up
  ```

#### *** You must give enviroment veriables to docker

#### You can set environment variables with ‘docker-compose run’ like:
  ```
  docker-compose run -e DEBUG=1 web python console.py
  ```
##### Also be sure you stop local postgresql because local psql already use 5432 port
  ```
  systemctl stop postgresql
  ```