# file thonny/roughparse.py:744-750
# lines [748, 749, 750]
# branches []

import pytest
from thonny.roughparse import HyperParser

@pytest.fixture
def hyperparser():
    class MockHyperParser(HyperParser):
        def __init__(self):
            self.isopener = [False, True, False]
            self.indexbracket = 1
            self.rawtext = 'print("Hello, World!")'
            self.bracketing = [(0, 5), (6, 7), (8, 9)]
    
    return MockHyperParser()

def test_is_in_string(hyperparser):
    assert hyperparser.is_in_string() == True
