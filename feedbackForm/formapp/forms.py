from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Email', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    title = forms.CharField(label='Title', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    feed = forms.CharField(label='Feedback Description', max_length=200, widget=forms.Textarea(attrs={'class': 'form-control'}))