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

    def test_static_with_invalid_file_or_directory(self, route_mixin):
        with pytest.raises(ValueError, match="Static route must be a valid path"):
            route_mixin.static("/static", 12345)

    def test_static_with_valid_file_or_directory(self, route_mixin, mocker):
        mock_generate_name = mocker.patch.object(route_mixin, '_generate_name', return_value="static")
        mock_apply_static = mocker.patch.object(route_mixin, '_apply_static')
        mock_future_statics = mocker.patch.object(route_mixin, '_future_statics', new_callable=set)

        route_mixin.strict_slashes = True
        route_mixin.static("/static", "/path/to/static")

        mock_generate_name.assert_called_once_with("static")
        assert len(mock_future_statics) == 1
        static = next(iter(mock_future_statics))
        assert static.uri == "/static"
        assert static.file_or_directory == "/path/to/static"
        assert static.name == "static"
        assert static.strict_slashes is True
        mock_apply_static.assert_called_once_with(static)

    def test_static_with_apply_false(self, route_mixin, mocker):
        mock_generate_name = mocker.patch.object(route_mixin, '_generate_name', return_value="static")
        mock_apply_static = mocker.patch.object(route_mixin, '_apply_static')
        mock_future_statics = mocker.patch.object(route_mixin, '_future_statics', new_callable=set)

        route_mixin.static("/static", "/path/to/static", apply=False)

        mock_generate_name.assert_called_once_with("static")
        assert len(mock_future_statics) == 1
        static = next(iter(mock_future_statics))
        assert static.uri == "/static"
        assert static.file_or_directory == "/path/to/static"
        assert static.name == "static"
        mock_apply_static.assert_not_called()
