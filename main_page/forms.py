from django import forms
from django.contrib.auth.models import User

from main_page.models import StudentProfile, CourseRegistration
from datetime import date


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        # 'first_name', 'last_name')
        fields = ('username', 'email', 'password',)


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ('category', )


class CourseRegistrationForm(forms.ModelForm):
    class Meta:
        model = CourseRegistration
        fields = ('course', 'student')


def validate_month(value):
    return True if 1 <= value <= 12 else False


def validate_year(value):
    year = date.today().year
    return True if year <= value <= year+3 else False


class MonthYearForm(forms.Form):
    month = forms.IntegerField(required=True, validators=[validate_year])
    year = forms.IntegerField(required=True, validators=[validate_month])
