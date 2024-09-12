# file: src/blib2to3/pgen2/pgen.py:359-363
# asked: {"lines": [359, 360, 361, 362, 363], "branches": [[361, 362], [361, 363]]}
# gained: {"lines": [359, 360, 361, 362, 363], "branches": [[361, 362], [361, 363]]}

import pytest
from blib2to3.pgen2 import tokenize
from blib2to3.pgen2.pgen import ParserGenerator
from pathlib import Path
from io import StringIO

class MockGenerator:
    def __init__(self, tokens):
        self.tokens = iter(tokens)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.tokens)

@pytest.fixture
def parser_generator(mocker):
    mock_stream = StringIO("")
    mocker.patch.object(ParserGenerator, 'parse', return_value=({}, 'mock_startsymbol'))
    mocker.patch.object(ParserGenerator, 'addfirstsets', return_value=None)
    pg = ParserGenerator(Path("mock_file"), mock_stream)
    yield pg

def test_gettoken_skips_comments_and_nl(parser_generator):
    tokens = [
        (tokenize.COMMENT, "# comment", (1, 0), (1, 9), "# comment"),
        (tokenize.NL, "\n", (1, 9), (1, 10), "\n"),
        (tokenize.NAME, "name", (2, 0), (2, 4), "name")
    ]
    parser_generator.generator = MockGenerator(tokens)
    parser_generator.gettoken()
    assert parser_generator.type == tokenize.NAME
    assert parser_generator.value == "name"
    assert parser_generator.begin == (2, 0)
    assert parser_generator.end == (2, 4)
    assert parser_generator.line == "name"

def test_gettoken_stops_at_first_non_comment_nl(parser_generator):
    tokens = [
        (tokenize.COMMENT, "# comment", (1, 0), (1, 9), "# comment"),
        (tokenize.NAME, "name", (2, 0), (2, 4), "name")
    ]
    parser_generator.generator = MockGenerator(tokens)
    parser_generator.gettoken()
    assert parser_generator.type == tokenize.NAME
    assert parser_generator.value == "name"
    assert parser_generator.begin == (2, 0)
    assert parser_generator.end == (2, 4)
    assert parser_generator.line == "name"
