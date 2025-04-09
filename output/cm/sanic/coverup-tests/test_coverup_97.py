# file sanic/mixins/routes.py:527-593
# lines [571]
# branches ['570->571', '592->exit']

import pytest
from sanic.mixins.routes import RouteMixin
from pathlib import PurePath
from unittest.mock import MagicMock

@pytest.fixture
def route_mixin():
    mixin = RouteMixin()
    mixin.strict_slashes = True
    mixin._generate_name = MagicMock(return_value="generated_name")
    mixin._apply_static = MagicMock()
    mixin._future_statics = set()
    return mixin

def test_static_with_strict_slashes_and_apply(route_mixin, tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("test content")

    # Call the static method with strict_slashes=None and apply=True
    # This should trigger line 571 and branch 592->exit
    routes = route_mixin.static(
        uri="/test",
        file_or_directory=str(file_path),
        strict_slashes=None,
        apply=True
    )

    # Assert that strict_slashes was set to the mixin's strict_slashes
    assert route_mixin._future_statics.pop().strict_slashes is True
    # Assert that _apply_static was called
    route_mixin._apply_static.assert_called_once()
