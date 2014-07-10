from django import forms
from django.contrib.auth.forms import UserCreationForm
from hair.models import *
from captcha.fields import CaptchaField


class InspireUserCreationForm(UserCreationForm):
        email = forms.EmailField(required=True)
        first_name = forms.CharField(max_length=100)
        last_name = forms.CharField(max_length=100)
        is_staff = forms.BooleanField(required=False)
        # captcha = CaptchaField()
        class Meta:
            model = PhoneUser
            fields = ("username", 'first_name', 'last_name', 'phone', 'is_staff', "email", "password1",
                     "password2")

        def clean_username(self):
            # Since User.username is unique, this check is redundant,
            # but it sets a nicer error message than the ORM. See #13147.
            username = self.cleaned_data["username"]
            try:
                PhoneUser.objects.get(username=username)
            except PhoneUser.DoesNotExist:
                return username
            raise forms.ValidationError(
                self.error_messages['duplicate_username'],
                code='duplicate_username',
            )


class CommentForm(forms.Form):

        content = forms.CharField()

        class Meta:
            model = Comment
            fields = 'content'