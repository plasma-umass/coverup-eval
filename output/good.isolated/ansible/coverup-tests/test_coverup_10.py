# file lib/ansible/module_utils/urls.py:1544-1654
# lines [1544, 1571, 1572, 1573, 1576, 1577, 1578, 1579, 1580, 1581, 1582, 1583, 1584, 1585, 1586, 1587, 1589, 1590, 1591, 1592, 1593, 1594, 1595, 1597, 1598, 1601, 1602, 1603, 1604, 1605, 1607, 1608, 1610, 1611, 1612, 1613, 1614, 1615, 1617, 1618, 1619, 1620, 1621, 1624, 1626, 1629, 1634, 1636, 1637, 1639, 1640, 1642, 1643, 1645, 1646, 1649, 1651, 1652, 1653]
# branches ['1571->1572', '1571->1576', '1577->1578', '1577->1626', '1578->1579', '1578->1583', '1583->1584', '1583->1597', '1586->1587', '1586->1589', '1590->1591', '1590->1595', '1601->1602', '1601->1607', '1617->1618', '1617->1624', '1626->1629', '1626->1634', '1645->1646', '1645->1649']

import pytest
from ansible.module_utils.urls import prepare_multipart
from collections.abc import Mapping
import os
import tempfile
import base64

@pytest.fixture
def cleanup_files():
    files_to_remove = []
    yield files_to_remove
    for file in files_to_remove:
        os.remove(file)

def test_prepare_multipart_with_file_content(cleanup_files):
    # Create a temporary file to test file content handling
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(b'file content')
        tmp_file_name = tmp_file.name
        cleanup_files.append(tmp_file_name)

    fields = {
        "file1": {
            "filename": tmp_file_name,
            "mime_type": "application/octet-stream"
        },
        "text_form_field": "value"
    }

    content_type, body = prepare_multipart(fields)

    assert isinstance(content_type, str)
    # Since the file content is base64 encoded, we need to check for the encoded string
    encoded_file_content = base64.b64encode(b'file content')
    assert encoded_file_content in body
    assert b'Content-Disposition: form-data; name="file1"; filename="' in body
    assert b'Content-Disposition: form-data; name="text_form_field"' in body
    assert b'Content-Type: application/octet-stream' in body
