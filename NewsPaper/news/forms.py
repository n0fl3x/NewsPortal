from django import forms

from .models import Post


class PostCreateForm(forms.ModelForm):
    text = forms.CharField(min_length=1)

    class Meta:
        model = Post
        fields = [
            'author_of_post',
            # 'post_type',
            # 'date_of_creation',
            'post_category',
            'title',
            'text',
            # 'rating_of_post',
        ]
