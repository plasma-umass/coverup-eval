# file sanic/mixins/routes.py:527-593
# lines []
# branches ['592->exit']

import pytest
from sanic.mixins.routes import RouteMixin
from pathlib import PurePath
from unittest.mock import MagicMock

@pytest.fixture
def route_mixin():
    mixin = RouteMixin()
    mixin._generate_name = MagicMock(return_value="generated_name")
    mixin._apply_static = MagicMock()
    mixin._future_statics = set()
    mixin.strict_slashes = None
    return mixin

def test_static_apply_false(route_mixin):
    # Test with apply set to False, which should not call _apply_static
    route_mixin.static(
        uri="/static",
        file_or_directory="/path/to/static",
        apply=False
    )
    route_mixin._apply_static.assert_not_called()
    assert len(route_mixin._future_statics) == 1

def test_static_apply_true(route_mixin):
    # Test with apply set to True, which should call _apply_static
    route_mixin.static(
        uri="/static",
        file_or_directory="/path/to/static",
        apply=True
    )
    route_mixin._apply_static.assert_called_once()
    assert len(route_mixin._future_statics) == 1
