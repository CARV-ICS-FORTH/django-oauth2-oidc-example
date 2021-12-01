# Configuration for the client

To run:

1. Create a virtual environment:
```
pipenv shell
```

or

```
python3 -m venv venv
source venv/bin/activate
```

2. Once the virtual enviroment is created, you need to install requirments and migrate:
```
pip install -r requirements.txt
./manage.py migrate
```

3. Set up the servers run client and configure the appropriate variables in `client/settings.py`.

4. Run the server:
```
./manage.py runserver 8000
```

5. Open http://127.0.0.1:8000 in a browser and login with the users that you created in server_OAUTH2 and server_OIDC.
