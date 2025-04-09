# file: src/blib2to3/pgen2/tokenize.py:180-181
# asked: {"lines": [180, 181], "branches": []}
# gained: {"lines": [180, 181], "branches": []}

import pytest
from blib2to3.pgen2.tokenize import StopTokenizing

def test_stop_tokenizing_exception():
    with pytest.raises(StopTokenizing):
        raise StopTokenizing("Stop tokenizing exception raised")

def test_stop_tokenizing_inheritance():
    assert issubclass(StopTokenizing, Exception)
