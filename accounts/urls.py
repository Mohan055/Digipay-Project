from accounts import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path("",views.sign_in,name="sign_in"),
    path("sign_up/",views.sign_up,name="sign_up"),
]