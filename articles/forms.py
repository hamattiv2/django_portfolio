from django import forms
from django.core.exceptions import ValidationError
from .models import Articles
from django.contrib.auth import get_user_model

class ArticleForm(forms.ModelForm):
    required_kwargs = {}
    required_kwargs["required"] = True
    required_kwargs["error_messages"] = {"required": "入力必須です"}
    title = forms.CharField(**required_kwargs)
    text = forms.CharField(widget=forms.Textarea, **required_kwargs)

    class Meta:
        model = Articles
        fields = ["title", "text", "create_user", "update_user"]
