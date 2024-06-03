# file sanic/blueprint_group.py:191-200
# lines [191, 200]
# branches []

import pytest
from sanic.blueprint_group import BlueprintGroup
from sanic import Blueprint

class TestBlueprintGroup:
    def test_insert(self, mocker):
        # Create a mock Blueprint object
        mock_blueprint = mocker.Mock(spec=Blueprint)
        
        # Create a BlueprintGroup instance
        blueprint_group = BlueprintGroup()
        
        # Mock the _sanitize_blueprint method to return the mock blueprint
        mock_sanitize_blueprint = mocker.patch.object(BlueprintGroup, '_sanitize_blueprint', return_value=mock_blueprint)
        
        # Mock the _blueprints attribute to be a list
        blueprint_group._blueprints = []
        
        # Insert the mock blueprint at index 0
        blueprint_group.insert(0, mock_blueprint)
        
        # Assert that the blueprint was inserted correctly
        assert blueprint_group._blueprints[0] == mock_blueprint
        assert len(blueprint_group._blueprints) == 1
        
        # Ensure the mock was called
        mock_sanitize_blueprint.assert_called_once_with(mock_blueprint)
