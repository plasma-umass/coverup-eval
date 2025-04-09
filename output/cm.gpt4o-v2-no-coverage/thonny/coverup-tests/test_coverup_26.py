# file: thonny/roughparse.py:752-756
# asked: {"lines": [754, 755, 756], "branches": []}
# gained: {"lines": [754, 755, 756], "branches": []}

import pytest
from thonny.roughparse import HyperParser

@pytest.fixture
def hyperparser_instance():
    class MockText:
        def __init__(self, text, indent_width=4, tabwidth=4):
            self.text = text
            self.indent_width = indent_width
            self.tabwidth = tabwidth

        def index(self, index):
            return index

        def get(self, start, end):
            return self.text

    text = MockText("def foo():\n    pass\n")
    return HyperParser(text, "1.0")

def test_is_in_code_true(hyperparser_instance):
    hyperparser_instance.indexbracket = 0
    hyperparser_instance.isopener = [False]
    hyperparser_instance.rawtext = "def foo():\n    pass\n"
    hyperparser_instance.bracketing = [(0, 0)]
    assert hyperparser_instance.is_in_code() is True

def test_is_in_code_false_comment(hyperparser_instance):
    hyperparser_instance.indexbracket = 0
    hyperparser_instance.isopener = [True]
    hyperparser_instance.rawtext = "# This is a comment\n"
    hyperparser_instance.bracketing = [(0, 0)]
    assert hyperparser_instance.is_in_code() is False

def test_is_in_code_false_string(hyperparser_instance):
    hyperparser_instance.indexbracket = 0
    hyperparser_instance.isopener = [True]
    hyperparser_instance.rawtext = "\"This is a string\"\n"
    hyperparser_instance.bracketing = [(0, 0)]
    assert hyperparser_instance.is_in_code() is False

def test_is_in_code_false_char(hyperparser_instance):
    hyperparser_instance.indexbracket = 0
    hyperparser_instance.isopener = [True]
    hyperparser_instance.rawtext = "'c'\n"
    hyperparser_instance.bracketing = [(0, 0)]
    assert hyperparser_instance.is_in_code() is False
