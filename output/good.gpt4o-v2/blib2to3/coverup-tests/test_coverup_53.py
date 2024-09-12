# file: src/blib2to3/pgen2/tokenize.py:196-212
# asked: {"lines": [196, 209, 210, 211, 212], "branches": []}
# gained: {"lines": [196, 209, 210, 211, 212], "branches": []}

import pytest
from blib2to3.pgen2.tokenize import tokenize, StopTokenizing

def test_tokenize_stop_tokenizing():
    def mock_readline():
        return ""
    
    def mock_tokeneater(*args):
        raise StopTokenizing
    
    # Ensure that the StopTokenizing exception is caught and handled
    try:
        tokenize(mock_readline, mock_tokeneater)
    except StopTokenizing:
        pytest.fail("StopTokenizing was not handled")
