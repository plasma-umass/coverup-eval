# file src/blib2to3/pgen2/pgen.py:359-363
# lines [362]
# branches ['361->362']

import pytest
from blib2to3.pgen2 import pgen
from blib2to3.pgen2 import tokenize

# Mock input to simulate the token stream
def mock_generator():
    yield (tokenize.COMMENT, "# Comment", (1, 0), (1, 9), "# Comment\n")
    yield (tokenize.NL, "\n", (2, 0), (2, 1), "\n")
    yield (tokenize.NAME, "name", (3, 0), (3, 4), "name")

@pytest.fixture
def parser_generator(mocker):
    mocker.patch.object(pgen.ParserGenerator, '__init__', return_value=None)
    pg = pgen.ParserGenerator()
    pg.generator = mock_generator()
    return pg

def test_gettoken_skips_comments_and_newlines(parser_generator):
    parser_generator.gettoken()
    assert parser_generator.type == tokenize.NAME
    assert parser_generator.value == "name"
    assert parser_generator.begin == (3, 0)
    assert parser_generator.end == (3, 4)
    assert parser_generator.line == "name"
