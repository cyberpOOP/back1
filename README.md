# lab1
# Routes
GET:

/catgeories - всі категорії

/users - всі користувачі

/records - список всіх записів

POST:

/category - додати категорію

/user - додати користувача

/user_record - додати запис користувачу

/by_user - знайти запис за користувачем

/by_category - знайти запис за користувачем та категорією

# Deploy

# Local

flask run

# Docker

docker build --build-arg PORT=5000 . -t <image_name>:latest

docker images

docker-compose build

docker-compose up

# Remote

URL: https://backendlab12.herokuapp.com

# Requests

Всі запроси виконуються за допомогою Postman. 

Наявні collection та environment