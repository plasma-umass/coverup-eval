# file sanic/blueprint_group.py:130-141
# lines [130, 141]
# branches []

import pytest
from sanic.blueprint_group import BlueprintGroup
from unittest.mock import MagicMock

class TestBlueprintGroup:
    def test_setitem(self):
        # Create a mock Blueprint object
        mock_blueprint = MagicMock()
        
        # Create an instance of BlueprintGroup and set up the internal list
        blueprint_group = BlueprintGroup()
        blueprint_group._blueprints = [MagicMock(), MagicMock(), MagicMock()]
        
        # Set a new item at a specific index
        index_to_set = 1
        blueprint_group[index_to_set] = mock_blueprint
        
        # Assert that the item was set correctly
        assert blueprint_group._blueprints[index_to_set] == mock_blueprint
