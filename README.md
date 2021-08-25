# customer-managment-system

This project help you manage your customers.

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
###### 5- Run server 
  ```
  python manage.py runserver 
  ```
