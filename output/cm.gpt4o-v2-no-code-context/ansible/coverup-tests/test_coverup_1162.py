# file: lib/ansible/module_utils/urls.py:1544-1654
# asked: {"lines": [1591, 1592, 1593, 1594, 1634, 1636, 1637, 1639, 1649], "branches": [[1590, 1591], [1626, 1634], [1645, 1649]]}
# gained: {"lines": [1591, 1592, 1593, 1594], "branches": [[1590, 1591]]}

import pytest
import email
import mimetypes
import os
from ansible.module_utils.urls import prepare_multipart
from collections.abc import Mapping
from ansible.module_utils.six import string_types, PY3
from ansible.module_utils._text import to_bytes, to_native

def test_prepare_multipart_with_mime_guess(monkeypatch):
    fields = {
        "file1": {
            "filename": "/bin/true",
            "mime_type": None
        }
    }

    def mock_guess_type(filename, strict):
        return 'application/octet-stream', None

    monkeypatch.setattr(mimetypes, 'guess_type', mock_guess_type)
    content_type, body = prepare_multipart(fields)
    assert 'multipart/form-data' in content_type
    assert b'application/octet-stream' in body

def test_prepare_multipart_with_mime_guess_exception(monkeypatch):
    fields = {
        "file1": {
            "filename": "/bin/true",
            "mime_type": None
        }
    }

    def mock_guess_type(filename, strict):
        raise Exception("Mocked exception")

    monkeypatch.setattr(mimetypes, 'guess_type', mock_guess_type)
    content_type, body = prepare_multipart(fields)
    assert 'multipart/form-data' in content_type
    assert b'application/octet-stream' in body

def test_prepare_multipart_py2(monkeypatch):
    fields = {
        "file1": {
            "filename": "/bin/true",
            "mime_type": "application/octet-stream"
        }
    }

    monkeypatch.setattr('ansible.module_utils.six.PY3', False)
    monkeypatch.setattr('ansible.module_utils.urls.cStringIO', lambda: email.generator.BytesIO())
    content_type, body = prepare_multipart(fields)
    assert 'multipart/form-data' in content_type
    assert b'application/octet-stream' in body

def test_prepare_multipart_py2_header_parser(monkeypatch):
    fields = {
        "file1": {
            "filename": "/bin/true",
            "mime_type": "application/octet-stream"
        }
    }

    monkeypatch.setattr('ansible.module_utils.six.PY3', False)
    monkeypatch.setattr('ansible.module_utils.urls.cStringIO', lambda: email.generator.BytesIO())
    content_type, body = prepare_multipart(fields)
    assert 'multipart/form-data' in content_type
    assert b'application/octet-stream' in body
