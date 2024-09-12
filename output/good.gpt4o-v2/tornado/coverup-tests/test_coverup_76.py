# file: tornado/escape.py:395-399
# asked: {"lines": [395, 396, 397, 398, 399], "branches": [[397, 398], [397, 399]]}
# gained: {"lines": [395, 396, 397, 398, 399], "branches": [[397, 398], [397, 399]]}

import pytest
import html.entities
from tornado.escape import _build_unicode_map

def test_build_unicode_map():
    # Call the function to ensure lines 395-399 are executed
    unicode_map = _build_unicode_map()
    
    # Verify that the unicode_map is correctly built
    assert isinstance(unicode_map, dict)
    for name, value in html.entities.name2codepoint.items():
        assert unicode_map[name] == chr(value)
