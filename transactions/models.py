from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.contrib.auth.models import User
from bankaccounts.models import Account

# Create your models here.

TRANSACTION_STATUS = (
    ['failed','FAILED'],
    ['completed','COMPLETED'],
    ['pending','PENDING'],
    ['processing','PROCESSING'],
    ['request_sent','REQUEST_SENT'],
    ['request_processing','REQUEST_PROCESSING'],
)

TRANSACTION_TYPE = (
    ['transfer','TRANSFER'],
    ['withdraw','WITHDRAW'],
    ['refund','REFUND'],
    ['received','RECEIVED'],
    ['request','REQUEST'],
    ['none','NONE']
)

class Transaction(models.Model):
    transaction_id = ShortUUIDField(unique=True,length=15,max_length=20,prefix="TRN",alphabet="1234567890")
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name="user")
    amount = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    description = models.CharField(max_length=1000,null=True,blank=True)
    receiver = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,related_name="receiver")
    sender = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,related_name="sender")
    receiver_account = models.ForeignKey(Account, on_delete=models.SET_NULL,null=True,related_name="receiver_account")
    sender_account = models.ForeignKey(Account, on_delete=models.SET_NULL,null=True,related_name="sender_account")
    status = models.CharField(max_length=100,choices=TRANSACTION_STATUS, default='pending')
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE, default='none')
    date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=False,null=True,blank=True) 

    def __str__(self):
        return f'{self.user}'
    
CARD_TYPE = (
    ['visa', 'VISA'],
    ['rupay','RUPAY'],
    ['mastercard','MASTERCARD'],
    ['platinum','PLATINUM']
)

CARD_STATUS = (
    ['active','ACTIVE'],
    ['inactive','INACTIVE'],
)

class CreditCard(models.Model):
    card_id = ShortUUIDField(unique=True,length=10, max_length=20,prefix="CRED",alphabet='1234567890') 
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255)
    number = ShortUUIDField(unique=True,length=16,max_length=16,alphabet="1234567890")
    month = models.CharField(max_length=15)  
    year = models.IntegerField()
    CVV = ShortUUIDField(length=3,max_length=6, unique=True,alphabet='1234567890') 
    card_type = models.CharField(max_length=20,choices=CARD_TYPE)
    card_status = models.CharField(max_length=20,choices=CARD_STATUS,default='in_active')
    date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    
    def _str_(self):
        return f'{self.user}'

    
