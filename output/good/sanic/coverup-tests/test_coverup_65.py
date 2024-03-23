# file sanic/blueprint_group.py:202-223
# lines [202, 215, 216, 217, 219, 220, 221, 222, 223]
# branches ['216->exit', '216->217', '219->220', '219->223']

import pytest
from unittest.mock import MagicMock
from sanic.blueprint_group import BlueprintGroup

@pytest.fixture
def blueprint_group():
    return BlueprintGroup()

@pytest.fixture
def mock_blueprint():
    blueprint = MagicMock()
    blueprint.middleware = MagicMock()
    return blueprint

def test_blueprint_group_middleware_with_function(blueprint_group, mock_blueprint):
    blueprint_group.append(mock_blueprint)
    
    def sample_middleware(request):
        pass

    blueprint_group.middleware(sample_middleware)

    mock_blueprint.middleware.assert_called_once_with(sample_middleware)

def test_blueprint_group_middleware_with_args(blueprint_group, mock_blueprint):
    blueprint_group.append(mock_blueprint)
    
    def sample_middleware(request):
        pass

    middleware_decorator = blueprint_group.middleware('arg1', 'arg2', kwarg1='value1')
    middleware_decorator(sample_middleware)

    mock_blueprint.middleware.assert_called_once_with(sample_middleware, 'arg1', 'arg2', kwarg1='value1')

# Cleanup is handled by pytest fixtures, no additional cleanup is necessary.
