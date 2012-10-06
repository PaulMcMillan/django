import warnings

from django.contrib.localflavor.gb.gb_regions import (
    ENGLAND_REGION_CHOICES, NORTHERN_IRELAND_REGION_CHOICES,
    WALES_REGION_CHOICES, SCOTTISH_REGION_CHOICES, GB_NATIONS_CHOICES,
    GB_REGION_CHOICES)
warnings.warn(
    'The "UK" prefix for United Kingdom has been deprecated in favour of the '
    'GB code. Please use the new GB-prefixed names.', DeprecationWarning)

UK_NATIONS_CHOICES = GB_NATIONS_CHOICES
UK_REGION_CHOICES  = GB_REGION_CHOICES
