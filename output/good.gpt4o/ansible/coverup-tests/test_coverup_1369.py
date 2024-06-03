# file lib/ansible/module_utils/urls.py:1544-1654
# lines [1571, 1572, 1573, 1576, 1577, 1578, 1579, 1580, 1581, 1582, 1583, 1584, 1585, 1586, 1587, 1589, 1590, 1591, 1592, 1593, 1594, 1595, 1597, 1598, 1601, 1602, 1603, 1604, 1605, 1607, 1608, 1610, 1611, 1612, 1613, 1614, 1615, 1617, 1618, 1619, 1620, 1621, 1624, 1626, 1629, 1634, 1636, 1637, 1639, 1640, 1642, 1643, 1645, 1646, 1649, 1651, 1652, 1653]
# branches ['1571->1572', '1571->1576', '1577->1578', '1577->1626', '1578->1579', '1578->1583', '1583->1584', '1583->1597', '1586->1587', '1586->1589', '1590->1591', '1590->1595', '1601->1602', '1601->1607', '1617->1618', '1617->1624', '1626->1629', '1626->1634', '1645->1646', '1645->1649']

import pytest
from ansible.module_utils.urls import prepare_multipart
from collections.abc import Mapping
import base64

def test_prepare_multipart_invalid_fields():
    with pytest.raises(TypeError, match="Mapping is required, cannot be type"):
        prepare_multipart("not a mapping")

def test_prepare_multipart_invalid_value_type():
    with pytest.raises(TypeError, match="value must be a string, or mapping, cannot be type"):
        prepare_multipart({"field": 123})

def test_prepare_multipart_missing_filename_and_content():
    with pytest.raises(ValueError, match="at least one of filename or content must be provided"):
        prepare_multipart({"field": {"mime_type": "text/plain"}})

def test_prepare_multipart_with_file_content(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("file content")

    fields = {
        "file1": {
            "filename": str(test_file),
            "mime_type": "text/plain"
        },
        "text_field": "text value"
    }

    content_type, body = prepare_multipart(fields)
    assert "multipart/form-data" in content_type
    assert base64.b64encode(b"file content") in body
    assert b"text value" in body

def test_prepare_multipart_with_content_only():
    fields = {
        "file1": {
            "content": "file content",
            "mime_type": "text/plain"
        },
        "text_field": "text value"
    }

    content_type, body = prepare_multipart(fields)
    assert "multipart/form-data" in content_type
    assert b"file content" in body
    assert b"text value" in body
