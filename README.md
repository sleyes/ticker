Ticker API

instructions:
1. use Python 3.9.7
2. clone the repo
3. create a virtual environment:
    python3 -m venv venv
4. activate the virtual environment:
    source venv/bin/activate
5. install requirements:
    pip install -r requirements.txt
6. run migrations:
    python manage.py migrate
7. (optional) create superuser
    python manage.py createsuperuser
8. run server:
    python manage.py runserver
9. go to the url http://127.0.0.1:8000/API/v1/register and create a user providing email, first_name and last_name. IMPORTANT: take note of the token
10. use the API by calling (replace Token with the one obtained in the previous step):
    curl --location --request GET 'http://127.0.0.1:8000/API/v1/get_ticker?symbol=FB' \
--header 'Authorization: Token 4197fdad52dee2ceb6e6889670762d2c99600c9bc907ddcdecf25f3968d8997e'
11. Optionally use Postman:
    method: GET
    url: http://127.0.0.1:8000/API/v1/get_ticker
    query params: key=symbol value=[share_symbol]
