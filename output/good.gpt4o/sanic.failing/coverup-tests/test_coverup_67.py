# file sanic/blueprint_group.py:143-154
# lines [143, 154]
# branches []

import pytest
from sanic.blueprint_group import BlueprintGroup

class TestBlueprintGroup:
    def test_delitem(self):
        # Create a mock BlueprintGroup with some blueprints
        group = BlueprintGroup()
        group._blueprints = ['blueprint1', 'blueprint2', 'blueprint3']
        
        # Delete the second blueprint
        del group[1]
        
        # Assert the blueprint was removed
        assert group._blueprints == ['blueprint1', 'blueprint3']
        
        # Clean up
        del group
