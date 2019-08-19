from django import forms
from .models import NewPost
from ckeditor.fields import RichTextFormField


class NewPostForm(forms.ModelForm):

    class Meta:
        model = NewPost
        fields = ['category', 'title', 'content', 'image', 'publish']

        widgets = {
            'category': forms.Select(
                attrs={'class': 'form-control js-example-basic-select2', 'placeholder': 'Select '}),
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Give post a title', }),
            'content': RichTextFormField(),
            'publish': forms.CheckboxInput(
                attrs={'class': 'js-switch'}),
            'image': forms.ClearableFileInput()
        }
