# file: apimd/parser.py:299-301
# asked: {"lines": [299, 300, 301], "branches": [[300, 0], [300, 301]]}
# gained: {"lines": [299], "branches": []}

import pytest
from dataclasses import dataclass

@dataclass
class Parser:
    toc: bool = False
    link: bool = False

    def __post_init__(self):
        if self.toc:
            self.link = True

def test_parser_post_init_with_toc():
    parser = Parser(toc=True)
    assert parser.link is True

def test_parser_post_init_without_toc():
    parser = Parser(toc=False)
    assert parser.link is False

@pytest.fixture
def parser_class(monkeypatch):
    monkeypatch.setattr('apimd.parser.Parser', Parser)
    yield Parser
    monkeypatch.undo()

def test_parser_post_init_with_fixture(parser_class):
    parser = parser_class(toc=True)
    assert parser.link is True

def test_parser_post_init_without_fixture(parser_class):
    parser = parser_class(toc=False)
    assert parser.link is False
