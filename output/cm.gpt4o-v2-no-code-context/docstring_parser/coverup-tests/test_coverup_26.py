# file: docstring_parser/common.py:113-146
# asked: {"lines": [], "branches": [[144, 143]]}
# gained: {"lines": [], "branches": [[144, 143]]}

import pytest
from docstring_parser.common import Docstring, DocstringDeprecated, DocstringMeta

def test_docstring_deprecation():
    docstring = Docstring()
    
    # Ensure deprecation is None when no deprecated meta is present
    assert docstring.deprecation is None
    
    # Add a deprecated meta and ensure it is returned
    deprecated_meta = DocstringDeprecated(args=[], description="Deprecated", version="1.0")
    docstring.meta.append(deprecated_meta)
    assert docstring.deprecation is deprecated_meta
    
    # Clean up
    docstring.meta.remove(deprecated_meta)
    assert docstring.deprecation is None

def test_docstring_deprecation_with_other_meta():
    docstring = Docstring()
    
    # Add a non-deprecated meta and ensure deprecation is still None
    non_deprecated_meta = DocstringMeta(args=[], description="Some description")
    docstring.meta.append(non_deprecated_meta)
    assert docstring.deprecation is None
    
    # Add a deprecated meta and ensure it is returned
    deprecated_meta = DocstringDeprecated(args=[], description="Deprecated", version="1.0")
    docstring.meta.append(deprecated_meta)
    assert docstring.deprecation is deprecated_meta
    
    # Clean up
    docstring.meta.remove(deprecated_meta)
    docstring.meta.remove(non_deprecated_meta)
    assert docstring.deprecation is None
