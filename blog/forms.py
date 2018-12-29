from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    name=forms.CharField(max_length=25,widget=forms.TextInput(attrs={'placeholder':'Enter your Name'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter your Email'}))
    to=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter to Email'}))
    comments=forms.CharField(required=False,widget=forms.Textarea(attrs={'placeholder':'Enter your comments','rows':4, 'cols':58}))
    
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        
        fields=('name','email','body')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Enter your Name'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter your Email'}),
            'body':forms.Textarea(attrs={'placeholder':'Enter your Commnets','rows':4, 'cols':58})

        }
      