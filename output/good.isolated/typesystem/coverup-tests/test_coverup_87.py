# file typesystem/tokenize/tokenize_yaml.py:112-128
# lines [125, 127, 128]
# branches []

import pytest
from typesystem.tokenize.tokenize_yaml import validate_yaml
from typesystem.fields import Field
from typesystem.schemas import Schema

def test_validate_yaml_missing_lines(mocker):
    # Mock the yaml import to be None to trigger the assertion
    mocker.patch('typesystem.tokenize.tokenize_yaml.yaml', None)
    
    # Define a dummy validator
    class DummySchema(Schema):
        pass

    # Attempt to call validate_yaml with a string and the dummy validator
    with pytest.raises(AssertionError) as excinfo:
        validate_yaml("test: 1", DummySchema)
    
    # Check that the assertion error message is as expected
    assert str(excinfo.value) == "'pyyaml' must be installed."
