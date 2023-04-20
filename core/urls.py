
from django.contrib import admin
from django.urls import path
from api.views import UserList, GetToken
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', UserList.as_view()),
    path('token/', GetToken.as_view()),
    # path('api-token-auth/', obtain_auth_token),
]
