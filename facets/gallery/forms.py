"""
Forms for Update and Delete of Media Records

"""

from django import forms
from gallery.models import Media


# Write your forms here.
class MediaModelForm(forms.ModelForm):
    """
    A model for for manipulating Media Records
    """
    class Meta:
        model = Media
        fields= ('name', 'type', 'file',
                  'is_published', 'tags')