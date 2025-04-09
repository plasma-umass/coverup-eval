# file: apimd/parser.py:299-301
# asked: {"lines": [299, 300, 301], "branches": [[300, 0], [300, 301]]}
# gained: {"lines": [299, 300, 301], "branches": [[300, 0], [300, 301]]}

import pytest
from apimd.parser import Parser

def test_parser_post_init_with_toc():
    parser = Parser(toc=True)
    assert parser.link is True

def test_parser_post_init_without_toc():
    parser = Parser(toc=False)
    assert parser.link is True  # Default value

def test_parser_post_init_default():
    parser = Parser()
    assert parser.link is True  # Default value
