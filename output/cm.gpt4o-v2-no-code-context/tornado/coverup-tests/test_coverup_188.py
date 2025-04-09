# file: tornado/util.py:211-215
# asked: {"lines": [212, 213, 214, 215], "branches": [[213, 214], [213, 215]]}
# gained: {"lines": [212, 213, 214, 215], "branches": [[213, 214], [213, 215]]}

import pytest
import re
from tornado.util import _re_unescape_replacement

_alphanum = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

def test_re_unescape_replacement_alphanum():
    match = re.match(r'\\(.)', r'\a')
    with pytest.raises(ValueError, match=r"cannot unescape '\\\\a'"):
        _re_unescape_replacement(match)

def test_re_unescape_replacement_non_alphanum():
    match = re.match(r'\\(.)', r'\*')
    result = _re_unescape_replacement(match)
    assert result == '*'
