from django import forms

from blog.models import Post, Category


class CreatePostForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label='Категории',
        help_text='Выберите одну или несколько категорий'




    )


    class Meta:
        model = Post
        fields = ('category', 'title', 'description', 'content', 'art_image')


    def __init__(self, *args, **kwargs):
        super(CreatePostForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()
