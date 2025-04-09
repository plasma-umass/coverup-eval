# file: docstring_parser/common.py:113-146
# asked: {"lines": [139, 146], "branches": [[136, 139], [137, 136], [143, 146], [144, 143]]}
# gained: {"lines": [139, 146], "branches": [[136, 139], [143, 146]]}

import pytest
from docstring_parser.common import Docstring, DocstringReturns, DocstringDeprecated

def test_docstring_returns():
    doc = Docstring()
    assert doc.returns is None  # Test when meta is empty

    returns_meta = DocstringReturns(args=[], description="desc", type_name="type", is_generator=False)
    doc.meta.append(returns_meta)
    assert doc.returns is returns_meta  # Test when DocstringReturns is in meta

def test_docstring_deprecation():
    doc = Docstring()
    assert doc.deprecation is None  # Test when meta is empty

    deprecation_meta = DocstringDeprecated(args=[], description="desc", version="1.0")
    doc.meta.append(deprecation_meta)
    assert doc.deprecation is deprecation_meta  # Test when DocstringDeprecated is in meta
