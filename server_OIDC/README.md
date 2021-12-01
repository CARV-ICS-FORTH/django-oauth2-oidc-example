# Configuration for the server with OIDC

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

2. Once the virtual enviroment is created, you need to install requirments, migrate and create a superuser:
```
pip install -r requirements.txt
./manage.py migrate
./manage.py createsuperuser
```

3. Run the server:
```
./manage.py runserver 8002
```

4. Register the client application
Open http://127.0.0.1:8002/admin/ in a browser, log in with the user that you created, and click "add" in Applications like the picture below:
![oauth_toolkit](https://user-images.githubusercontent.com/47854739/136280377-05fbf850-484d-42e5-bfd3-6e8321507c06.png)

You need to configure the application that you are about to register. Client id and Client secret are automatically generated. You have to provide the rest of the information:
* User: The owner of the Application (if you delete the user you also delete everything that the user created).
* Redirect uris: Applications must register at least one redirection endpoint before using the authorization endpoint. The Authorization Server will deliver the access token to the client only if the client specifies one of the verified redirection uris. For this project, paste verbatim the value `http://127.0.0.1:8000/oauth/complete/mycustomoidc/`.
* Client type: Choose `confidential`.
* Authorization grant type: Choose `Authorization code`.
* Name: This is the name of the client application on the server, and will be displayed on the authorization request page, where users can allow/deny access to their data. Enter `server_OIDC`.
* Algorithm: Choose `RSA with HSA-2 256`.

Your application should look like the picture below:
![oidc_app_configuration](https://user-images.githubusercontent.com/47854739/136284213-e3e30519-547f-4fac-b7b5-ebb43a8f1b73.png)

5. You need to provide the client id and client secret to your client application. Go to `settings.py` on the client app (`client/settings.py`) and add the generated key and secret to the variable SOCIAL_AUTH_MYCUSTOMOIDC_KEY and SOCIAL_AUTH_MYCUSTOMOIDC_SECRET line 29/30.

6. If you want to enable LDAP authentication follow the instructions in server_LDAP.
