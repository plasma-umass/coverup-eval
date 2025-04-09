# file: lib/ansible/module_utils/urls.py:1544-1654
# asked: {"lines": [1544, 1571, 1572, 1573, 1576, 1577, 1578, 1579, 1580, 1581, 1582, 1583, 1584, 1585, 1586, 1587, 1589, 1590, 1591, 1592, 1593, 1594, 1595, 1597, 1598, 1601, 1602, 1603, 1604, 1605, 1607, 1608, 1610, 1611, 1612, 1613, 1614, 1615, 1617, 1618, 1619, 1620, 1621, 1624, 1626, 1629, 1634, 1636, 1637, 1639, 1640, 1642, 1643, 1645, 1646, 1649, 1651, 1652, 1653], "branches": [[1571, 1572], [1571, 1576], [1577, 1578], [1577, 1626], [1578, 1579], [1578, 1583], [1583, 1584], [1583, 1597], [1586, 1587], [1586, 1589], [1590, 1591], [1590, 1595], [1601, 1602], [1601, 1607], [1617, 1618], [1617, 1624], [1626, 1629], [1626, 1634], [1645, 1646], [1645, 1649]]}
# gained: {"lines": [1544, 1571, 1572, 1573, 1576, 1577, 1578, 1579, 1580, 1581, 1582, 1583, 1584, 1585, 1586, 1587, 1589, 1590, 1595, 1597, 1598, 1601, 1602, 1603, 1604, 1605, 1607, 1608, 1610, 1611, 1612, 1613, 1614, 1615, 1617, 1618, 1619, 1620, 1621, 1624, 1626, 1629, 1640, 1642, 1643, 1645, 1646, 1651, 1652, 1653], "branches": [[1571, 1572], [1571, 1576], [1577, 1578], [1577, 1626], [1578, 1579], [1578, 1583], [1583, 1584], [1583, 1597], [1586, 1587], [1586, 1589], [1590, 1595], [1601, 1602], [1601, 1607], [1617, 1618], [1617, 1624], [1626, 1629], [1645, 1646]]}

import pytest
import email.mime.multipart
import mimetypes
import os
from ansible.module_utils.common.collections import Mapping
from ansible.module_utils.six import PY3, string_types
from ansible.module_utils.six.moves import cStringIO
from ansible.module_utils._text import to_bytes, to_native
from ansible.module_utils.urls import prepare_multipart
import base64

class MockMapping(Mapping):
    def __init__(self, data):
        self._data = data

    def __getitem__(self, key):
        return self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def items(self):
        return self._data.items()

def test_prepare_multipart_with_string_field():
    fields = MockMapping({"text_form_field": "value"})
    content_type, body = prepare_multipart(fields)
    assert "multipart/form-data" in content_type
    assert b'value' in body

def test_prepare_multipart_with_file_content(monkeypatch):
    fields = MockMapping({
        "file1": {
            "content": "text based file content",
            "filename": "fake.txt",
            "mime_type": "text/plain",
        }
    })
    content_type, body = prepare_multipart(fields)
    assert "multipart/form-data" in content_type
    assert b'text based file content' in body

def test_prepare_multipart_with_file(monkeypatch, tmp_path):
    test_file = tmp_path / "testfile.txt"
    test_file.write_text("file content")
    fields = MockMapping({
        "file1": {
            "filename": str(test_file),
            "mime_type": "text/plain"
        }
    })
    content_type, body = prepare_multipart(fields)
    assert "multipart/form-data" in content_type
    assert base64.b64encode(b'file content') in body

def test_prepare_multipart_with_invalid_fields():
    with pytest.raises(TypeError):
        prepare_multipart(["not", "a", "mapping"])

def test_prepare_multipart_with_invalid_value_type():
    fields = MockMapping({"field": 123})
    with pytest.raises(TypeError):
        prepare_multipart(fields)

def test_prepare_multipart_with_missing_filename_and_content():
    fields = MockMapping({"file1": {}})
    with pytest.raises(ValueError):
        prepare_multipart(fields)
