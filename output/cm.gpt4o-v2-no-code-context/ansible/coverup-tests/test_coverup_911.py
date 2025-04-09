# file: lib/ansible/module_utils/urls.py:1544-1654
# asked: {"lines": [1571, 1572, 1573, 1576, 1577, 1578, 1579, 1580, 1581, 1582, 1583, 1584, 1585, 1586, 1587, 1589, 1590, 1591, 1592, 1593, 1594, 1595, 1597, 1598, 1601, 1602, 1603, 1604, 1605, 1607, 1608, 1610, 1611, 1612, 1613, 1614, 1615, 1617, 1618, 1619, 1620, 1621, 1624, 1626, 1629, 1634, 1636, 1637, 1639, 1640, 1642, 1643, 1645, 1646, 1649, 1651, 1652, 1653], "branches": [[1571, 1572], [1571, 1576], [1577, 1578], [1577, 1626], [1578, 1579], [1578, 1583], [1583, 1584], [1583, 1597], [1586, 1587], [1586, 1589], [1590, 1591], [1590, 1595], [1601, 1602], [1601, 1607], [1617, 1618], [1617, 1624], [1626, 1629], [1626, 1634], [1645, 1646], [1645, 1649]]}
# gained: {"lines": [1571, 1572, 1573, 1576, 1577, 1578, 1579, 1580, 1581, 1582, 1583, 1584, 1585, 1586, 1587, 1589, 1590, 1595, 1597, 1598, 1601, 1602, 1603, 1604, 1605, 1607, 1608, 1610, 1611, 1612, 1613, 1614, 1615, 1617, 1618, 1619, 1620, 1621, 1624, 1626, 1629, 1640, 1642, 1643, 1645, 1646, 1651, 1652, 1653], "branches": [[1571, 1572], [1571, 1576], [1577, 1578], [1577, 1626], [1578, 1579], [1578, 1583], [1583, 1584], [1583, 1597], [1586, 1587], [1586, 1589], [1590, 1595], [1601, 1602], [1601, 1607], [1617, 1618], [1617, 1624], [1626, 1629], [1645, 1646]]}

import pytest
import email
import mimetypes
import os
from io import BytesIO as cStringIO
from ansible.module_utils.urls import prepare_multipart
from ansible.module_utils.six import PY3, string_types
from ansible.module_utils._text import to_bytes, to_native
from collections.abc import Mapping
import base64

def test_prepare_multipart_invalid_fields_type():
    with pytest.raises(TypeError, match="Mapping is required, cannot be type int"):
        prepare_multipart(123)

def test_prepare_multipart_string_field():
    fields = {
        "text_form_field": "value"
    }
    content_type, body = prepare_multipart(fields)
    assert "multipart/form-data" in content_type
    assert b'value' in body

def test_prepare_multipart_mapping_field_with_content():
    fields = {
        "file1": {
            "content": "text based file content",
            "filename": "fake.txt",
            "mime_type": "text/plain",
        }
    }
    content_type, body = prepare_multipart(fields)
    assert "multipart/form-data" in content_type
    assert b'text based file content' in body

def test_prepare_multipart_mapping_field_with_filename(monkeypatch):
    test_file_content = b"binary content"
    test_file_path = "/tmp/testfile.bin"

    with open(test_file_path, "wb") as f:
        f.write(test_file_content)

    fields = {
        "file1": {
            "filename": test_file_path,
            "mime_type": "application/octet-stream"
        }
    }

    content_type, body = prepare_multipart(fields)
    assert "multipart/form-data" in content_type
    encoded_content = base64.b64encode(test_file_content)
    assert encoded_content in body

    os.remove(test_file_path)

def test_prepare_multipart_mapping_field_with_invalid_value():
    fields = {
        "file1": 123
    }
    with pytest.raises(TypeError, match="value must be a string, or mapping, cannot be type int"):
        prepare_multipart(fields)

def test_prepare_multipart_mapping_field_with_missing_content_and_filename():
    fields = {
        "file1": {}
    }
    with pytest.raises(ValueError, match="at least one of filename or content must be provided"):
        prepare_multipart(fields)

def test_prepare_multipart_py2(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.six.PY3', False)
    fields = {
        "text_form_field": "value"
    }
    content_type, body = prepare_multipart(fields)
    assert "multipart/form-data" in content_type
    assert b'value' in body

def test_prepare_multipart_py3(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.six.PY3', True)
    fields = {
        "text_form_field": "value"
    }
    content_type, body = prepare_multipart(fields)
    assert "multipart/form-data" in content_type
    assert b'value' in body
