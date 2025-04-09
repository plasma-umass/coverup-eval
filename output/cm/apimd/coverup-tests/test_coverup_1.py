# file apimd/parser.py:31-33
# lines [31, 33]
# branches []

import pytest
from apimd.parser import _m

def test__m():
    assert _m() == ''
    assert _m('apimd') == 'apimd'
    assert _m('apimd', 'parser') == 'apimd.parser'
    assert _m('', 'parser') == 'parser'
    assert _m('apimd', '') == 'apimd'
    assert _m('', '') == ''
    assert _m('apimd', '', 'parser') == 'apimd.parser'
