from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        
class SignUpForm(UserCreationForm):
	username = forms.CharField(max_length=30, required=True, help_text='Optional.')
	first_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
	birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	password1 = forms.CharField(max_length=30, required=True, help_text='Optional.')
	password2 = forms.CharField(max_length=30, required=True, help_text='Optional.')
	
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'birth_date', 'email', 'password1', 'password2', )

#PicApril		
class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()