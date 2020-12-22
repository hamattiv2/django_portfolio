from django.db import models
from django.contrib.auth import get_user_model

class Tags(models.Model):
    tag = models.CharField(max_length=30)
    create_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="tag_create_user")
    update_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="tag_update_user")
    insert_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

class Articles(models.Model):
    title = models.CharField(max_length=200, error_messages={"required": "入力必須です"})
    text = models.TextField(error_messages={"required": "入力必須です"})
    tag = models.ManyToManyField(Tags, through="ArticleTag", blank=True)
    create_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="article_create_user")
    update_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="article_update_user")
    insert_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ArticleTag(models.Model):
        tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
        article = models.ForeignKey(Articles, on_delete=models.CASCADE)