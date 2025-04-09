# file sanic/blueprint_group.py:156-162
# lines [156, 162]
# branches []

import pytest
from sanic.blueprint_group import BlueprintGroup

class TestBlueprintGroup:
    def test_len(self, mocker):
        # Create a mock for the _blueprints attribute
        mocker.patch.object(BlueprintGroup, '_blueprints', new_callable=mocker.PropertyMock, return_value=['blueprint1', 'blueprint2', 'blueprint3'])
        
        # Initialize the BlueprintGroup object
        blueprint_group = BlueprintGroup()
        
        # Assert the length of the blueprint group
        assert len(blueprint_group) == 3
