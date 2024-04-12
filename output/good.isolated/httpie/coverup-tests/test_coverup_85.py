# file httpie/cli/requestitems.py:105-117
# lines [106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116]
# branches []

import os
import pytest
from httpie.cli.requestitems import KeyValueArg, ParseError, process_file_upload_arg

SEPARATOR_FILE_UPLOAD_TYPE = ';type='

@pytest.fixture
def mock_file(tmp_path):
    file_path = tmp_path / "testfile.txt"
    file_path.write_text("test content")
    return str(file_path)

def test_process_file_upload_arg_with_type(mock_file):
    arg = KeyValueArg('foo', f'{mock_file}{SEPARATOR_FILE_UPLOAD_TYPE}text/plain', '=', 'foo=' + f'{mock_file}{SEPARATOR_FILE_UPLOAD_TYPE}text/plain')
    basename, file_obj, mime_type = process_file_upload_arg(arg)
    assert basename == 'testfile.txt'
    assert mime_type == 'text/plain'
    with file_obj:
        assert file_obj.read() == b'test content'

def test_process_file_upload_arg_without_type(mock_file):
    arg = KeyValueArg('foo', mock_file, '=', 'foo=' + mock_file)
    basename, file_obj, mime_type = process_file_upload_arg(arg)
    assert basename == 'testfile.txt'
    assert mime_type is None or mime_type == 'text/plain'  # Assuming get_content_type returns 'text/plain' for '.txt'
    with file_obj:
        assert file_obj.read() == b'test content'

def test_process_file_upload_arg_file_not_found():
    arg = KeyValueArg('foo', 'nonexistentfile.txt', '=', 'foo=nonexistentfile.txt')
    with pytest.raises(ParseError) as exc_info:
        process_file_upload_arg(arg)
    assert 'nonexistentfile.txt' in str(exc_info.value)
