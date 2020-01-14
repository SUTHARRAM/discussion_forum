from django import forms

#from pagedown.widget import PagedownWidget

from .models import Post

class PostForm(forms.ModelForm):

    content = forms.CharField()
    #publish = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Post
        fields = [
            "title", 
            "content", 
            "image", 
            #"publish",
        ]