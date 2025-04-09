# file: docstring_parser/common.py:113-146
# asked: {"lines": [143, 144, 145, 146], "branches": [[143, 144], [143, 146], [144, 143], [144, 145]]}
# gained: {"lines": [143, 144, 145, 146], "branches": [[143, 144], [143, 146], [144, 145]]}

import pytest
from docstring_parser.common import Docstring, DocstringDeprecated

def test_docstring_deprecation():
    docstring = Docstring()
    
    # Ensure deprecation is None when no deprecated meta is present
    assert docstring.deprecation is None
    
    # Add a deprecated meta and check if it is returned
    deprecated_meta = DocstringDeprecated(args=[], version="1.0", description="This is deprecated")
    docstring.meta.append(deprecated_meta)
    
    assert docstring.deprecation is deprecated_meta

    # Clean up
    docstring.meta.remove(deprecated_meta)
    assert docstring.deprecation is None
