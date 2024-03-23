# file mimesis/providers/internet.py:48-57
# lines [48, 56, 57]
# branches []

import pytest
from mimesis.enums import MimeType
from mimesis.providers import BaseProvider

# Assuming the Internet class is part of the mimesis.providers.internet module
from mimesis.providers.internet import Internet

@pytest.fixture
def internet_provider():
    return Internet()

def test_content_type_with_mime_type(internet_provider):
    # Test with a specific MimeType
    content_type = internet_provider.content_type(mime_type=MimeType.APPLICATION)
    assert content_type.startswith('Content-Type: application/')

def test_content_type_without_mime_type(internet_provider):
    # Test without specifying a MimeType
    content_type = internet_provider.content_type()
    assert content_type.startswith('Content-Type: ')
