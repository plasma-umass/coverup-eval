# file sanic/blueprint_group.py:82-89
# lines [89]
# branches []

import pytest
from sanic.blueprint_group import BlueprintGroup
from sanic import Blueprint

def test_blueprint_group_blueprints_property():
    # Create a mock Blueprint instance
    mock_blueprint = Blueprint('mock_blueprint')

    # Create an instance of BlueprintGroup and add the mock blueprint
    blueprint_group = BlueprintGroup()
    blueprint_group._blueprints = [mock_blueprint]

    # Access the blueprints property
    blueprints = blueprint_group.blueprints

    # Assert that the blueprints property returns the correct list
    assert blueprints == [mock_blueprint]

    # Clean up
    del blueprint_group._blueprints
