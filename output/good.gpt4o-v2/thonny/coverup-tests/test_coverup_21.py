# file: thonny/roughparse.py:752-756
# asked: {"lines": [754, 755, 756], "branches": []}
# gained: {"lines": [754, 755, 756], "branches": []}

import pytest
from thonny.roughparse import HyperParser

class MockText:
    def __init__(self, text):
        self.text = text
        self.indent_width = 4
        self.tabwidth = 4

    def index(self, index):
        return index

    def get(self, start, end):
        return self.text

@pytest.fixture
def hyperparser_instance(monkeypatch):
    text = MockText("some sample text")
    index = "1.0"
    instance = HyperParser(text, index)
    # Mocking necessary attributes for the test
    instance.isopener = [False, True]
    instance.indexbracket = 1
    instance.rawtext = [' ', '#', '"', "'"]
    instance.bracketing = [(0, 0), (1, 1)]
    yield instance

def test_is_in_code_true(hyperparser_instance):
    hyperparser_instance.isopener[hyperparser_instance.indexbracket] = False
    assert hyperparser_instance.is_in_code() is True

def test_is_in_code_false_comment(hyperparser_instance):
    hyperparser_instance.isopener[hyperparser_instance.indexbracket] = True
    hyperparser_instance.rawtext[hyperparser_instance.bracketing[hyperparser_instance.indexbracket][0]] = '#'
    assert hyperparser_instance.is_in_code() is False

def test_is_in_code_false_double_quote(hyperparser_instance):
    hyperparser_instance.isopener[hyperparser_instance.indexbracket] = True
    hyperparser_instance.rawtext[hyperparser_instance.bracketing[hyperparser_instance.indexbracket][0]] = '"'
    assert hyperparser_instance.is_in_code() is False

def test_is_in_code_false_single_quote(hyperparser_instance):
    hyperparser_instance.isopener[hyperparser_instance.indexbracket] = True
    hyperparser_instance.rawtext[hyperparser_instance.bracketing[hyperparser_instance.indexbracket][0]] = "'"
    assert hyperparser_instance.is_in_code() is False
