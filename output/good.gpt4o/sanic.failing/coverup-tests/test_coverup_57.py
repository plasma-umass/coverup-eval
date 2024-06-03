# file sanic/blueprint_group.py:91-99
# lines [91, 92, 99]
# branches []

import pytest
from sanic.blueprint_group import BlueprintGroup

class TestBlueprintGroup:
    def test_version_property(self, mocker):
        # Create a mock instance of BlueprintGroup
        mock_blueprint_group = mocker.MagicMock(spec=BlueprintGroup)
        
        # Set the _version attribute
        mock_blueprint_group._version = "1.0"
        
        # Access the version property
        version = BlueprintGroup.version.__get__(mock_blueprint_group)
        
        # Assert that the version property returns the correct value
        assert version == "1.0"
