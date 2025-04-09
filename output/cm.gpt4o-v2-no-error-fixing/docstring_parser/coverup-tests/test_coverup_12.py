# file: docstring_parser/common.py:113-146
# asked: {"lines": [113, 114, 116, 118, 119, 120, 121, 122, 124, 125, 126, 128, 129, 130, 131, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 146], "branches": [[136, 137], [136, 139], [137, 136], [137, 138], [143, 144], [143, 146], [144, 143], [144, 145]]}
# gained: {"lines": [113, 114, 116, 118, 119, 120, 121, 122, 124, 125, 126, 128, 129, 130, 131, 134, 135, 136, 137, 138, 141, 142, 143, 144, 145], "branches": [[136, 137], [137, 138], [143, 144], [144, 145]]}

import pytest
from docstring_parser.common import Docstring, DocstringParam, DocstringRaises, DocstringReturns, DocstringDeprecated

def test_docstring_initialization():
    doc = Docstring()
    assert doc.short_description is None
    assert doc.long_description is None
    assert doc.blank_after_short_description is False
    assert doc.blank_after_long_description is False
    assert doc.meta == []

def test_docstring_params():
    doc = Docstring()
    param = DocstringParam(args=["param"], description="A parameter", arg_name="param1", type_name="str", is_optional=False, default=None)
    doc.meta.append(param)
    assert doc.params == [param]

def test_docstring_raises():
    doc = Docstring()
    raises = DocstringRaises(args=["raises"], description="An exception", type_name="ValueError")
    doc.meta.append(raises)
    assert doc.raises == [raises]

def test_docstring_returns():
    doc = Docstring()
    returns = DocstringReturns(args=["returns"], description="A return value", type_name="str", is_generator=False)
    doc.meta.append(returns)
    assert doc.returns == returns

def test_docstring_deprecation():
    doc = Docstring()
    deprecation = DocstringDeprecated(args=["deprecated"], description="Deprecated", version="1.0.0")
    doc.meta.append(deprecation)
    assert doc.deprecation == deprecation
