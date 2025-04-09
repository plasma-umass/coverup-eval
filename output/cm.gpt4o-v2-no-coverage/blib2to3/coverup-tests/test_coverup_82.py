# file: src/blib2to3/pgen2/tokenize.py:380-399
# asked: {"lines": [398, 399], "branches": []}
# gained: {"lines": [398, 399], "branches": []}

import pytest
from blib2to3.pgen2.tokenize import untokenize
from blib2to3.pgen2.tokenize import TokenInfo
from io import StringIO
import token
import tokenize

def test_untokenize_full_input():
    source = "def foo():\n    return 42\n"
    tokens = list(tokenize.generate_tokens(StringIO(source).readline))
    untok_source = untokenize(tokens)
    assert untok_source.replace(" ", "") == source.replace(" ", "")

def test_untokenize_limited_input():
    source = "def foo():\n    return 42\n"
    tokens = [tok[:2] for tok in tokenize.generate_tokens(StringIO(source).readline)]
    newcode = untokenize(tokens)
    readline = iter(newcode.splitlines(1)).__next__
    t2 = [tok[:2] for tok in tokenize.generate_tokens(readline)]
    assert tokens == t2
