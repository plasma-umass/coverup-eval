# file: lib/ansible/utils/color.py:56-70
# asked: {"lines": [56, 58, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], "branches": [[61, 62], [61, 63], [63, 64], [63, 65], [65, 66], [65, 69], [69, 0], [69, 70]]}
# gained: {"lines": [56, 58, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], "branches": [[61, 62], [61, 63], [63, 64], [63, 65], [65, 66], [65, 69], [69, 70]]}

import pytest
from ansible.utils.color import parsecolor
from ansible import constants as C

def test_parsecolor_named_color(monkeypatch):
    monkeypatch.setattr(C, 'COLOR_CODES', {'red': '31'})
    assert parsecolor('red') == '31'

def test_parsecolor_color_code():
    assert parsecolor('color123') == '38;5;123'

def test_parsecolor_rgb_code():
    assert parsecolor('rgb123') == '38;5;67'

def test_parsecolor_gray_code():
    assert parsecolor('gray10') == '38;5;242'

def test_parsecolor_invalid_color(monkeypatch):
    monkeypatch.setattr(C, 'COLOR_CODES', {'invalid': 'invalid_code'})
    assert parsecolor('invalid') == 'invalid_code'
