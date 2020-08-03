from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db import models
import uuid
# Create your models here.

class User(AbstractUser):

    # around the globe.
    name = CharField(max_length=255)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    role = CharField(max_length=256)
    # def delete_user(self):
    #     return reverse("staff:delete-user", args=[self.uuid])
