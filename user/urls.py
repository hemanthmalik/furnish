from django.urls import path, include
from . import views as user_view

urlpatterns = [
    path('register/', user_view.register, name='register'),
    path('login/', user_view.CustomAuthToken.as_view(), name="login"),
    path('testapi/', user_view.SecuredTestAPI.as_view(), name="test")
]