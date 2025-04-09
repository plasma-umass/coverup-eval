# file: lib/ansible/utils/color.py:56-70
# asked: {"lines": [63, 64, 65, 66, 67, 68, 69, 70], "branches": [[61, 63], [63, 64], [63, 65], [65, 66], [65, 69], [69, 0], [69, 70]]}
# gained: {"lines": [63, 64, 65, 66, 67, 68, 69, 70], "branches": [[61, 63], [63, 64], [63, 65], [65, 66], [65, 69], [69, 70]]}

import pytest
from ansible.utils.color import parsecolor
from ansible import constants as C

def test_parsecolor_named_color():
    assert parsecolor('red') == C.COLOR_CODES['red']
    assert parsecolor('blue') == C.COLOR_CODES['blue']

def test_parsecolor_color_code():
    assert parsecolor('color123') == u'38;5;123'
    assert parsecolor('color0') == u'38;5;0'

def test_parsecolor_rgb():
    assert parsecolor('rgb123') == u'38;5;67'
    assert parsecolor('rgb000') == u'38;5;16'
    assert parsecolor('rgb555') == u'38;5;231'

def test_parsecolor_gray():
    assert parsecolor('gray0') == u'38;5;232'
    assert parsecolor('gray23') == u'38;5;255'

def test_parsecolor_invalid(monkeypatch):
    monkeypatch.setitem(C.COLOR_CODES, 'invalid', 'invalid_color_code')
    assert parsecolor('invalid') == 'invalid_color_code'
