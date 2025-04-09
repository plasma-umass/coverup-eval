# file tornado/escape.py:395-399
# lines [395, 396, 397, 398, 399]
# branches ['397->398', '397->399']

import pytest
from tornado.escape import _build_unicode_map

def test_build_unicode_map():
    unicode_map = _build_unicode_map()
    # Check if the function returns a dictionary
    assert isinstance(unicode_map, dict)
    # Check if some known entities are in the map
    assert 'amp' in unicode_map  # &amp;
    assert unicode_map['amp'] == '&'
    assert 'gt' in unicode_map  # &gt;
    assert unicode_map['gt'] == '>'
    assert 'lt' in unicode_map  # &lt;
    assert unicode_map['lt'] == '<'
    # Check if the map is not empty
    assert len(unicode_map) > 0
