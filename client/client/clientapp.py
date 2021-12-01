# Copyright [2021] [FORTH-ICS]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from urllib.parse import urljoin
#import jwt

from requests import HTTPError
from django.contrib.auth.models import User
from social_core.backends.oauth import BaseOAuth2


class clientappOAuth2(BaseOAuth2):
    """Custom Django OAuth authentication backend"""
    name = 'clientapp'
    AUTHORIZATION_URL = 'http://localhost:8001/oauth/authorize/'
    ACCESS_TOKEN_URL = 'http://localhost:8001/oauth/token/'
    ACCESS_TOKEN_METHOD = 'POST'
    SCOPE_SEPARATOR = ','
    REDIRECT_STATE = False
    STATE_PARAMETER = True
    SEND_USER_AGENT = True
    ID_KEY="username"

    def get_user_details(self, response):
            """Return user details from my provider account"""
            return response


    def user_data(self, access_token, *args, **kwargs):
        return self.get_json('http://127.0.0.1:8001/userinfo', headers={
            'Authorization': 'Bearer ' + access_token
        })

