from django import forms
from ATGApp.models import Review, Stadium, UserProfile
from django.contrib.auth.models import User

class StadiumForm(forms.ModelForm):
    name = forms.CharField(Stadium._meta.get_field("name").max_length, help_text="Please enter the Stadium name.")
    capacity = forms.IntegerField(Stadium._meta.get_field("capacity").max_length, help_text="Please the Stadiums Capacity.")
    postcode = forms.CharField(Stadium._meta.get_field("name").max_length, help_text="Please enter the Postcode of the Stadium.")
    #image input
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Stadium
        fields = ('name','capacity', 'postcode', 'image')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)


