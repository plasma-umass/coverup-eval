# file: apimd/parser.py:564-574
# asked: {"lines": [564, 566, 567, 568, 569, 570, 571, 572, 574], "branches": [[567, 568], [567, 571], [568, 567], [568, 569], [571, 572], [571, 574]]}
# gained: {"lines": [564, 566, 567, 568, 569, 570, 571, 572, 574], "branches": [[567, 568], [567, 571], [568, 567], [568, 569], [571, 572], [571, 574]]}

import pytest
from apimd.parser import Parser
from apimd.parser import table, code

@pytest.fixture
def parser():
    return Parser()

def test_get_const_with_constants(parser, mocker):
    parser.const = {
        'test.CONST1': 'value1',
        'test.CONST2': 'value2',
        'other.CONST3': 'value3'
    }
    parser.root = {
        'test.CONST1': 'test',
        'test.CONST2': 'test',
        'other.CONST3': 'other'
    }
    mocker.patch.object(parser, 'is_public', return_value=True)
    
    result = parser._Parser__get_const('test')
    
    expected = table('Constants', 'Type', items=[
        (code('CONST1'), code('value1')),
        (code('CONST2'), code('value2'))
    ])
    
    assert result == expected

def test_get_const_without_constants(parser, mocker):
    parser.const = {
        'other.CONST3': 'value3'
    }
    parser.root = {
        'other.CONST3': 'other'
    }
    mocker.patch.object(parser, 'is_public', return_value=True)
    
    result = parser._Parser__get_const('test')
    
    assert result == ''
