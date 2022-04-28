from django.db import models
from accounts.models import User
# Create your models here.

class RollPaper(models.Model):
    
    title = models.CharField(max_length = 100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        User,
        # settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
