# file: tornado/escape.py:395-399
# asked: {"lines": [395, 396, 397, 398, 399], "branches": [[397, 398], [397, 399]]}
# gained: {"lines": [395, 396, 397, 398, 399], "branches": [[397, 398], [397, 399]]}

import pytest
from tornado.escape import _build_unicode_map

def test_build_unicode_map():
    unicode_map = _build_unicode_map()
    assert isinstance(unicode_map, dict)
    assert 'AElig' in unicode_map
    assert unicode_map['AElig'] == chr(198)
    assert 'zwnj' in unicode_map
    assert unicode_map['zwnj'] == chr(8204)
