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

from django.contrib import admin

from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User, Group
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from account.views import(
    user_info_secret,
    UserList,
    UserDetails,
    GroupList,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r"^oauth/", include('oauth2_provider.urls', namespace='oauth2_provider')),
    # path('api/hello', ApiEndpoint.as_view()),  # an example resource endpoint
    path('userinfo', user_info_secret),
    path('users/', UserList.as_view()),
    path('users/<pk>/', UserDetails.as_view()),
    path('groups/', GroupList.as_view()),

]
