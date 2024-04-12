# file src/blib2to3/pgen2/parse.py:190-203
# lines [190, 192, 194, 195, 197, 198, 199, 200, 201, 202, 203]
# branches ['192->194', '192->200', '198->199', '198->200', '201->202', '201->203']

import pytest
from blib2to3.pgen2.parse import Parser, ParseError
from blib2to3.pgen2 import token
from blib2to3.pgen2.grammar import Grammar
from typing import Optional, Text

class TestParser:
    @pytest.fixture
    def parser(self, mocker):
        grammar = Grammar()
        parser = Parser(grammar)
        parser.used_names = mocker.MagicMock()
        return parser

    def test_classify_with_name_token(self, parser):
        type = token.NAME
        value = "test_name"
        context = ("", (1, 0))
        parser.grammar.keywords = {value: 256}
        parser.grammar.tokens = {}
        label = parser.classify(type, value, context)
        assert label == 256
        parser.used_names.add.assert_called_once_with(value)

    def test_classify_with_non_name_token(self, parser):
        type = token.NUMBER
        value = "123"
        context = ("", (1, 0))
        parser.grammar.tokens = {type: 2}
        label = parser.classify(type, value, context)
        assert label == 2

    def test_classify_with_invalid_token(self, parser):
        type = token.OP
        value = "@"
        context = ("", (1, 0))
        parser.grammar.tokens = {}
        with pytest.raises(ParseError):
            parser.classify(type, value, context)
