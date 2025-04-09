# file: lib/ansible/plugins/shell/powershell.py:33-57
# asked: {"lines": [33, 39, 45, 46, 47, 48, 50, 51, 52, 54, 55, 57], "branches": [[45, 46], [45, 57]]}
# gained: {"lines": [33, 39, 45, 46, 47, 48, 50, 51, 52, 54, 55, 57], "branches": [[45, 46], [45, 57]]}

import pytest
import re
import xml.etree.ElementTree as ET
from ansible.module_utils._text import to_bytes
from ansible.plugins.shell.powershell import _parse_clixml

def test_parse_clixml_single_obj():
    data = b'#< CLIXML\r\n<Objs Version="1.1.0.1" xmlns="http://schemas.microsoft.com/powershell/2004/04"><S S="Error">Error message_x000D__x000A_</S></Objs>'
    result = _parse_clixml(data)
    assert result == to_bytes('Error message')

def test_parse_clixml_multiple_objs():
    data = b'#< CLIXML\r\n<Objs Version="1.1.0.1" xmlns="http://schemas.microsoft.com/powershell/2004/04"><S S="Error">First error_x000D__x000A_</S></Objs><Objs Version="1.1.0.1" xmlns="http://schemas.microsoft.com/powershell/2004/04"><S S="Error">Second error_x000D__x000A_</S></Objs>'
    result = _parse_clixml(data)
    assert result == to_bytes('First error\r\nSecond error')

def test_parse_clixml_no_error_stream():
    data = b'#< CLIXML\r\n<Objs Version="1.1.0.1" xmlns="http://schemas.microsoft.com/powershell/2004/04"><S S="Output">Output message_x000D__x000A_</S></Objs>'
    result = _parse_clixml(data)
    assert result == to_bytes('')

def test_parse_clixml_empty_data():
    data = b''
    result = _parse_clixml(data)
    assert result == to_bytes('')

def test_parse_clixml_invalid_xml():
    data = b'#< CLIXML\r\n<Objs Version="1.1.0.1" xmlns="http://schemas.microsoft.com/powershell/2004/04"><S S="Error">Error message'
    with pytest.raises(ET.ParseError):
        _parse_clixml(data)
