# file: thonny/roughparse.py:632-634
# asked: {"lines": [632, 633, 634], "branches": []}
# gained: {"lines": [632, 633, 634], "branches": []}

import pytest
from thonny.roughparse import RoughParser

@pytest.fixture
def rough_parser():
    parser = RoughParser(indent_width=4, tabwidth=4)
    parser.lastch = None
    return parser

def test_is_block_opener_colon(rough_parser, mocker):
    mocker.patch.object(rough_parser, '_study2', side_effect=lambda: setattr(rough_parser, 'lastch', ':'))
    assert rough_parser.is_block_opener() == True

def test_is_block_opener_not_colon(rough_parser, mocker):
    mocker.patch.object(rough_parser, '_study2', side_effect=lambda: setattr(rough_parser, 'lastch', ';'))
    assert rough_parser.is_block_opener() == False
