# file src/blib2to3/pgen2/parse.py:190-203
# lines []
# branches ['198->200']

import pytest
from blib2to3.pgen2 import token
from blib2to3.pgen2.parse import Parser, ParseError
from blib2to3.pgen2.grammar import Grammar
from typing import Optional, Text

class TestParser:
    @pytest.fixture
    def parser(self, mocker):
        grammar = Grammar()
        mocker.patch.object(grammar, 'keywords', {})
        mocker.patch.object(grammar, 'tokens', { token.NAME: 1, token.NUMBER: 2 })
        parser = Parser(grammar)
        parser.used_names = set()
        return parser

    def test_classify_with_keyword(self, parser):
        # This test is designed to cover the branch 198->200
        type = token.NAME
        value = 'if'
        context = ('', 0, 0)
        parser.grammar.keywords[value] = 256  # Manually add a keyword to trigger branch 198->200
        ilabel = parser.classify(type, value, context)
        assert ilabel == 256
        assert value in parser.used_names

    def test_classify_with_non_keyword_name(self, parser):
        # This test is designed to cover the branch 198->200
        type = token.NAME
        value = 'non_keyword'
        context = ('', 0, 0)
        ilabel = parser.classify(type, value, context)
        assert ilabel == 1
        assert value in parser.used_names

    def test_classify_with_non_keyword_number(self, parser):
        # This test is designed to cover the branch 198->200
        type = token.NUMBER
        value = '123'
        context = ('', 0, 0)
        ilabel = parser.classify(type, value, context)
        assert ilabel == 2
        assert value not in parser.used_names

    def test_classify_with_bad_token(self, parser):
        # This test will raise an exception for an undefined token type
        type = token.OP
        value = '+'
        context = ('', 0, 0)
        with pytest.raises(ParseError):
            parser.classify(type, value, context)
