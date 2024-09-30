from django import forms
from .models import Post

class PostCreate(forms.ModelForm):
    class Meta:
      model = Post
      fields = ['title','body','image']


    widget = {
       'title': forms.TextInput(attrs={
          'class':'form-titlebox',
          'placeholder':'Enter recipe title here'
       }),
       'body': forms.Textarea(attrs={
          'class':'form-body-field',
          'placeholder':'enter recipe'
       }),
       'image' : forms.ClearableFileInput(attrs={
          'class':'form-image-field',
       }),
    }

    help_text = {
       'title': 'This should contain the title of your recipe',
       'body': 'This should contain the recipe content'
    }

    error_messages = {
       'title': {
          'required': 'please enter a title for the recipe',
          'max-length': 'Title cannot be longer than 250 character'
       },
        'body': {
          'required': 'Body cannot empty',
       }
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = "Recipe Title"
        self.fields['body'].label = "Recipe Content"
        self.fields['image'].label = "Image of food"
          




