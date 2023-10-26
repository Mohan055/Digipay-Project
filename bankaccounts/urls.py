from django.urls import path
from bankaccounts import views

app_name = 'bankaccounts'

urlpatterns = [
    path('',views.KYC_reg, name='kyc'),
    path('kyc_logout',views.KYC_logout, name='kyc_logout'),
    path('account/',views.account,name='account'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('add_card/',views.add_card,name='add_card')    
]