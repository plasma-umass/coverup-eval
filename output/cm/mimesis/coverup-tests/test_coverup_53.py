# file mimesis/schema.py:113-115
# lines [113, 114, 115]
# branches []

import pytest
from mimesis.schema import AbstractField

class DummyField(AbstractField):
    def __init__(self, locale='en'):
        self.locale = locale

def test_abstract_field_str_representation():
    dummy_field = DummyField()
    assert str(dummy_field) == 'DummyField <en>'

    dummy_field_with_locale = DummyField(locale='es')
    assert str(dummy_field_with_locale) == 'DummyField <es>'
