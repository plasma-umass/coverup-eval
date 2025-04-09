# file src/blib2to3/pgen2/tokenize.py:380-399
# lines [380, 398, 399]
# branches []

import pytest
from blib2to3.pgen2.tokenize import untokenize
from blib2to3.pgen2 import token
from collections import namedtuple

TokenInfo = namedtuple('TokenInfo', ['type', 'string', 'start', 'end', 'line'])

def test_untokenize():
    # Prepare a simple token stream that includes different token types
    tokens = [
        TokenInfo(token.NAME, 'def', (1, 0), (1, 3), 'def foo():\n'),
        TokenInfo(token.NAME, 'foo', (1, 4), (1, 7), 'def foo():\n'),
        TokenInfo(token.OP, '(', (1, 7), (1, 8), 'def foo():\n'),
        TokenInfo(token.OP, ')', (1, 8), (1, 9), 'def foo():\n'),
        TokenInfo(token.OP, ':', (1, 9), (1, 10), 'def foo():\n'),
        TokenInfo(token.NEWLINE, '\n', (1, 10), (1, 11), 'def foo():\n'),
        TokenInfo(token.INDENT, '    ', (2, 0), (2, 4), '    pass\n'),
        TokenInfo(token.NAME, 'pass', (2, 4), (2, 8), '    pass\n'),
        TokenInfo(token.NEWLINE, '\n', (2, 8), (2, 9), '    pass\n'),
        TokenInfo(token.DEDENT, '', (3, 0), (3, 0), ''),
        TokenInfo(token.ENDMARKER, '', (3, 0), (3, 0), ''),
    ]

    # Use untokenize to convert the tokens back to source code
    source_code = untokenize(tokens)

    # Verify that the untokenized source code matches the expected output
    expected_code = 'def foo():\n    pass\n'
    assert source_code == expected_code
