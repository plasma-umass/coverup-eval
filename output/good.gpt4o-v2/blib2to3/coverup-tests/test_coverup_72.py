# file: src/blib2to3/pgen2/tokenize.py:380-399
# asked: {"lines": [380, 398, 399], "branches": []}
# gained: {"lines": [380, 398, 399], "branches": []}

import pytest
from blib2to3.pgen2.tokenize import untokenize, TokenInfo
from blib2to3.pgen2.token import NAME, OP, NEWLINE, ENDMARKER

def test_untokenize():
    tokens = [
        (NAME, 'def', (1, 0), (1, 3), 'def foo():\n'),
        (NAME, 'foo', (1, 4), (1, 7), 'def foo():\n'),
        (OP, '(', (1, 7), (1, 8), 'def foo():\n'),
        (OP, ')', (1, 8), (1, 9), 'def foo():\n'),
        (OP, ':', (1, 9), (1, 10), 'def foo():\n'),
        (NEWLINE, '\n', (1, 10), (1, 11), 'def foo():\n'),
        (ENDMARKER, '', (2, 0), (2, 0), '')
    ]
    
    result = untokenize(tokens)
    assert result == 'def foo():\n'

