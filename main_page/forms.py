from django import forms
from django.contrib.auth.models import User

from main_page.models import StudentProfile, CourseRegistration


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        # 'first_name', 'last_name')
        fields = ('username', 'email', 'password', )


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ('category', )


class CourseRegistrationForm(forms.ModelForm):
    class Meta:
        model = CourseRegistration
        fields = ('course', 'student')
