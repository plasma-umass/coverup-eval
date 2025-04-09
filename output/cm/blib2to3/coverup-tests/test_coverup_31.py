# file src/blib2to3/pgen2/tokenize.py:231-234
# lines [231, 232, 233, 234]
# branches []

import pytest
from blib2to3.pgen2.tokenize import Untokenizer

def test_untokenizer_initialization():
    untokenizer = Untokenizer()
    assert untokenizer.tokens == []
    assert untokenizer.prev_row == 1
    assert untokenizer.prev_col == 0
