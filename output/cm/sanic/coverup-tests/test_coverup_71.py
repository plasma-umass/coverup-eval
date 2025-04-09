# file sanic/blueprint_group.py:91-99
# lines [91, 92, 99]
# branches []

import pytest
from sanic.blueprint_group import BlueprintGroup
from typing import Optional, Union

# Assuming the BlueprintGroup class has other necessary methods implemented
# as it inherits from MutableSequence, we will focus on testing the `version` property.

@pytest.fixture
def blueprint_group():
    bg = BlueprintGroup()
    yield bg
    # No cleanup needed as the BlueprintGroup instance is local to the test

def test_blueprint_group_version_property(blueprint_group):
    # Test the default version value (should be None if not set)
    assert blueprint_group.version is None, "Default version should be None"

    # Set the version to a specific value and test
    blueprint_group._version = '1.0'
    assert blueprint_group.version == '1.0', "Version should be '1.0'"

    # Set the version to a different type (int) and test
    blueprint_group._version = 2
    assert blueprint_group.version == 2, "Version should be 2"

    # Set the version to another type (float) and test
    blueprint_group._version = 3.1
    assert blueprint_group.version == 3.1, "Version should be 3.1"

# Note: The actual implementation of the BlueprintGroup class is not provided,
# so this test assumes that the class has an attribute `_version` which is
# manipulated directly for testing purposes. In a real-world scenario, there
# would likely be a method to set the version, rather than setting a protected
# attribute directly.
