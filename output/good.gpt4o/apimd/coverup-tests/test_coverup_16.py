# file apimd/parser.py:31-33
# lines [31, 33]
# branches []

import pytest
from apimd.parser import _m

def test_m_function():
    # Test with multiple non-empty strings
    result = _m('module', 'submodule', 'subsubmodule')
    assert result == 'module.submodule.subsubmodule'

    # Test with some empty strings
    result = _m('module', '', 'submodule')
    assert result == 'module.submodule'

    # Test with all empty strings
    result = _m('', '', '')
    assert result == ''

    # Test with a single non-empty string
    result = _m('module')
    assert result == 'module'

    # Test with a single empty string
    result = _m('')
    assert result == ''
