# file mimesis/providers/file.py:33-40
# lines [33, 39, 40]
# branches []

import pytest
from mimesis.providers.file import File

@pytest.fixture
def file_provider():
    return File()

def test_file_provider_sub(file_provider):
    # Test with string containing spaces
    string_with_spaces = "This is a test string"
    result = file_provider._File__sub(string_with_spaces)
    assert " " not in result
    assert "_" in result or "-" in result

    # Test with string containing multiple consecutive spaces
    string_with_multiple_spaces = "This   is   another   test   string"
    result = file_provider._File__sub(string_with_multiple_spaces)
    assert " " not in result
    assert "_" in result or "-" in result

    # Test with string containing no spaces
    string_without_spaces = "NoSpacesHere"
    result = file_provider._File__sub(string_without_spaces)
    assert result == string_without_spaces

    # Test with empty string
    empty_string = ""
    result = file_provider._File__sub(empty_string)
    assert result == empty_string
