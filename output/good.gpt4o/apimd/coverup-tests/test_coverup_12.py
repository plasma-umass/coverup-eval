# file apimd/parser.py:74-87
# lines [74, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 87]
# branches ['76->exit', '76->77', '77->78', '77->80', '80->81', '80->87', '82->83', '82->84']

import pytest
from unittest.mock import MagicMock
from typing import List
from apimd.parser import walk_body
from ast import If, Try, stmt

def test_walk_body(mocker):
    # Mocking the stmt class
    mock_stmt = mocker.create_autospec(stmt, instance=True)
    
    # Creating mock If node
    mock_if = mocker.create_autospec(If, instance=True)
    mock_if.body = [mock_stmt]
    mock_if.orelse = [mock_stmt]
    
    # Creating mock Try node
    mock_try = mocker.create_autospec(Try, instance=True)
    mock_try.body = [mock_stmt]
    mock_try.handlers = [MagicMock(body=[mock_stmt])]
    mock_try.orelse = [mock_stmt]
    mock_try.finalbody = [mock_stmt]
    
    # Test with If node
    body: List[stmt] = [mock_if]
    result = list(walk_body(body))
    assert result == [mock_stmt, mock_stmt]
    
    # Test with Try node
    body = [mock_try]
    result = list(walk_body(body))
    assert result == [mock_stmt, mock_stmt, mock_stmt, mock_stmt]
    
    # Test with mixed If and Try nodes
    body = [mock_if, mock_try]
    result = list(walk_body(body))
    assert result == [mock_stmt, mock_stmt, mock_stmt, mock_stmt, mock_stmt, mock_stmt]

