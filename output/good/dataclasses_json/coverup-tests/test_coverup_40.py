# file dataclasses_json/core.py:211-231
# lines [217]
# branches ['216->217']

import pytest
from datetime import datetime
from dataclasses_json.core import _support_extended_types

@pytest.fixture
def cleanup():
    # Setup if necessary
    yield
    # Teardown if necessary

def test_support_extended_types_datetime_already_instance(mocker, cleanup):
    # Mocking _issubclass_safe to return True for datetime
    mocker.patch('dataclasses_json.core._issubclass_safe', return_value=True)
    # Creating a datetime instance
    dt_instance = datetime.now()
    # Call the function with a datetime instance
    result = _support_extended_types(datetime, dt_instance)
    # Assert that the result is the same datetime instance
    assert result is dt_instance
