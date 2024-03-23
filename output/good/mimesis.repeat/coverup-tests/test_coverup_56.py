# file mimesis/schema.py:113-115
# lines [113, 114, 115]
# branches []

import pytest
from mimesis.schema import AbstractField

class DummyField(AbstractField):
    def __init__(self, locale='en'):
        self.locale = locale

@pytest.fixture
def dummy_field():
    return DummyField()

def test_abstract_field_str(dummy_field):
    assert str(dummy_field) == 'DummyField <en>'
