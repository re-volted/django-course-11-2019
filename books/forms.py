from django import forms
from books.models import Comment


# class CommentForm(forms.Form):
#     username = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     text = forms.CharField(widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['book']