# Configuration for the server_LDAP

This adds django-auth-ldap to enable authentication with LDAP.

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

3. If you get an error when trying to install django-auth-ldap, make sure you install these libraries
   `libsasl2-dev python-dev libldap2-dev libssl-dev`

4. Set up the proper configuration in `ldap2/settings.py`

Steps:
* Point to your server, set AUTH_LDAP_SERVER_URI to your LDAP server.
* Add the credentials for your LDAP server so that you can perform various search operations on users.

    ```
    AUTH_LDAP_BIND_DN
    AUTH_LDAP_BIND_PASSWORD
    ```

* You can use search/bind or direct bind. Read the [django-auth-ldap documentation](https://django-auth-ldap.readthedocs.io/en/latest/authentication.html) for the different options.

5. Run the server:
```
./manage.py runserver
```

6. Open http://127.0.0.1:8000 in a browser and login with the users that you have in LDAP directory.
