from django import forms

from blog.models import Post, Category


class CreatePostForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=True,
        label='Категории',
        help_text='Выберите одну или несколько категорий'
    )

    class Meta:
        model = Post
        fields = ('category', 'title', 'description', 'content', 'art_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание'}),
            'content': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите контент'}),
            'art_image': forms.TextInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }

    def __init__(self, *args, **kwargs):
        super(CreatePostForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()
