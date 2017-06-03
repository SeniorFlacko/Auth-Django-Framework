import urllib2
from django import forms
from .models import Image
from django.core.files.base import ContentFile
from django.utils.text import slugify

class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {
        'url': forms.HiddenInput,
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg','jpeg']
        extension = url.rsplit('.',1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The given URL does not match valid image extensions.')

        return url

    def save(self, force_insert=False,force_update=False,commit=True):
        image = super(ImageCreateForm,self).save(commit=False) #Create a instance of image with commit=False
        image_url = self.cleaned_data['url']
        image_name = '{}.{}'.format(slugify(image.title),
                                    image_url.rsplit('.',1)[1].lower())
        
        #download image from the URL
        req = urllib2.Request(image_url)
        response = urllib2.urlopen(req)
        #response = urllib2.request.urlopen(image_url) #use urllib module to download the image
        image.image.save(image_name,
                         ContentFile(response.read()),
                         save=False)

        if commit: #we save form only when commit is True
            image.save()

        return image
            