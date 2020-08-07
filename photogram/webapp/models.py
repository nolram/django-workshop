from django.db import models
from django.conf import settings

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=255)
    photo = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    fk_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_post', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.pk} - {self.fk_user} - {self.created_at}'


class Like(models.Model):
    id = models.AutoField(primary_key=True)
    fk_post = models.ForeignKey('Post', related_name='like_post', on_delete=models.CASCADE)
    fk_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_like', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.pk} - {self.fk_post} - {self.fk_user} - {self.created_at}'

    class Meta:
        unique_together = (('fk_post', 'fk_user'))


class Follower(models.Model):
    id = models.AutoField(primary_key=True)
    user_following = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_following', on_delete=models.CASCADE)
    user_follower = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_follower', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.pk} - {self.user_following} - {self.user_follower} - {self.created_at}'

    class Meta:
        unique_together = (('user_following', 'user_follower'))