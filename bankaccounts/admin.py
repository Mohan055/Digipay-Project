from django.contrib import admin
from bankaccounts.models import Account,KYC


# Register your models here.
class Accountadmin(admin.ModelAdmin):
    list_display = ['user','account_number','account_balance','account_status', 'kyc_submitted','kyc_confirmed']
    list_editable = ['account_balance','account_status','kyc_submitted','kyc_confirmed']

class KYCAdmin(admin.ModelAdmin):
    list_display = ['full_name','gender','identity_type']
    
admin.site.register(Account,Accountadmin)
admin.site.register(KYC,KYCAdmin)