from django.db import models
from django.contrib.auth.models import AbstractUser


class NotificationFriendsUser(models.Model):
    notification = models.ManyToManyField('User', related_name='friends_notification')

    def __str__(self):
        return f'{self.id}'

    class Meta:
        db_table = 'friend_notification'


class User(AbstractUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='users/', blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    friends = models.ManyToManyField('self', related_name='users_friends')
    subscribers = models.ManyToManyField('self', related_name='user_subscriber', symmetrical=False)
    notifications = models.ForeignKey(NotificationFriendsUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'id: {self.id} first_name: {self.first_name} last_name: {self.last_name}'

    class Meta:
        db_table = 'users'



