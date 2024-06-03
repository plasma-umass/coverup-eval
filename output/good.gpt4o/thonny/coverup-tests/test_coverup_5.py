# file thonny/roughparse.py:632-634
# lines [632, 633, 634]
# branches []

import pytest
from thonny.roughparse import RoughParser

class MockRoughParser(RoughParser):
    def __init__(self, lastch):
        self.lastch = lastch

    def _study2(self):
        pass

@pytest.fixture
def mock_rough_parser(mocker):
    mocker.patch.object(RoughParser, '_study2', return_value=None)
    return MockRoughParser(":")

def test_is_block_opener(mock_rough_parser):
    assert mock_rough_parser.is_block_opener() == True

@pytest.fixture
def mock_rough_parser_not_block(mocker):
    mocker.patch.object(RoughParser, '_study2', return_value=None)
    return MockRoughParser("a")

def test_is_not_block_opener(mock_rough_parser_not_block):
    assert mock_rough_parser_not_block.is_block_opener() == False
