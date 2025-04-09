# file lib/ansible/plugins/shell/powershell.py:33-57
# lines [39, 45, 46, 47, 48, 50, 51, 52, 54, 55, 57]
# branches ['45->46', '45->57']

import pytest
import xml.etree.ElementTree as ET
import re
from ansible.plugins.shell.powershell import _parse_clixml

def test_parse_clixml_with_nested_elements():
    # This is a sample CLIXML data with nested <Objs> elements
    data = b'#< CLIXML\r\n<Objs Version="1.1.0.1" xmlns="http://schemas.microsoft.com/powershell/2004/04"><S S="Error">Error message 1_x000D__x000A_</S></Objs><Objs Version="1.1.0.1" xmlns="http://schemas.microsoft.com/powershell/2004/04"><S S="Error">Error message 2_x000D__x000A_</S></Objs>'
    
    result = _parse_clixml(data, stream="Error")
    
    # Verify that the result contains the expected error messages
    assert result == b'Error message 1\r\nError message 2'

@pytest.fixture(autouse=True)
def cleanup():
    # Cleanup code if necessary
    yield
    # Add any necessary cleanup code here

