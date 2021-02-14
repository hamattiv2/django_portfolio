from django import forms
from django.core.exceptions import ValidationError
from .models import Articles
from django.contrib.auth import get_user_model
from django.core.files.storage import FileSystemStorage
from django.conf import settings

class ArticleForm(forms.ModelForm):
    required_kwargs = {}
    required_kwargs["required"] = True
    required_kwargs["error_messages"] = {"required": "入力必須です"}
    title = forms.CharField(**required_kwargs)
    text = forms.CharField(widget=forms.Textarea, **required_kwargs)
    plan_document = forms.FileField(**required_kwargs)

    class Meta:
        model = Articles
        fields = ["title", "text", "create_user", "update_user", 'plan_document']

    def save(self):
        plan_document = self.cleaned_data['plan_document']
        media_dir = settings.MEDIA_ROOT + 'plan'
        fileobject = FileSystemStorage()
        fileobject.save('plan/{}'.format(plan_document.name), plan_document)

        instance = super(ArticleForm, self).save(commit=True)
        return instance