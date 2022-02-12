from django.forms import ModelForm
from .models import Post, Category


class PostsForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'postCategorys', 'categoryType']
        