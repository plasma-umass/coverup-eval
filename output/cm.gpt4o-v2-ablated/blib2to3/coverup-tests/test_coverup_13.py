# file: src/blib2to3/pgen2/tokenize.py:231-234
# asked: {"lines": [231, 232, 233, 234], "branches": []}
# gained: {"lines": [231, 232, 233, 234], "branches": []}

import pytest
from blib2to3.pgen2.tokenize import Untokenizer

@pytest.fixture
def untokenizer():
    return Untokenizer()

def test_untokenizer_initial_state(untokenizer):
    assert untokenizer.tokens == []
    assert untokenizer.prev_row == 1
    assert untokenizer.prev_col == 0
