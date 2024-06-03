# file thonny/jedi_utils.py:99-120
# lines []
# branches ['106->109']

import pytest
from unittest.mock import Mock

# Assuming ThonnyCompletion is a class defined somewhere in thonny.jedi_utils
from thonny.jedi_utils import ThonnyCompletion, _tweak_completions

def test_tweak_completions_with_equals(mocker):
    # Mocking a completion object with the necessary attributes
    completion_mock = Mock()
    completion_mock.name = "test"
    completion_mock.complete = "test="
    completion_mock.type = "type"
    completion_mock.description = "description"
    completion_mock.parent = "parent"
    completion_mock.full_name = "full_name"

    completions = [completion_mock]

    # Call the function with the mocked completions
    result = _tweak_completions(completions)

    # Verify the result
    assert len(result) == 1
    assert result[0].name == "test="
    assert result[0].complete == "test="
    assert result[0].type == "type"
    assert result[0].description == "description"
    assert result[0].parent == "parent"
    assert result[0].full_name == "full_name"

    # Clean up
    mocker.stopall()

def test_tweak_completions_without_equals(mocker):
    # Mocking a completion object with the necessary attributes
    completion_mock = Mock()
    completion_mock.name = "test"
    completion_mock.complete = "test"
    completion_mock.type = "type"
    completion_mock.description = "description"
    completion_mock.parent = "parent"
    completion_mock.full_name = "full_name"

    completions = [completion_mock]

    # Call the function with the mocked completions
    result = _tweak_completions(completions)

    # Verify the result
    assert len(result) == 1
    assert result[0].name == "test"
    assert result[0].complete == "test"
    assert result[0].type == "type"
    assert result[0].description == "description"
    assert result[0].parent == "parent"
    assert result[0].full_name == "full_name"

    # Clean up
    mocker.stopall()
