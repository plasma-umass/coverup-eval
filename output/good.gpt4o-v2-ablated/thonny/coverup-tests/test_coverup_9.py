# file: thonny/roughparse.py:752-756
# asked: {"lines": [754, 755, 756], "branches": []}
# gained: {"lines": [754, 755, 756], "branches": []}

import pytest
from thonny.roughparse import HyperParser

@pytest.fixture
def hyper_parser():
    class MockHyperParser(HyperParser):
        def __init__(self, isopener, indexbracket, rawtext, bracketing):
            self.isopener = isopener
            self.indexbracket = indexbracket
            self.rawtext = rawtext
            self.bracketing = bracketing

    return MockHyperParser

def test_is_in_code_true(hyper_parser):
    parser = hyper_parser([False], 0, "some code", [(0, 0)])
    assert parser.is_in_code() == True

def test_is_in_code_false_comment(hyper_parser):
    parser = hyper_parser([True], 0, "# some comment", [(0, 0)])
    assert parser.is_in_code() == False

def test_is_in_code_false_double_quote(hyper_parser):
    parser = hyper_parser([True], 0, '"some string"', [(0, 0)])
    assert parser.is_in_code() == False

def test_is_in_code_false_single_quote(hyper_parser):
    parser = hyper_parser([True], 0, "'some string'", [(0, 0)])
    assert parser.is_in_code() == False
