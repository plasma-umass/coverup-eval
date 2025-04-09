# file src/blib2to3/pgen2/tokenize.py:180-181
# lines [180, 181]
# branches []

import pytest
from blib2to3.pgen2 import tokenize

def test_stop_tokenizing_exception():
    with pytest.raises(tokenize.StopTokenizing):
        raise tokenize.StopTokenizing
