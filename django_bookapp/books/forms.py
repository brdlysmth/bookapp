from django import forms
from .models import Post


class BookRegisterForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['title', 'author', 'summary']
		