# file: thonny/jedi_utils.py:10-16
# asked: {"lines": [10, 11, 13, 14, 16], "branches": []}
# gained: {"lines": [10, 11, 13, 14, 16], "branches": []}

import pytest
import jedi.parser_utils
from thonny.jedi_utils import get_statement_of_position

def test_get_statement_of_position_with_jedi_parser_utils(monkeypatch):
    # Mock the function in jedi.parser_utils to ensure it is called
    def mock_get_statement_of_position(node, pos):
        return "mocked_result"
    
    # Ensure the function exists in jedi.parser_utils for the test
    monkeypatch.setattr(jedi.parser_utils, "get_statement_of_position", mock_get_statement_of_position, raising=False)
    
    node = "test_node"
    pos = "test_pos"
    
    result = get_statement_of_position(node, pos)
    
    assert result == "mocked_result"

def test_get_statement_of_position_without_jedi_parser_utils(monkeypatch):
    # Remove the function from jedi.parser_utils to ensure the fallback is used
    monkeypatch.delattr(jedi.parser_utils, "get_statement_of_position", raising=False)
    
    def _copy_of_get_statement_of_position(node, pos):
        return "fallback_result"
    
    # Inject the fallback function into the module
    monkeypatch.setattr("thonny.jedi_utils._copy_of_get_statement_of_position", _copy_of_get_statement_of_position)
    
    node = "test_node"
    pos = "test_pos"
    
    result = get_statement_of_position(node, pos)
    
    assert result == "fallback_result"
