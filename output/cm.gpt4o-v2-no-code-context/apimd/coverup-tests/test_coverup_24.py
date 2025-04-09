# file: apimd/parser.py:564-574
# asked: {"lines": [564, 566, 567, 568, 569, 570, 571, 572, 574], "branches": [[567, 568], [567, 571], [568, 567], [568, 569], [571, 572], [571, 574]]}
# gained: {"lines": [564, 566, 567, 568, 569, 570, 571, 572, 574], "branches": [[567, 568], [567, 571], [568, 567], [568, 569], [571, 572], [571, 574]]}

import pytest
from unittest.mock import MagicMock

# Assuming the Parser class is imported from apimd.parser
from apimd.parser import Parser

@pytest.fixture
def parser():
    return Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={'CONST_A': 'name', 'CONST_B': 'name'}, alias={}, const={'CONST_A': 'value_A', 'CONST_B': 'value_B'})

def test_get_const_with_constants(parser, mocker):
    # Mocking the necessary attributes and methods
    parser.is_public = mocker.MagicMock(side_effect=lambda x: True)
    
    # Mocking the code and table functions
    mocker.patch('apimd.parser.code', side_effect=lambda x: f"code_{x}")
    mocker.patch('apimd.parser.table', side_effect=lambda title, type_, items: f"table_{items}")
    
    result = parser._Parser__get_const('name')
    
    assert result == "table_[('code_CONST_A', 'code_value_A'), ('code_CONST_B', 'code_value_B')]"

def test_get_const_without_constants(parser, mocker):
    # Mocking the necessary attributes and methods
    parser.root = {'CONST_A': 'other_name', 'CONST_B': 'other_name'}
    parser.is_public = mocker.MagicMock(side_effect=lambda x: True)
    
    # Mocking the code and table functions
    mocker.patch('apimd.parser.code', side_effect=lambda x: f"code_{x}")
    mocker.patch('apimd.parser.table', side_effect=lambda title, type_, items: f"table_{items}")
    
    result = parser._Parser__get_const('name')
    
    assert result == ""
