# file: thonny/roughparse.py:744-750
# asked: {"lines": [744, 748, 749, 750], "branches": []}
# gained: {"lines": [744, 748, 749, 750], "branches": []}

import pytest
from thonny.roughparse import HyperParser

@pytest.fixture
def hyperparser_instance(monkeypatch):
    # Mocking the necessary attributes for the HyperParser instance
    class MockText:
        indent_width = 4
        tabwidth = 4

        def index(self, index):
            return index

        def get(self, start, end):
            return 'print("Hello, World!")'

    class MockRoughParser:
        def __init__(self, indent_width, tabwidth):
            self.indent_width = indent_width
            self.tabwidth = tabwidth
            self.str = 'print("Hello, World!") \\n'

        def set_str(self, s):
            pass

        def find_good_parse_start(self, is_char_in_string=None):
            return 0

        def set_lo(self, lo):
            pass

        def get_last_stmt_bracketing(self):
            return [(0, 0), (6, 1)]

    monkeypatch.setattr('thonny.roughparse.RoughParser', MockRoughParser)

    text = MockText()
    index = '1.0'
    hp = HyperParser(text, index)
    hp.isopener = [False, True]
    hp.rawtext = 'print("Hello, World!")'
    hp.bracketing = [(0, 0), (6, 1)]
    hp.indexbracket = 1
    return hp

def test_is_in_string_true(hyperparser_instance):
    hp = hyperparser_instance
    assert hp.is_in_string() == True

def test_is_in_string_false(hyperparser_instance):
    hp = hyperparser_instance
    hp.isopener[hp.indexbracket] = False
    assert hp.is_in_string() == False

def test_is_in_string_not_in_quotes(hyperparser_instance):
    hp = hyperparser_instance
    hp.rawtext = 'print(Hello, World!)'
    assert hp.is_in_string() == False
