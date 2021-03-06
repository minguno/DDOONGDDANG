from django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm, 
    AuthenticationForm, 
    UsernameField,
    PasswordChangeForm,
    SetPasswordForm,
    PasswordResetForm
)
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django import forms
from .validators import validate_realname

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'username',
            }
        )
    )
    email = forms.EmailField(
        label='이메일',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'email',
            }
        )
    )
    realname = forms.CharField(
        validators=[validate_realname],
        label='이름',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'realname',
                'data-bs-toggle': 'tooltip',
                'data-bs-placement': 'top',
            }
        )
    )
    nickname = forms.CharField(
        label='닉네임',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password1 = forms.CharField(
        label="비밀번호",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control',
            }),
    )
    password2 = forms.CharField(
        label="비밀번호 확인",
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control'
            }),
        strip=False,
    )    
    class Meta:
        model = User
        fields = ('username','realname','email', 'nickname','password1', 'password2',)


class CustomUserChangeForm(UserChangeForm):
    nickname = forms.CharField(
        label='닉네임',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )    
    password = None

    class Meta:
        model = User
        fields = ('nickname',)


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'class': 'form-control',
                'id': 'username',
                },
                ),
    )
    password = forms.CharField(
        label="비밀번호",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'class': 'form-control'}),
    )
    # 오류메시지 커스터마이징
    error_messages = {
                'invalid_login': (
                # "Please enter a correct %(username)s and password. Note that both "
                "올바른 아이디와 비밀번호를 입력해주세요. 두 필드 모두 대문자와 소문자를 구분합니다."
                ),
                'inactive': ("This account is inactive."),
                }

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(
        label='기존 비밀번호',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'class': 'form-control',
            }
        )
    
    )
    new_password1 = forms.CharField(
        label='새 비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    new_password2 = forms.CharField(
        label='새 비밀번호 (확인)',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password = None

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2',)

    

class CheckPasswordForm(forms.Form):
    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control', 
                }
        ),
    )
    def __init__(self, user, *args, **kwargs): #현재 접속중인 사용자의 password 가져오기 위해 init 메서드로 user객체 생성
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self): #clean 메서드로 form에 입력된 password값과 init으로 생성된 현재 사용자의 password 값을 check_password 통해 비교
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = self.user.password

        if password:
            if not check_password(password, confirm_password):
                self.add_error('password', '비밀번호가 일치하지 않습니다.')


class CustomPasswordRestForm(PasswordResetForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            msg = _("해당 이메일의 사용자가 존재하지 않습니다.")
            self.add_error('email', msg)
        return email