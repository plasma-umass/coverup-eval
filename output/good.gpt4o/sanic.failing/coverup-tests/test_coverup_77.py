# file sanic/blueprint_group.py:182-189
# lines [182, 189]
# branches []

import pytest
from sanic.blueprint_group import BlueprintGroup
from sanic import Blueprint

class TestBlueprintGroup:
    def test_append(self, mocker):
        # Create a mock Blueprint object
        mock_blueprint = mocker.Mock(spec=Blueprint)
        
        # Mock the _sanitize_blueprint method to return the mock blueprint
        mocker.patch.object(BlueprintGroup, '_sanitize_blueprint', return_value=mock_blueprint)
        
        # Create an instance of BlueprintGroup
        blueprint_group = BlueprintGroup()
        
        # Mock the _blueprints attribute as a list
        blueprint_group._blueprints = []
        
        # Append the mock blueprint to the group
        blueprint_group.append(mock_blueprint)
        
        # Assert that the blueprint was appended to the _blueprints list
        assert blueprint_group._blueprints == [mock_blueprint]
        
        # Assert that _sanitize_blueprint was called with the correct argument
        blueprint_group._sanitize_blueprint.assert_called_once_with(bp=mock_blueprint)
