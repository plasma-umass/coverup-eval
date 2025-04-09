# file sanic/mixins/routes.py:622-730
# lines [622, 629, 630, 634, 635, 639, 640, 641, 642, 647, 648, 649, 650, 651, 653, 654, 655, 656, 658, 659, 662, 663, 664, 665, 666, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 684, 685, 686, 688, 689, 690, 691, 692, 695, 696, 697, 699, 701, 703, 704, 706, 707, 708, 710, 712, 713, 714, 715, 716, 718, 719, 720, 721, 722, 723, 724, 726, 727, 728, 729]
# branches ['634->635', '634->639', '640->641', '640->647', '648->649', '648->658', '663->664', '663->671', '668->669', '668->670', '672->673', '672->688', '674->675', '674->676', '678->679', '678->688', '685->686', '685->688', '688->689', '688->703', '695->699', '695->701', '703->704', '703->706', '706->707', '706->718', '707->708', '707->710', '712->713', '712->714', '714->715', '714->718']

import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from sanic.exceptions import InvalidUsage, FileNotFound
from sanic.response import HTTPResponse
from sanic.mixins.routes import RouteMixin
from sanic.handlers import ContentRangeHandler, HeaderNotFound, ContentRangeError
from os import path
from urllib.parse import unquote
from time import gmtime, strftime

@pytest.mark.asyncio
async def test_static_request_handler_invalid_url():
    route_mixin = RouteMixin()
    with pytest.raises(InvalidUsage):
        await route_mixin._static_request_handler(
            file_or_directory="/some/path",
            use_modified_since=False,
            use_content_range=False,
            stream_large_files=False,
            request=MagicMock(),
            __file_uri__="../invalid/path"
        )

@pytest.mark.asyncio
async def test_static_request_handler_file_not_found(mocker):
    route_mixin = RouteMixin()
    mocker.patch("sanic.mixins.routes.path.abspath", side_effect=lambda x: x)
    mocker.patch("sanic.mixins.routes.unquote", side_effect=lambda x: x)
    mocker.patch("sanic.mixins.routes.path.join", side_effect=lambda x, y: f"{x}/{y}")
    mocker.patch("sanic.mixins.routes.stat_async", side_effect=FileNotFoundError)
    mocker.patch("sanic.mixins.routes.error_logger.exception")

    with pytest.raises(FileNotFound):
        await route_mixin._static_request_handler(
            file_or_directory="/some/path",
            use_modified_since=False,
            use_content_range=False,
            stream_large_files=False,
            request=MagicMock(),
            __file_uri__="nonexistent_file"
        )

@pytest.mark.asyncio
async def test_static_request_handler_if_modified_since(mocker):
    route_mixin = RouteMixin()
    mock_request = MagicMock()
    mock_request.headers = {"If-Modified-Since": "Wed, 21 Oct 2015 07:28:00 GMT"}
    mock_stat = MagicMock()
    mock_stat.st_mtime = 1445412480

    mocker.patch("sanic.mixins.routes.path.abspath", side_effect=lambda x: x)
    mocker.patch("sanic.mixins.routes.unquote", side_effect=lambda x: x)
    mocker.patch("sanic.mixins.routes.path.join", side_effect=lambda x, y: f"{x}/{y}")
    mocker.patch("sanic.mixins.routes.stat_async", return_value=mock_stat)

    response = await route_mixin._static_request_handler(
        file_or_directory="/some/path",
        use_modified_since=True,
        use_content_range=False,
        stream_large_files=False,
        request=mock_request,
        __file_uri__="file"
    )

    assert response.status == 304

@pytest.mark.asyncio
async def test_static_request_handler_content_range(mocker):
    route_mixin = RouteMixin()
    mock_request = MagicMock()
    mock_request.method = "GET"
    mock_stat = MagicMock()
    mock_stat.st_size = 1000

    mocker.patch("sanic.mixins.routes.path.abspath", side_effect=lambda x: x)
    mocker.patch("sanic.mixins.routes.unquote", side_effect=lambda x: x)
    mocker.patch("sanic.mixins.routes.path.join", side_effect=lambda x, y: f"{x}/{y}")
    mocker.patch("sanic.mixins.routes.stat_async", return_value=mock_stat)
    mocker.patch("sanic.mixins.routes.ContentRangeHandler", side_effect=HeaderNotFound)

    response = await route_mixin._static_request_handler(
        file_or_directory="/some/path",
        use_modified_since=False,
        use_content_range=True,
        stream_large_files=False,
        request=mock_request,
        __file_uri__="file"
    )

    assert response.status == 200
    assert response.headers["Accept-Ranges"] == "bytes"
    assert response.headers["Content-Length"] == "1000"

@pytest.mark.asyncio
async def test_static_request_handler_stream_large_files(mocker):
    route_mixin = RouteMixin()
    mock_request = MagicMock()
    mock_request.method = "GET"
    mock_stat = MagicMock()
    mock_stat.st_size = 2000000

    mocker.patch("sanic.mixins.routes.path.abspath", side_effect=lambda x: x)
    mocker.patch("sanic.mixins.routes.unquote", side_effect=lambda x: x)
    mocker.patch("sanic.mixins.routes.path.join", side_effect=lambda x, y: f"{x}/{y}")
    mocker.patch("sanic.mixins.routes.stat_async", return_value=mock_stat)
    mocker.patch("sanic.mixins.routes.file_stream", new_callable=AsyncMock)

    response = await route_mixin._static_request_handler(
        file_or_directory="/some/path",
        use_modified_since=False,
        use_content_range=False,
        stream_large_files=True,
        request=mock_request,
        __file_uri__="large_file"
    )

    assert response.status == 200
    assert mocker.patch("sanic.mixins.routes.file_stream").called
