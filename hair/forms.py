from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from hair.models import Categories


class InspireUserCreationForm(UserCreationForm):
        email = forms.EmailField(required=True)
        first_name = forms.CharField(max_length=100)
        last_name = forms.CharField(max_length=100)
        image = forms.ImageField(required=False)
        class Meta:
            model = User
            fields = ('image', "username", 'first_name', 'last_name', "email", "password1",
                     "password2")

        def clean_username(self):
            # Since User.username is unique, this check is redundant,
            # but it sets a nicer error message than the ORM. See #13147.
            username = self.cleaned_data["username"]
            try:
                User.objects.get(username=username)
            except User.DoesNotExist:
                return username
            raise forms.ValidationError(
                self.error_messages['duplicate_username'],
                code='duplicate_username',
            )


class PostForm(forms.Form):

    title = forms.CharField(max_length=120)
    body = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 15}))
    category = forms.ModelChoiceField(queryset=Categories.objects.all())


class CommentForm(forms.Form):
    email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 15}))