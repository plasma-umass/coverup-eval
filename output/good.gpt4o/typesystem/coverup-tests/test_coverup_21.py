# file typesystem/json_schema.py:565-569
# lines [565, 566, 567, 568, 569]
# branches ['567->568', '567->569']

import pytest
from typesystem.fields import Field
from typesystem.json_schema import get_standard_properties

def test_get_standard_properties_with_default(mocker):
    # Mocking a Field object
    field = mocker.Mock(spec=Field)
    field.has_default.return_value = True
    field.default = "default_value"

    result = get_standard_properties(field)
    
    assert result == {"default": "default_value"}

def test_get_standard_properties_without_default(mocker):
    # Mocking a Field object
    field = mocker.Mock(spec=Field)
    field.has_default.return_value = False

    result = get_standard_properties(field)
    
    assert result == {}
