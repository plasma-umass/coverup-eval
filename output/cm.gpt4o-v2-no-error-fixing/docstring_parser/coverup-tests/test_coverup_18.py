# file: docstring_parser/common.py:113-146
# asked: {"lines": [], "branches": [[137, 136], [144, 143]]}
# gained: {"lines": [], "branches": [[137, 136], [144, 143]]}

import pytest
from docstring_parser.common import Docstring, DocstringReturns, DocstringDeprecated

def test_docstring_returns():
    doc = Docstring()
    returns_meta = DocstringReturns(args=[], description="Return description", type_name="str", is_generator=False)
    doc.meta.append(returns_meta)
    
    assert doc.returns is returns_meta

    # Test branch 137->136
    doc.meta.insert(0, "NotADocstringReturns")
    assert doc.returns is returns_meta

def test_docstring_deprecation():
    doc = Docstring()
    deprecation_meta = DocstringDeprecated(args=[], description="Deprecated description", version="1.0.0")
    doc.meta.append(deprecation_meta)
    
    assert doc.deprecation is deprecation_meta

    # Test branch 144->143
    doc.meta.insert(0, "NotADocstringDeprecated")
    assert doc.deprecation is deprecation_meta
