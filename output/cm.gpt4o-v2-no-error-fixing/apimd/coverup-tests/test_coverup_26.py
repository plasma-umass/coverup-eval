# file: apimd/parser.py:564-574
# asked: {"lines": [566, 567, 568, 569, 570, 571, 572, 574], "branches": [[567, 568], [567, 571], [568, 567], [568, 569], [571, 572], [571, 574]]}
# gained: {"lines": [566, 567, 568, 569, 570, 571, 572, 574], "branches": [[567, 568], [567, 571], [568, 567], [568, 569], [571, 572], [571, 574]]}

import pytest
from unittest.mock import MagicMock

def test_get_const_with_constants(monkeypatch):
    from apimd.parser import Parser

    # Mocking the dependencies
    mock_code = MagicMock(side_effect=lambda x: f"code({x})")
    mock_table = MagicMock(return_value="mocked_table")
    monkeypatch.setattr("apimd.parser.code", mock_code)
    monkeypatch.setattr("apimd.parser.table", mock_table)

    # Creating a Parser instance with necessary attributes
    parser = Parser()
    parser.const = {"const1": "value1", "const2": "value2"}
    parser.root = {"const1": "name", "const2": "other_name"}
    parser.is_public = MagicMock(side_effect=lambda x: x == "const1")

    # Calling the method
    result = parser._Parser__get_const("name")

    # Assertions
    assert result == "mocked_table"
    mock_code.assert_any_call("const1")
    mock_code.assert_any_call("value1")
    mock_table.assert_called_once_with('Constants', 'Type', items=[('code(const1)', 'code(value1)')])

def test_get_const_without_constants(monkeypatch):
    from apimd.parser import Parser

    # Mocking the dependencies
    mock_code = MagicMock(side_effect=lambda x: f"code({x})")
    mock_table = MagicMock(return_value="mocked_table")
    monkeypatch.setattr("apimd.parser.code", mock_code)
    monkeypatch.setattr("apimd.parser.table", mock_table)

    # Creating a Parser instance with necessary attributes
    parser = Parser()
    parser.const = {"const1": "value1", "const2": "value2"}
    parser.root = {"const1": "other_name", "const2": "other_name"}
    parser.is_public = MagicMock(return_value=True)

    # Calling the method
    result = parser._Parser__get_const("name")

    # Assertions
    assert result == ""
    mock_code.assert_not_called()
    mock_table.assert_not_called()
