# file sanic/mixins/routes.py:527-593
# lines [527, 531, 532, 533, 534, 535, 536, 537, 538, 539, 568, 570, 571, 573, 574, 575, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 590, 592, 593]
# branches ['570->571', '570->573', '573->574', '573->578', '592->exit', '592->593']

import pytest
from sanic import Sanic
from sanic.mixins.routes import RouteMixin
from pathlib import PurePath
from unittest.mock import MagicMock

class MockRouteMixin(RouteMixin):
    def __init__(self):
        self._future_statics = set()
        self.strict_slashes = None
        self._apply_static = MagicMock()

    def _generate_name(self, name):
        return f"generated_{name}"

@pytest.fixture
def mock_route_mixin():
    return MockRouteMixin()

def test_static_method_with_pure_path(mock_route_mixin):
    uri = "/static"
    file_or_directory = PurePath("/path/to/static")
    pattern = r"/?.+"
    use_modified_since = True
    use_content_range = False
    stream_large_files = False
    name = "static"
    host = None
    strict_slashes = None
    content_type = None
    apply = True

    mock_route_mixin.static(
        uri,
        file_or_directory,
        pattern,
        use_modified_since,
        use_content_range,
        stream_large_files,
        name,
        host,
        strict_slashes,
        content_type,
        apply
    )

    assert len(mock_route_mixin._future_statics) == 1
    static_route = next(iter(mock_route_mixin._future_statics))
    assert static_route.uri == uri
    assert static_route.file_or_directory == file_or_directory
    assert static_route.pattern == pattern
    assert static_route.use_modified_since == use_modified_since
    assert static_route.use_content_range == use_content_range
    assert static_route.stream_large_files == stream_large_files
    assert static_route.name == f"generated_{name}"
    assert static_route.host == host
    assert static_route.strict_slashes == strict_slashes
    assert static_route.content_type == content_type
    mock_route_mixin._apply_static.assert_called_once_with(static_route)

def test_static_method_with_invalid_path_type(mock_route_mixin):
    with pytest.raises(ValueError) as exc_info:
        mock_route_mixin.static(
            uri="/static",
            file_or_directory=123,  # Invalid type
            pattern=r"/?.+",
            use_modified_since=True,
            use_content_range=False,
            stream_large_files=False,
            name="static",
            host=None,
            strict_slashes=None,
            content_type=None,
            apply=True
        )
    assert "Static route must be a valid path, not 123" in str(exc_info.value)
