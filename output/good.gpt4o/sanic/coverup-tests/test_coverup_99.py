# file sanic/blueprint_group.py:182-189
# lines [189]
# branches []

import pytest
from sanic.blueprint_group import BlueprintGroup
from sanic import Blueprint

@pytest.fixture
def blueprint_group():
    return BlueprintGroup()

def test_append_blueprint(blueprint_group, mocker):
    # Mock the _sanitize_blueprint method to ensure it is called
    mock_sanitize = mocker.patch('sanic.blueprint_group.BlueprintGroup._sanitize_blueprint', return_value=Blueprint('test_bp'))

    # Create a mock Blueprint object
    mock_blueprint = Blueprint('mock_bp')

    # Append the mock Blueprint to the BlueprintGroup
    blueprint_group.append(mock_blueprint)

    # Assert that _sanitize_blueprint was called with the correct argument
    mock_sanitize.assert_called_once_with(bp=mock_blueprint)

    # Assert that the BlueprintGroup's _blueprints list contains the sanitized Blueprint
    assert blueprint_group._blueprints[-1].name == 'test_bp'
