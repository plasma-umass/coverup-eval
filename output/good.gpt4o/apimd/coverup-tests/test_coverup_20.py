# file apimd/parser.py:46-48
# lines [48]
# branches []

import pytest
from apimd.parser import _defaults

def test_defaults_with_none():
    args = [None, None]
    result = list(_defaults(args))
    assert result == [" ", " "]

def test_defaults_with_values(mocker):
    mock_code = mocker.patch('apimd.parser.code', side_effect=lambda x: f"code({x})")
    mock_unparse = mocker.patch('apimd.parser.unparse', side_effect=lambda x: f"unparse({x})")
    
    args = ['a', 'b']
    result = list(_defaults(args))
    
    assert result == ["code(unparse(a))", "code(unparse(b))"]
    mock_code.assert_called()
    mock_unparse.assert_called()
