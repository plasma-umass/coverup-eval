# file apimd/parser.py:299-301
# lines [299, 300, 301]
# branches ['300->exit', '300->301']

import pytest
from apimd.parser import Parser
from dataclasses import dataclass

@dataclass
class ParserWithTOC(Parser):
    toc: bool = False
    link: bool = False  # Explicitly add the link attribute for testing

def test_parser_post_init_toc_true():
    # Setup: create a Parser instance with toc set to True
    parser = ParserWithTOC(toc=True)

    # Exercise: trigger the __post_init__ method
    parser.__post_init__()

    # Verify: check if link attribute is set to True
    assert parser.link is True

def test_parser_post_init_toc_false():
    # Setup: create a Parser instance with toc set to False
    parser = ParserWithTOC(toc=False)

    # Exercise: trigger the __post_init__ method
    parser.__post_init__()

    # Verify: check if link attribute remains False
    assert parser.link is False
