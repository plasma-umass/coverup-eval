# file mimesis/providers/internet.py:48-57
# lines [48, 56, 57]
# branches []

import pytest
from mimesis.providers.internet import Internet
from mimesis.enums import MimeType

@pytest.fixture
def internet():
    return Internet()

def test_content_type_default(internet):
    content_type = internet.content_type()
    assert content_type.startswith('Content-Type: ')

def test_content_type_specific(internet):
    content_type = internet.content_type(MimeType.APPLICATION)
    assert content_type.startswith('Content-Type: application/')
