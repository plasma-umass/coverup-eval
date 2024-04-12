# file httpie/utils.py:77-89
# lines []
# branches ['85->exit']

import mimetypes
import pytest
from httpie.utils import get_content_type

def test_get_content_type_with_known_mime_and_encoding(tmp_path, mocker):
    # Setup a temporary file with a known extension
    temp_file = tmp_path / "test.txt"
    temp_file.write_text("Test content", encoding="utf-8")

    # Mock mimetypes to return a known mime type and encoding
    mocker.patch('mimetypes.guess_type', return_value=('text/plain', 'utf-8'))

    # Call the function and assert the returned content type includes the charset
    content_type = get_content_type(str(temp_file))
    assert content_type == 'text/plain; charset=utf-8'

def test_get_content_type_with_unknown_mime(tmp_path, mocker):
    # Setup a temporary file with an unknown extension
    temp_file = tmp_path / "test.unknown"
    temp_file.write_text("Test content", encoding="utf-8")

    # Mock mimetypes to return None for mime type
    mocker.patch('mimetypes.guess_type', return_value=(None, None))

    # Call the function and assert that None is returned
    content_type = get_content_type(str(temp_file))
    assert content_type is None
