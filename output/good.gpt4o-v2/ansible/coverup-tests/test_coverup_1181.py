# file: lib/ansible/module_utils/urls.py:1544-1654
# asked: {"lines": [1591, 1592, 1593, 1594, 1634, 1636, 1637, 1639, 1649], "branches": [[1590, 1591], [1626, 1634], [1645, 1649]]}
# gained: {"lines": [1591, 1592, 1593, 1594], "branches": [[1590, 1591]]}

import pytest
import email
import mimetypes
import os
from ansible.module_utils.urls import prepare_multipart
from ansible.module_utils.six import PY3

@pytest.fixture
def create_temp_file(tmp_path):
    temp_file = tmp_path / "testfile.txt"
    temp_file.write_text("This is a test file.")
    return temp_file

def test_prepare_multipart_with_mime_guess(monkeypatch, create_temp_file):
    fields = {
        "file1": {
            "filename": str(create_temp_file)
        }
    }

    def mock_guess_type(url, strict=True):
        return ('text/plain', None)

    monkeypatch.setattr(mimetypes, 'guess_type', mock_guess_type)

    content_type, body = prepare_multipart(fields)
    assert 'multipart/form-data' in content_type
    assert b'testfile.txt' in body

def test_prepare_multipart_with_mime_guess_exception(monkeypatch, create_temp_file):
    fields = {
        "file1": {
            "filename": str(create_temp_file)
        }
    }

    def mock_guess_type(url, strict=True):
        raise Exception("Mocked exception")

    monkeypatch.setattr(mimetypes, 'guess_type', mock_guess_type)

    content_type, body = prepare_multipart(fields)
    assert 'multipart/form-data' in content_type
    assert b'testfile.txt' in body

def test_prepare_multipart_py2(monkeypatch, create_temp_file):
    fields = {
        "file1": {
            "filename": str(create_temp_file)
        }
    }

    monkeypatch.setattr('ansible.module_utils.six.PY3', False)

    class MockStringIO:
        def __init__(self):
            self.value = b""

        def write(self, data):
            self.value += data

        def getvalue(self):
            return self.value

    monkeypatch.setattr('ansible.module_utils.six.moves.cStringIO', MockStringIO)

    content_type, body = prepare_multipart(fields)
    assert 'multipart/form-data' in content_type
    assert b'testfile.txt' in body

def test_prepare_multipart_py2_header_parser(monkeypatch, create_temp_file):
    fields = {
        "file1": {
            "filename": str(create_temp_file)
        }
    }

    monkeypatch.setattr('ansible.module_utils.six.PY3', False)

    class MockStringIO:
        def __init__(self):
            self.value = b""

        def write(self, data):
            self.value += data

        def getvalue(self):
            return self.value

    monkeypatch.setattr('ansible.module_utils.six.moves.cStringIO', MockStringIO)

    class MockHeaderParser:
        def parsestr(self, data):
            return email.message_from_string(data)

    monkeypatch.setattr('email.parser.HeaderParser', MockHeaderParser)

    content_type, body = prepare_multipart(fields)
    assert 'multipart/form-data' in content_type
    assert b'testfile.txt' in body
