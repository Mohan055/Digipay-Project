from django.contrib import admin
from transactions.models import CreditCard,Transaction
# Register your models here.

admin.site.register(Transaction)

class CreditCardAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'number', 'month', 'year', 'card_type', 'card_status')

admin.site.register(CreditCard, CreditCardAdmin)