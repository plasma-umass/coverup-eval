# file: thonny/roughparse.py:744-750
# asked: {"lines": [748, 749, 750], "branches": []}
# gained: {"lines": [748, 749, 750], "branches": []}

import pytest
from thonny.roughparse import HyperParser

@pytest.fixture
def hyperparser_instance():
    # Mocking the necessary attributes for the test
    class MockText:
        def index(self, index):
            return index

    text = MockText()
    text.indent_width = 4
    text.tabwidth = 4
    text.get = lambda start, end: "some text"
    
    hp = HyperParser(text, "1.0")
    hp.isopener = [False, True]
    hp.indexbracket = 1
    hp.rawtext = 'some "text"'
    hp.bracketing = [(0, 0), (5, 1)]
    
    return hp

def test_is_in_string(hyperparser_instance):
    hp = hyperparser_instance
    assert hp.is_in_string() == True

    # Modify the instance to test the other branch
    hp.isopener = [False, False]
    assert hp.is_in_string() == False

    hp.isopener = [False, True]
    hp.rawtext = "some text"
    assert hp.is_in_string() == False
