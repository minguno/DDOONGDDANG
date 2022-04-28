from django.contrib.auth.forms import UserChangeForm,UserCreationForm
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','realname','nickname','password1', 'password2')


class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ('nickname',)