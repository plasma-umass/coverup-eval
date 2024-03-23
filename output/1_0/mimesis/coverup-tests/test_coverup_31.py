# file mimesis/providers/file.py:55-63
# lines [55, 61, 62, 63]
# branches []

import pytest
from mimesis.enums import MimeType
from mimesis.providers import File

@pytest.fixture
def file_provider():
    return File()

def test_mime_type_with_none(file_provider):
    mime = file_provider.mime_type()
    assert isinstance(mime, str)

def test_mime_type_with_specific_type(file_provider):
    specific_type = MimeType.APPLICATION
    mime = file_provider.mime_type(type_=specific_type)
    assert isinstance(mime, str)
    assert mime.startswith('application/')

def test_mime_type_with_all_enum_types(file_provider):
    for mime_type in MimeType:
        mime = file_provider.mime_type(type_=mime_type)
        assert isinstance(mime, str)
        assert any(mime.startswith(prefix) for prefix in mime_type.value)
