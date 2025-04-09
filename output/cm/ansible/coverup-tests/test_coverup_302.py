# file lib/ansible/plugins/shell/powershell.py:33-57
# lines [33, 39, 45, 46, 47, 48, 50, 51, 52, 54, 55, 57]
# branches ['45->46', '45->57']

import pytest
import re
from xml.etree import ElementTree as ET
from ansible.plugins.shell.powershell import _parse_clixml
from ansible.module_utils._text import to_bytes

@pytest.fixture
def mock_et_fromstring(mocker):
    return mocker.patch('xml.etree.ElementTree.fromstring', side_effect=ET.fromstring)

def test_parse_clixml_with_nested_elements(mock_et_fromstring):
    # Mock data with nested CLIXML elements
    mock_data = b'<# CLIXML\r\n<Objs Version="1.1.0.1" xmlns="http://schemas.microsoft.com/powershell/2004/04"><S S="Error">Test error message 1_x000D__x000A_</S></Objs><Objs Version="1.1.0.1" xmlns="http://schemas.microsoft.com/powershell/2004/04"><S S="Error">Test error message 2_x000D__x000A_</S></Objs>'
    
    # Call the function with the mock data
    result = _parse_clixml(mock_data, stream="Error")
    
    # Expected result after parsing
    expected_result = to_bytes('Test error message 1\r\nTest error message 2')
    
    # Assert that the result matches the expected result
    assert result == expected_result, "The parsed CLIXML error messages do not match the expected result."

    # Assert that the ElementTree.fromstring was called twice, once for each Objs element
    assert mock_et_fromstring.call_count == 2, "ElementTree.fromstring should have been called twice for the nested CLIXML elements."
