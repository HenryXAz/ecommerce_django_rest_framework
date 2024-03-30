# django
from django.urls import path

# views
from apps.users.api.api import user_api_view 

urlpatterns = [
  path('users/', user_api_view, name='users_api')
]