# file: src/blib2to3/pgen2/pgen.py:136-141
# asked: {"lines": [136, 137, 138, 139, 140, 141], "branches": [[139, 0], [139, 140], [140, 139], [140, 141]]}
# gained: {"lines": [136, 137, 138, 139, 140, 141], "branches": [[139, 0], [139, 140], [140, 141]]}

import pytest
from unittest.mock import MagicMock
from blib2to3.pgen2.pgen import ParserGenerator

@pytest.fixture
def parser_generator():
    pg = ParserGenerator.__new__(ParserGenerator)
    pg.dfas = {'A': [], 'B': []}
    pg.first = {}
    pg.calcfirst = MagicMock()
    return pg

def test_addfirstsets(parser_generator):
    parser_generator.addfirstsets()
    assert parser_generator.calcfirst.call_count == 2
    assert parser_generator.calcfirst.call_args_list[0][0][0] == 'A'
    assert parser_generator.calcfirst.call_args_list[1][0][0] == 'B'
