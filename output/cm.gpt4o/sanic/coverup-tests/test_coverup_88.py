# file sanic/blueprint_group.py:191-200
# lines [191, 200]
# branches []

import pytest
from sanic.blueprint_group import BlueprintGroup
from sanic import Blueprint

class TestBlueprintGroup:
    def test_insert(self, mocker):
        # Mock the Blueprint class
        mock_blueprint = mocker.Mock(spec=Blueprint)
        
        # Create an instance of BlueprintGroup
        blueprint_group = BlueprintGroup()
        
        # Mock the _sanitize_blueprint method using a class-level patch
        mock_sanitize = mocker.patch.object(BlueprintGroup, '_sanitize_blueprint', return_value=mock_blueprint)
        
        # Mock the _blueprints attribute
        blueprint_group._blueprints = []
        
        # Insert the mock blueprint at index 0
        blueprint_group.insert(0, mock_blueprint)
        
        # Assertions to verify the behavior
        mock_sanitize.assert_called_once_with(mock_blueprint)
        assert blueprint_group._blueprints == [mock_blueprint]
