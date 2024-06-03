# file typesystem/tokenize/tokenize_yaml.py:112-128
# lines [125, 127, 128]
# branches []

import pytest
from typesystem.tokenize.tokenize_yaml import validate_yaml
from typesystem import String

def test_validate_yaml_with_missing_pyyaml(mocker):
    # Mock the yaml import to simulate 'pyyaml' not being installed
    mocker.patch('typesystem.tokenize.tokenize_yaml.yaml', None)
    
    content = "key: value"
    validator = String()
    
    with pytest.raises(AssertionError, match="'pyyaml' must be installed."):
        validate_yaml(content, validator)
