from django.db import models
from django.contrib.auth.models import User

# Role choices for users
ROLE_CHOICES = (
    ('hod', 'hod'),
    ('reg', 'reg'),
    ('vc', 'vc'),
    ('admin', 'Admin'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return self.user.username
