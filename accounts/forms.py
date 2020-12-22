from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model
from django import forms

class LoginForm(auth_forms.AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.files.values():
            field.widget.attrs["class"] = "w-100"
            field.widget.attr["placeholder"] = filed.label

class SignUpForm(auth_forms.UserCreationForm):
    required_kwargs = {}
    required_kwargs["required"] = True
    required_kwargs["error_messages"] = {"required": "入力必須です"}
    username = forms.CharField(**required_kwargs)
    password1 = forms.CharField(**required_kwargs)
    password2 = forms.CharField(**required_kwargs)

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password1", "password2"]
