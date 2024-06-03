# file sanic/blueprint_group.py:101-108
# lines [101, 102, 108]
# branches []

import pytest
from sanic.blueprint_group import BlueprintGroup

class TestBlueprintGroup:
    def test_strict_slashes_property(self, mocker):
        # Create a mock instance of BlueprintGroup
        mock_blueprint_group = mocker.MagicMock(spec=BlueprintGroup)
        
        # Set the _strict_slashes attribute
        mock_blueprint_group._strict_slashes = True
        
        # Access the strict_slashes property
        result = BlueprintGroup.strict_slashes.__get__(mock_blueprint_group)
        
        # Assert that the property returns the correct value
        assert result is True
