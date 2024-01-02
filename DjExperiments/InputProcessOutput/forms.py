from django import forms

class blogForm(forms.Form):
    name = forms.CharField(max_length=25)
    topic = forms.CharField(max_length=25)
    blogPost = forms.CharField(required=False,
                               widget=forms.Textarea)
