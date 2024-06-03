# file thonny/roughparse.py:752-756
# lines [754, 755, 756]
# branches []

import pytest
from thonny.roughparse import HyperParser

@pytest.fixture
def hyper_parser():
    class MockHyperParser(HyperParser):
        def __init__(self):
            self.isopener = [False, True, False]
            self.indexbracket = 1
            self.rawtext = [' ', '#', ' ']
            self.bracketing = [(0, 0), (1, 1), (2, 2)]
    
    return MockHyperParser()

def test_is_in_code(hyper_parser):
    assert not hyper_parser.is_in_code()
    
    hyper_parser.rawtext[1] = 'a'
    assert hyper_parser.is_in_code()
