# file mimesis/schema.py:113-115
# lines [113, 114, 115]
# branches []

import pytest
from mimesis.schema import AbstractField

class DummyField(AbstractField):
    def __init__(self, locale):
        self.locale = locale

def test_abstract_field_str_representation():
    locale = 'en'
    dummy_field = DummyField(locale)
    expected_str = 'DummyField <{}>'.format(locale)
    
    assert str(dummy_field) == expected_str
