from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    auth_user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class App(models.Model):
    owner = models.ManyToOneRel(
        Account, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=100, null=False)
    summary = models.CharField(max_length=100, null=False)
    content = models.CharField(max_length=100, null=False)
    s3_url = models.CharField(max_length=200, null=False)
    app_url = models.CharField(max_length=200, null=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
