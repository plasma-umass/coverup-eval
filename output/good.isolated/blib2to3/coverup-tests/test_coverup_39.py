# file src/blib2to3/pgen2/tokenize.py:225-230
# lines [225, 227, 228, 229]
# branches []

import pytest
from blib2to3.pgen2.tokenize import Untokenizer

def test_untokenizer_initialization():
    untokenizer = Untokenizer()
    assert untokenizer.tokens == []
    assert untokenizer.prev_row == 1
    assert untokenizer.prev_col == 0
