# file dataclasses_json/undefined.py:169-191
# lines [184]
# branches ['183->184']

import dataclasses
import pytest
from dataclasses_json.undefined import _CatchAllUndefinedParameters
from dataclasses import Field, MISSING

@pytest.fixture
def cleanup():
    # Fixture to clean up any state after tests
    yield
    # No cleanup needed for this specific test case

@pytest.fixture
def mock_field(mocker):
    # Create a mock Field object with a default value
    field = mocker.Mock(spec=Field)
    field.default = 42
    field.default_factory = dataclasses._MISSING_TYPE
    return field

def test_catch_all_undefined_parameters_get_default_with_default(cleanup, mock_field):
    # Test the branch where the field has a default value
    default_value = _CatchAllUndefinedParameters._get_default(mock_field)
    assert default_value == 42  # Assert that the default value is returned
