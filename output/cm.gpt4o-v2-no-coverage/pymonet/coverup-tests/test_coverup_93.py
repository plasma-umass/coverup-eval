# file: pymonet/utils.py:25-34
# asked: {"lines": [25, 34], "branches": []}
# gained: {"lines": [25, 34], "branches": []}

import pytest
from pymonet.utils import identity

def test_identity():
    assert identity(5) == 5
    assert identity("test") == "test"
    assert identity([1, 2, 3]) == [1, 2, 3]
    assert identity({"key": "value"}) == {"key": "value"}
    assert identity(None) is None
