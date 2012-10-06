from __future__ import absolute_import

from .models import HKPlace

from django.forms import ModelForm


class HKPlaceForm(ModelForm):

    class Meta:
        model = HKPlace
