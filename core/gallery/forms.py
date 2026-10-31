from django import forms
from django.contrib.auth.forms import UserCreationForm
from PIL import Image
from .models import Photo

class RegisterForm(UserCreationForm):
    accept_privacy = forms.BooleanField(
        required=True,
        label='I confirm I have permission to upload these photos and accept the privacy notice.',
    )
    # This inherits all standard fields (Username, Password, Confirm Password)
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + () # Add 'email' here if you want it

class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']

    def clean_image(self):
        image = self.cleaned_data['image']
        allowed_types = {'image/jpeg', 'image/png', 'image/webp'}
        if image.content_type not in allowed_types:
            raise forms.ValidationError('Upload a JPEG, PNG, or WebP image.')
        if image.size > 10 * 1024 * 1024:
            raise forms.ValidationError('Each image must be 10 MB or smaller.')
        try:
            verifier = Image.open(image)
            verifier.verify()
            image.seek(0)
        except (OSError, ValueError) as error:
            raise forms.ValidationError('The uploaded file is not a valid image.') from error
        return image
