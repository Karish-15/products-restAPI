# products-restAPI
- REST API with JWT auth and algolia search functionality.

- Client made using HTML, CSS and Js. Backend made using django-rest, SQLite, Algolia Search.

- JWT Authentication is implemented. Client must send Access tokens to be able to use product search.

- User can search the database for keywords and the response is formatted in JSON with relevant details.

## How to run:
- Install requirements from `requirements.txt`
- Run django server using `python manage.py runserver` in root directory.
- Run client from `\Client\js_client` using `python -m http.server 8111`. This starts client server on port 8111.
