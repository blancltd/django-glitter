from django import forms

from .models import ImageBlock


class ImageBlockForm(forms.ModelForm):
    class Meta:
        model = ImageBlock
        exclude = ()

    def __init__(self, *args, **kwargs):
        self.base_fields['image'].widget.attrs['class'] = 'image-related-field'
        super().__init__(*args, **kwargs)
