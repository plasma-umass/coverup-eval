# file: thonny/roughparse.py:744-750
# asked: {"lines": [744, 748, 749, 750], "branches": []}
# gained: {"lines": [744, 748, 749, 750], "branches": []}

import pytest
from thonny.roughparse import HyperParser

@pytest.fixture
def hyperparser():
    class MockHyperParser(HyperParser):
        def __init__(self, isopener, indexbracket, rawtext, bracketing):
            self.isopener = isopener
            self.indexbracket = indexbracket
            self.rawtext = rawtext
            self.bracketing = bracketing

    return MockHyperParser

def test_is_in_string_true(hyperparser):
    hp = hyperparser(
        isopener={0: True},
        indexbracket=0,
        rawtext='"some text"',
        bracketing={0: (0, 1)}
    )
    assert hp.is_in_string() is True

def test_is_in_string_false_not_opener(hyperparser):
    hp = hyperparser(
        isopener={0: False},
        indexbracket=0,
        rawtext='"some text"',
        bracketing={0: (0, 1)}
    )
    assert hp.is_in_string() is False

def test_is_in_string_false_not_quote(hyperparser):
    hp = hyperparser(
        isopener={0: True},
        indexbracket=0,
        rawtext='some text',
        bracketing={0: (0, 1)}
    )
    assert hp.is_in_string() is False
