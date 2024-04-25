# melp-api-backend

-------------

# Introduccion

Aplicacion donde se pueden agregar, ver, editar y eliminar restaurantes.

Ademas se puede consultar los restaurantes en un radio determinado indicando la posision actual.

----

# Tecnologias utilizadas

* Docker
* FastAPI
* Dependency Injection
* Pydantic
* MySQL
* SQLAlchemy


------

# Endpoints

### GET restaurants

`curl --location 'https://melp-api-backend-production.up.railway.app/restaurants/get/RESTAURANT_ID'`

### UPDATE restaurants
`curl --location --request PUT 'https://melp-api-backend-production.up.railway.app/restaurants/update/RESTAURANT_ID' \
--header 'Content-Type: application/json' \
--data-raw '{
    "rating": RATING,
    "email": EMAIL,
    "name": NAME,
    "site": SITE,
    "phone": PHONE_NUMBER,
    "street": STREET,
    "city": CITY,
    "state": STATE,
    "latitude": LATITUDE,
    "longitude": LONGITUDE
}'`

### SAVE restaurants
`curl --location 'https://melp-api-backend-production.up.railway.app/restaurants/save' \
--header 'Content-Type: application/json' \
--data-raw '{
    "rating": RATING,
    "email": EMAIL,
    "name": NAME,
    "site": SITE,
    "phone": PHONE_NUMBER,
    "street": STREET,
    "city": CITY,
    "state": STATE,
    "latitude": LATITUDE,
    "longitude": LONGITUDE
}'`

### DELETE restaurants
`curl --location --request DELETE 'https://melp-api-backend-production.up.railway.app/restaurants/delete/RESTAURANT_ID'`

### GET restaurants by radius

`curl --location 'https://melp-api-backend-production.up.railway.app/restaurants/statistics/?latitude=LATITUDE&longitude=LONGITUDE&radius=RADIUS'`

----

