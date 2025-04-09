# file lib/ansible/utils/color.py:56-70
# lines [56, 58, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]
# branches ['61->62', '61->63', '63->64', '63->65', '65->66', '65->69', '69->exit', '69->70']

import pytest
import re
from ansible.utils.color import parsecolor

def test_parsecolor(mocker):
    # Mock the COLOR_CODES dictionary
    mock_color_codes = {
        'red': '31',
        'green': '32',
        'blue': '34'
    }
    mocker.patch('ansible.utils.color.C.COLOR_CODES', mock_color_codes)

    # Test for named color
    assert parsecolor('red') == '31'
    assert parsecolor('green') == '32'
    assert parsecolor('blue') == '34'

    # Test for colorNNN
    assert parsecolor('color123') == '38;5;123'

    # Test for rgbXYZ
    assert parsecolor('rgb123') == '38;5;67'  # 16 + 36*1 + 6*2 + 3 = 67

    # Test for grayNNN
    assert parsecolor('gray5') == '38;5;237'  # 232 + 5 = 237

    # Test for invalid color
    with pytest.raises(KeyError):
        parsecolor('invalidcolor')
