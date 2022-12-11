from django import forms
from .models import Image, ImageAlbum


class NewImageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["album"].queryset = ImageAlbum.objects.all()

    class Meta:
        model = Image
        fields = ["album", "image", "description"]
