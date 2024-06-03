# file sanic/blueprint_group.py:130-141
# lines [130, 141]
# branches []

import pytest
from sanic.blueprint_group import BlueprintGroup
from sanic import Blueprint

class TestBlueprintGroup:
    def test_setitem(self):
        # Create a BlueprintGroup instance
        group = BlueprintGroup()
        group._blueprints = [Blueprint('bp1'), Blueprint('bp2')]

        # Create a new Blueprint
        new_bp = Blueprint('new_bp')

        # Set the new Blueprint at index 1
        group[1] = new_bp

        # Assert that the Blueprint at index 1 is now the new Blueprint
        assert group._blueprints[1] == new_bp

        # Clean up
        del group
