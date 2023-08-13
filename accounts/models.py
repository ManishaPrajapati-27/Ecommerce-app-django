from django.db import models

# Create your models here.

from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from .emails import send_account_activation_email
from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
from cart.models import CartItems

# from cart.models import CartItems

# Create your models here.

class Account(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="account")
    email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="accounts/%Y/%m/%d/", null=True, blank=True)

    def get_cart_count(self):
        return CartItems.objects.filter(cart__is_paid=False, cart__user=self.user).count()

@receiver(post_save, sender=User)
def send_email_token(sender, instance, created, **kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())
            Account.objects.create(user=instance, email_token=email_token)
            email = instance.email
            send_account_activation_email(email, email_token)

    except Exception as e:
        print(e)
