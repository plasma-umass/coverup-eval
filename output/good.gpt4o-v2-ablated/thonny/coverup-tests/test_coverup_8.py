# file: thonny/jedi_utils.py:99-120
# asked: {"lines": [99, 102, 103, 104, 105, 106, 107, 109, 110, 111, 112, 113, 114, 115, 116, 120], "branches": [[103, 104], [103, 120], [106, 107], [106, 109]]}
# gained: {"lines": [99, 102, 103, 104, 105, 106, 107, 109, 110, 111, 112, 113, 114, 115, 116, 120], "branches": [[103, 104], [103, 120], [106, 107], [106, 109]]}

import pytest
from unittest.mock import Mock

# Assuming ThonnyCompletion is defined somewhere in the thonny/jedi_utils.py
from thonny.jedi_utils import ThonnyCompletion, _tweak_completions

def test_tweak_completions_no_trailing_equals():
    mock_completion = Mock()
    mock_completion.name = "test"
    mock_completion.complete = "test"
    mock_completion.type = "type"
    mock_completion.description = "description"
    mock_completion.parent = "parent"
    mock_completion.full_name = "full_name"
    
    completions = [mock_completion]
    result = _tweak_completions(completions)
    
    assert len(result) == 1
    assert result[0].name == "test"
    assert result[0].complete == "test"
    assert result[0].type == "type"
    assert result[0].description == "description"
    assert result[0].parent == "parent"
    assert result[0].full_name == "full_name"

def test_tweak_completions_with_trailing_equals():
    mock_completion = Mock()
    mock_completion.name = "test"
    mock_completion.complete = "test="
    mock_completion.type = "type"
    mock_completion.description = "description"
    mock_completion.parent = "parent"
    mock_completion.full_name = "full_name"
    
    completions = [mock_completion]
    result = _tweak_completions(completions)
    
    assert len(result) == 1
    assert result[0].name == "test="
    assert result[0].complete == "test="
    assert result[0].type == "type"
    assert result[0].description == "description"
    assert result[0].parent == "parent"
    assert result[0].full_name == "full_name"

def test_tweak_completions_name_already_has_trailing_equals():
    mock_completion = Mock()
    mock_completion.name = "test="
    mock_completion.complete = "test="
    mock_completion.type = "type"
    mock_completion.description = "description"
    mock_completion.parent = "parent"
    mock_completion.full_name = "full_name"
    
    completions = [mock_completion]
    result = _tweak_completions(completions)
    
    assert len(result) == 1
    assert result[0].name == "test="
    assert result[0].complete == "test="
    assert result[0].type == "type"
    assert result[0].description == "description"
    assert result[0].parent == "parent"
    assert result[0].full_name == "full_name"
