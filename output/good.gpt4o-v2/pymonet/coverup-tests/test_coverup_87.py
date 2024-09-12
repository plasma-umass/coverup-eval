# file: pymonet/utils.py:37-46
# asked: {"lines": [37, 46], "branches": []}
# gained: {"lines": [37, 46], "branches": []}

import pytest
from pymonet.utils import increase

def test_increase():
    assert increase(0) == 1
    assert increase(-1) == 0
    assert increase(100) == 101
