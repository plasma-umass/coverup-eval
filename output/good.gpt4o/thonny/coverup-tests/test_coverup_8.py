# file thonny/jedi_utils.py:99-120
# lines [99, 102, 103, 104, 105, 106, 107, 109, 110, 111, 112, 113, 114, 115, 116, 120]
# branches ['103->104', '103->120', '106->107', '106->109']

import pytest
from unittest.mock import Mock

# Assuming ThonnyCompletion is a class defined somewhere in thonny.jedi_utils
from thonny.jedi_utils import _tweak_completions, ThonnyCompletion

def test_tweak_completions(mocker):
    # Mocking a completion object
    mock_completion = Mock()
    mock_completion.name = "test"
    mock_completion.complete = "test="
    mock_completion.type = "type"
    mock_completion.description = "description"
    mock_completion.parent = "parent"
    mock_completion.full_name = "full_name"

    completions = [mock_completion]

    # Call the function with the mocked completions
    result = _tweak_completions(completions)

    # Assertions to verify the postconditions
    assert len(result) == 1
    assert result[0].name == "test="
    assert result[0].complete == "test="
    assert result[0].type == "type"
    assert result[0].description == "description"
    assert result[0].parent == "parent"
    assert result[0].full_name == "full_name"

    # Clean up
    mocker.stopall()
