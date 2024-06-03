# file httpie/cli/requestitems.py:139-151
# lines [139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 150]
# branches []

import os
import pytest
from httpie.cli.requestitems import load_text_file, KeyValueArg, ParseError

def test_load_text_file_success(tmp_path):
    # Create a temporary file with some text content
    file_path = tmp_path / "testfile.txt"
    file_content = "Hello, world!"
    file_path.write_text(file_content)

    # Create a KeyValueArg instance pointing to the temporary file
    item = KeyValueArg(key=None, sep=None, orig=str(file_path), value=str(file_path))

    # Call the function and assert the content is read correctly
    result = load_text_file(item)
    assert result == file_content

def test_load_text_file_io_error(mocker):
    # Mock the open function to raise an IOError
    mocker.patch("builtins.open", side_effect=IOError("File not found"))

    # Create a KeyValueArg instance with a dummy file path
    item = KeyValueArg(key=None, sep=None, orig="dummy_path", value="dummy_path")

    # Call the function and assert that ParseError is raised
    with pytest.raises(ParseError) as excinfo:
        load_text_file(item)
    assert 'dummy_path' in str(excinfo.value)
    assert 'File not found' in str(excinfo.value)

def test_load_text_file_unicode_decode_error(tmp_path):
    # Create a temporary file with non-UTF8 content
    file_path = tmp_path / "testfile.bin"
    file_content = b'\x80\x81\x82'
    file_path.write_bytes(file_content)

    # Create a KeyValueArg instance pointing to the temporary file
    item = KeyValueArg(key=None, sep=None, orig=str(file_path), value=str(file_path))

    # Call the function and assert that ParseError is raised
    with pytest.raises(ParseError) as excinfo:
        load_text_file(item)
    assert 'cannot embed the content' in str(excinfo.value)
    assert str(file_path) in str(excinfo.value)
