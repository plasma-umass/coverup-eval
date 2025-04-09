# file: lib/ansible/utils/color.py:56-70
# asked: {"lines": [56, 58, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], "branches": [[61, 62], [61, 63], [63, 64], [63, 65], [65, 66], [65, 69], [69, 0], [69, 70]]}
# gained: {"lines": [56, 58, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], "branches": [[61, 62], [61, 63], [63, 64], [63, 65], [65, 66], [65, 69], [69, 70]]}

import pytest
import re
from ansible.utils.color import parsecolor

class C:
    COLOR_CODES = {
        'red': '31',
        'green': '32',
        'blue': '34',
    }

@pytest.fixture(autouse=True)
def setup(monkeypatch):
    monkeypatch.setattr('ansible.utils.color.C', C)

def test_parsecolor_named_color():
    assert parsecolor('red') == '31'
    assert parsecolor('green') == '32'
    assert parsecolor('blue') == '34'

def test_parsecolor_color_number():
    assert parsecolor('color123') == '38;5;123'

def test_parsecolor_rgb():
    assert parsecolor('rgb123') == '38;5;67'  # 16 + 36*1 + 6*2 + 3 = 67

def test_parsecolor_gray():
    assert parsecolor('gray5') == '38;5;237'  # 232 + 5 = 237

def test_parsecolor_no_match():
    with pytest.raises(KeyError):
        parsecolor('unknown_color')
