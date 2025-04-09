# file mimesis/providers/internet.py:48-57
# lines [48, 56, 57]
# branches []

import pytest
from mimesis.enums import MimeType
from mimesis.providers import Internet

@pytest.fixture
def internet_provider():
    return Internet()

def test_content_type_with_mime_type(internet_provider):
    # Test with specified mime_type from MimeType enum
    mime_type = MimeType.APPLICATION
    content_type = internet_provider.content_type(mime_type=mime_type)
    assert content_type.startswith('Content-Type: ')

def test_content_type_without_mime_type(internet_provider):
    # Test without specified mime_type (should cover random selection)
    content_type = internet_provider.content_type()
    assert content_type.startswith('Content-Type: ')
