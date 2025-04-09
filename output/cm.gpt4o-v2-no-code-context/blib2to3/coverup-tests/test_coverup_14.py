# file: src/blib2to3/pgen2/pgen.py:136-141
# asked: {"lines": [136, 137, 138, 139, 140, 141], "branches": [[139, 0], [139, 140], [140, 139], [140, 141]]}
# gained: {"lines": [136, 137, 138, 139, 140, 141], "branches": [[139, 0], [139, 140], [140, 141]]}

import pytest
from blib2to3.pgen2.pgen import ParserGenerator

class MockParserGenerator(ParserGenerator):
    def __init__(self):
        self.dfas = {'A': None, 'B': None}
        self.first = {}

    def calcfirst(self, name):
        self.first[name] = True

@pytest.fixture
def parser_generator():
    return MockParserGenerator()

def test_addfirstsets(parser_generator):
    parser_generator.addfirstsets()
    assert 'A' in parser_generator.first
    assert 'B' in parser_generator.first
