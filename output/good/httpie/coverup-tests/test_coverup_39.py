# file httpie/cli/requestitems.py:139-151
# lines [139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 150]
# branches []

import os
import pytest
from httpie.cli.requestitems import KeyValueArg, ParseError, load_text_file

def test_load_text_file_ioerror(mocker, tmp_path):
    # Create a temporary file and remove it to simulate IOError
    temp_file = tmp_path / "tempfile.txt"
    temp_file.write_text("content")
    temp_file_path = str(temp_file)
    temp_file.unlink()

    # Mock os.path.expanduser to return the path of the removed file
    mocker.patch('os.path.expanduser', return_value=temp_file_path)

    # Create a KeyValueArg instance with dummy key and sep values
    item = KeyValueArg(orig='--string', value=temp_file_path, key='string', sep='=')

    # Expect ParseError due to IOError (file not found)
    with pytest.raises(ParseError) as excinfo:
        load_text_file(item)
    assert str(excinfo.value).startswith(f'"{item.orig}":')

def test_load_text_file_unicode_error(mocker, tmp_path):
    # Create a temporary file with non-UTF8 content
    temp_file = tmp_path / "tempfile.bin"
    temp_file.write_bytes(b'\xff\xff\xff\xff')

    # Mock os.path.expanduser to return the path of the binary file
    mocker.patch('os.path.expanduser', return_value=str(temp_file))

    # Create a KeyValueArg instance with dummy key and sep values
    item = KeyValueArg(orig='--binary', value=str(temp_file), key='binary', sep='=')

    # Expect ParseError due to UnicodeDecodeError
    with pytest.raises(ParseError) as excinfo:
        load_text_file(item)
    assert str(excinfo.value).startswith(f'"{item.orig}": cannot embed the content of "{item.value}"')
