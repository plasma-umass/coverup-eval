# file: src/blib2to3/pgen2/pgen.py:80-88
# asked: {"lines": [80, 81, 82, 83, 84, 85, 87, 88], "branches": [[84, 85], [84, 88]]}
# gained: {"lines": [80, 81, 82, 83, 84, 85, 87, 88], "branches": [[84, 85], [84, 88]]}

import pytest
from blib2to3.pgen2.pgen import ParserGenerator, PgenGrammar

@pytest.fixture
def parser_generator():
    class MockParserGenerator(ParserGenerator):
        def __init__(self):
            self.first = {
                'test_name': {'label1', 'label2'}
            }

        def make_label(self, c, label):
            return hash(label)

    return MockParserGenerator()

@pytest.fixture
def pgen_grammar():
    return PgenGrammar()

def test_make_first(parser_generator, pgen_grammar):
    result = parser_generator.make_first(pgen_grammar, 'test_name')
    assert isinstance(result, dict)
    assert len(result) == 2
    assert all(isinstance(k, int) and v == 1 for k, v in result.items())
