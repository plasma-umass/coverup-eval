# file lib/ansible/module_utils/urls.py:1544-1654
# lines [1572, 1573, 1587, 1591, 1592, 1593, 1594, 1597, 1598, 1634, 1636, 1637, 1639, 1649]
# branches ['1571->1572', '1583->1597', '1586->1587', '1590->1591', '1626->1634', '1645->1649']

import pytest
from ansible.module_utils.urls import prepare_multipart
from collections.abc import Mapping
from io import BytesIO
import mimetypes
import os
import email.mime.multipart
import email.mime.application
import email.mime.nonmultipart
import email.policy
import email.generator
import email.utils
import email.parser

# Mocking os.path.basename to ensure it's called for coverage
@pytest.fixture
def mock_basename(mocker):
    mocker.patch('os.path.basename', return_value='true')

# Mocking open to ensure it's called for coverage
@pytest.fixture
def mock_open(mocker):
    mocker.patch('builtins.open', mocker.mock_open(read_data=b'file content'))

# Mocking mimetypes.guess_type to ensure it's called for coverage
@pytest.fixture
def mock_mimetypes(mocker):
    mocker.patch('mimetypes.guess_type', return_value=(None, None))

# Mocking to_bytes to ensure it's called for coverage
@pytest.fixture
def mock_to_bytes(mocker):
    mocker.patch('ansible.module_utils._text.to_bytes', return_value=b'content')

# Mocking to_native to ensure it's called for coverage
@pytest.fixture
def mock_to_native(mocker):
    mocker.patch('ansible.module_utils._text.to_native', return_value='true')

@pytest.fixture
def mock_cStringIO(mocker):
    mocker.patch('ansible.module_utils.urls.cStringIO', return_value=BytesIO())

def test_prepare_multipart(mock_basename, mock_open, mock_mimetypes, mock_to_bytes, mock_to_native, mock_cStringIO):
    # Test with non-Mapping input
    with pytest.raises(TypeError):
        prepare_multipart("not a mapping")

    # Test with empty filename and content
    with pytest.raises(ValueError):
        prepare_multipart({"field": {}})

    # Test with a valid mapping including a file and a text field
    fields = {
        "file1": {
            "filename": "/bin/true",
            "mime_type": "application/octet-stream"
        },
        "text_form_field": "value"
    }
    content_type, body = prepare_multipart(fields)

    # Assertions to check postconditions
    assert 'multipart/form-data' in content_type
    assert b'name="text_form_field"' in body
    assert b'name="file1"' in body
    assert b'filename="true"' in body
    assert b'Content-Transfer-Encoding: base64' in body or b'file content' in body

    # Test with a valid mapping including a file without mime_type
    fields = {
        "file2": {
            "filename": "/bin/true",
            "content": "text based file content"
        }
    }
    content_type, body = prepare_multipart(fields)

    # Assertions to check postconditions
    assert 'multipart/form-data' in content_type
    assert b'name="file2"' in body
    assert b'filename="true"' in body
    assert b'text based file content' in body

    # Test with a valid mapping including a file with an unknown mime_type
    fields = {
        "file3": {
            "filename": "/bin/true",
            "content": "text based file content",
            "mime_type": None
        }
    }
    content_type, body = prepare_multipart(fields)

    # Assertions to check postconditions
    assert 'multipart/form-data' in content_type
    assert b'name="file3"' in body
    assert b'filename="true"' in body
    assert b'text based file content' in body
