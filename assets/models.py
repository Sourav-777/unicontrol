from django.db import models

class Asset(models.Model):

    OS_CHOICES = [
        ('windows', 'Windows'),
        ('linux', 'Linux'),
        ('macos', 'MacOS'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('retired', 'Retired'),
    ]

    hostname = models.CharField(max_length=100, unique=True)
    os_type = models.CharField(max_length=20, choices=OS_CHOICES)
    ip_address = models.GenericIPAddressField()
    owner = models.CharField(max_length=100)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )

    compliance_status = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hostname
