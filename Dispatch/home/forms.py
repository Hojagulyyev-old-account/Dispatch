from django import forms

from .models import Post

class PostUpdateForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'fileContainer'}))

    class Meta:
        model = Post
        fields = ('body', 'image')
