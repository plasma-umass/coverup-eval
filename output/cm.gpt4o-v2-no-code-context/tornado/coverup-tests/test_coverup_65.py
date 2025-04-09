# file: tornado/escape.py:395-399
# asked: {"lines": [395, 396, 397, 398, 399], "branches": [[397, 398], [397, 399]]}
# gained: {"lines": [395, 396, 397, 398, 399], "branches": [[397, 398], [397, 399]]}

import pytest
import html.entities
from tornado.escape import _build_unicode_map

def test_build_unicode_map(monkeypatch):
    # Mock the html.entities.name2codepoint to ensure full coverage
    mock_name2codepoint = {
        'quot': 34,
        'amp': 38,
        'lt': 60,
        'gt': 62
    }
    
    monkeypatch.setattr(html.entities, 'name2codepoint', mock_name2codepoint)
    
    unicode_map = _build_unicode_map()
    
    # Verify that the unicode_map is built correctly
    assert unicode_map == {
        'quot': '"',
        'amp': '&',
        'lt': '<',
        'gt': '>'
    }
