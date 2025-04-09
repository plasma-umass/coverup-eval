# file: thonny/roughparse.py:744-750
# asked: {"lines": [744, 748, 749, 750], "branches": []}
# gained: {"lines": [744, 748, 749, 750], "branches": []}

import pytest
from thonny.roughparse import HyperParser

@pytest.fixture
def hyperparser():
    class MockHyperParser(HyperParser):
        def __init__(self):
            self.isopener = [False, True, False]
            self.indexbracket = 1
            self.rawtext = ' "test" '
            self.bracketing = [(0, 0), (1, 1), (2, 2)]
    
    return MockHyperParser()

def test_is_in_string_true(hyperparser):
    assert hyperparser.is_in_string() == True

def test_is_in_string_false(hyperparser, monkeypatch):
    monkeypatch.setattr(hyperparser, 'isopener', [False, False, False])
    assert hyperparser.is_in_string() == False
