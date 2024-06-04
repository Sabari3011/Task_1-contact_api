from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import userlogin  ,CheckApi , logoutUser


urlpatterns = [
     path("login/",obtain_auth_token,name="login"),
     path("check/",CheckApi.as_view()),
     path("logout/",logoutUser),
     # path('api/restricted/', RestrictedView.as_view(), name='restricted'),

]
