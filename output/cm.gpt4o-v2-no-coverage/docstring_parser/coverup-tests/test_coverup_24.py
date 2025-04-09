# file: docstring_parser/common.py:113-146
# asked: {"lines": [126, 130, 131, 136, 137, 138, 139, 143, 144, 145, 146], "branches": [[136, 137], [136, 139], [137, 136], [137, 138], [143, 144], [143, 146], [144, 143], [144, 145]]}
# gained: {"lines": [126, 130, 131, 136, 137, 138, 143, 144, 145], "branches": [[136, 137], [137, 138], [143, 144], [144, 145]]}

import pytest
from docstring_parser.common import Docstring, DocstringParam, DocstringRaises, DocstringReturns, DocstringDeprecated

def test_docstring_init():
    doc = Docstring()
    assert doc.short_description is None
    assert doc.long_description is None
    assert doc.blank_after_short_description is False
    assert doc.blank_after_long_description is False
    assert doc.meta == []

def test_docstring_params():
    doc = Docstring()
    param = DocstringParam(args=[], description=None, arg_name="arg", type_name=None, is_optional=None, default=None)
    doc.meta.append(param)
    assert doc.params == [param]

def test_docstring_raises():
    doc = Docstring()
    raises = DocstringRaises(args=[], description=None, type_name=None)
    doc.meta.append(raises)
    assert doc.raises == [raises]

def test_docstring_returns():
    doc = Docstring()
    returns = DocstringReturns(args=[], description=None, type_name=None, is_generator=False)
    doc.meta.append(returns)
    assert doc.returns == returns

def test_docstring_deprecation():
    doc = Docstring()
    deprecation = DocstringDeprecated(args=[], description=None, version=None)
    doc.meta.append(deprecation)
    assert doc.deprecation == deprecation
