from django import forms 

class ProfileForm(forms.Form):
    user_image = forms.ImageField()
    # user_image = forms.FileField()