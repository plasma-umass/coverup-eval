# file sanic/mixins/routes.py:527-593
# lines [527, 531, 532, 533, 534, 535, 536, 537, 538, 539, 568, 570, 571, 573, 574, 575, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 590, 592, 593]
# branches ['570->571', '570->573', '573->574', '573->578', '592->exit', '592->593']

import pytest
from unittest.mock import Mock, patch
from pathlib import PurePath
from sanic.mixins.routes import RouteMixin

class TestRouteMixin:
    @pytest.fixture
    def route_mixin(self):
        return RouteMixin()

    def test_static_with_valid_path(self, route_mixin):
        route_mixin._generate_name = Mock(return_value="static")
        route_mixin._future_statics = set()
        route_mixin._apply_static = Mock()
        route_mixin.strict_slashes = None

        route_mixin.static(
            uri="/static",
            file_or_directory="path/to/static",
            pattern=r"/?.+",
            use_modified_since=True,
            use_content_range=False,
            stream_large_files=False,
            name="static",
            host=None,
            strict_slashes=None,
            content_type=None,
            apply=True,
        )

        assert len(route_mixin._future_statics) == 1
        route_mixin._apply_static.assert_called_once()

    def test_static_with_invalid_path(self, route_mixin):
        with pytest.raises(ValueError, match="Static route must be a valid path"):
            route_mixin.static(
                uri="/static",
                file_or_directory=123,  # Invalid path type
                pattern=r"/?.+",
                use_modified_since=True,
                use_content_range=False,
                stream_large_files=False,
                name="static",
                host=None,
                strict_slashes=None,
                content_type=None,
                apply=True,
            )

    def test_static_with_strict_slashes(self, route_mixin):
        route_mixin._generate_name = Mock(return_value="static")
        route_mixin._future_statics = set()
        route_mixin._apply_static = Mock()
        route_mixin.strict_slashes = True

        route_mixin.static(
            uri="/static",
            file_or_directory="path/to/static",
            pattern=r"/?.+",
            use_modified_since=True,
            use_content_range=False,
            stream_large_files=False,
            name="static",
            host=None,
            strict_slashes=None,  # Should inherit from self.strict_slashes
            content_type=None,
            apply=True,
        )

        assert len(route_mixin._future_statics) == 1
        route_mixin._apply_static.assert_called_once()
        assert next(iter(route_mixin._future_statics)).strict_slashes is True
