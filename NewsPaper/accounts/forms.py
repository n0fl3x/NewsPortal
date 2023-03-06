from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from allauth.account.forms import SignupForm

from news.models import Author


class SignUpForm(UserCreationForm):

    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class CustomSignupForm(SignupForm):

    def save(self, request):
        user = super().save(request)
        authors = Group.objects.get(name='authors')
        user.groups.add(authors)
        Author.objects.create(author_user=User.objects.get(pk=user.id))
        return user
