# file tornado/util.py:384-397
# lines [384, 385, 386, 387, 388, 395, 396, 397]
# branches ['388->395', '388->397']

import pytest
from unittest.mock import Mock
from tornado.util import ArgReplacer
from types import FunctionType, CodeType

def test_getargnames_with_cython_func(mocker):
    # Create a mock function with func_code attribute
    mock_code = Mock(spec=CodeType)
    mock_code.co_varnames = ('arg1', 'arg2', 'arg3')
    mock_code.co_argcount = 3

    mock_func = Mock(spec=FunctionType)
    mock_func.func_code = mock_code

    # Mock the ArgReplacer to bypass the __init__ arguments
    replacer = Mock(ArgReplacer)
    replacer._getargnames = ArgReplacer._getargnames.__get__(replacer, ArgReplacer)
    
    argnames = replacer._getargnames(mock_func)

    assert argnames == ('arg1', 'arg2', 'arg3')

def test_getargnames_with_typeerror():
    replacer = Mock(ArgReplacer)
    replacer._getargnames = ArgReplacer._getargnames.__get__(replacer, ArgReplacer)

    with pytest.raises(TypeError):
        replacer._getargnames(123)  # Passing a non-callable to trigger TypeError
