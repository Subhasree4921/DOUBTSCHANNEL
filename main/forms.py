from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Answer, Question, CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ("detail",)


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ("title", "detail", "tags")


class ProfileForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "username", "bio", "location")


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username",)
        field_classes = {"username": UsernameField}
