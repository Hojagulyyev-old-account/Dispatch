from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'newpst-input'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'fileContainer'}))

    class Meta:
        model = Post
        fields = ('body', 'image')
