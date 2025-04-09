# file: thonny/roughparse.py:752-756
# asked: {"lines": [754, 755, 756], "branches": []}
# gained: {"lines": [754, 755, 756], "branches": []}

import pytest
from thonny.roughparse import HyperParser

@pytest.fixture
def hyperparser():
    class MockHyperParser(HyperParser):
        def __init__(self):
            self.isopener = [False, True, False]
            self.indexbracket = 1
            self.rawtext = "some text # comment"
            self.bracketing = [(0, 0), (10, 10), (20, 20)]
    
    return MockHyperParser()

def test_is_in_code_true(hyperparser):
    hyperparser.rawtext = "some text # comment"
    hyperparser.bracketing = [(0, 0), (10, 10), (20, 20)]
    assert hyperparser.is_in_code() == False

def test_is_in_code_false(hyperparser):
    hyperparser.rawtext = "some text"
    hyperparser.bracketing = [(0, 0), (5, 5), (10, 10)]
    assert hyperparser.is_in_code() == True
