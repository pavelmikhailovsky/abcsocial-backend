from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Comment(models.Model):
    text = models.TextField()
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='parent_comments',
    )
    # user_page = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE,
    #     blank=True,
    #     null=True,
    #     related_name='comment_on_page',
    # )
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_comment')
    # post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True, related_name='post_comments')

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'comments'
