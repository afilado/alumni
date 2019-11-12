from django import forms
from django.contrib.auth.models import User

PASSING_YEAR = (
    ('2010', '2010'),
    ('2011', '2011'),
    ('2012', '2012'),
    ('2013', '2013'),
    ('2014', '2014'),
    ('2015', '2015'),
    ('2016', '2016'),
    ('2017', '2017'),
    ('2018', '2018'),
    ('2019', '2019'),
    ('2020', '2020'),
)

BRANCH = (
    ('CSE', "Computer Science Engineering"),
    ('ME', 'Mechanical Engineering'),
    ('CE', 'Civil Engineering'),
    ('CHE', 'Chemical Engineering'),
    ('EE', 'Electrical Engineering'),
    ('ECE', 'Electronics and Communication Engineering0'),
)

SEX = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
)


class SignUpForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_Password = forms.CharField(widget=forms.PasswordInput())
    passing_ear = forms.ChoiceField(choices=PASSING_YEAR)
    branch = forms.ChoiceField(choices=BRANCH)
    gender = forms.ChoiceField(choices=SEX)
