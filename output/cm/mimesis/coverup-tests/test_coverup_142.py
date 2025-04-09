# file mimesis/providers/generic.py:34-36
# lines [34, 35]
# branches []

import pytest
from mimesis.providers.generic import Generic
from mimesis import locales

# Assuming the Generic class has more methods and attributes that are not shown in the snippet provided.

def test_generic_initialization():
    # Test initialization with different locales
    for locale in locales.LIST_OF_LOCALES:
        generic_provider = Generic(locale)
        assert generic_provider.locale == locale
