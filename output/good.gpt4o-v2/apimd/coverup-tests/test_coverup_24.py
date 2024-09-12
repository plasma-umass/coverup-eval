# file: apimd/parser.py:564-574
# asked: {"lines": [564, 566, 567, 568, 569, 570, 571, 572, 574], "branches": [[567, 568], [567, 571], [568, 567], [568, 569], [571, 572], [571, 574]]}
# gained: {"lines": [564, 566, 567, 568, 569, 570, 571, 572, 574], "branches": [[567, 568], [567, 571], [568, 567], [568, 569], [571, 572], [571, 574]]}

import pytest
from unittest.mock import MagicMock
from apimd.parser import Parser, code, table

def test_get_const_with_constants(monkeypatch):
    parser = Parser()
    parser.const = {'const1': 'value1', 'const2': 'value2'}
    parser.root = {'const1': 'root1', 'const2': 'root2'}
    parser.is_public = MagicMock(return_value=True)
    
    def mock_code(value):
        return f'code({value})'
    
    def mock_table(title1, title2, items):
        return f'table({title1}, {title2}, {items})'
    
    monkeypatch.setattr('apimd.parser.code', mock_code)
    monkeypatch.setattr('apimd.parser.table', mock_table)
    
    result = parser._Parser__get_const('root1')
    assert result == "table(Constants, Type, [('code(const1)', 'code(value1)')])"

def test_get_const_without_constants(monkeypatch):
    parser = Parser()
    parser.const = {'const1': 'value1', 'const2': 'value2'}
    parser.root = {'const1': 'root1', 'const2': 'root2'}
    parser.is_public = MagicMock(return_value=False)
    
    result = parser._Parser__get_const('root1')
    assert result == ""
