# file sanic/mixins/routes.py:622-730
# lines [622, 629, 630, 634, 635, 639, 640, 641, 642, 647, 648, 649, 650, 651, 653, 654, 655, 656, 658, 659, 662, 663, 664, 665, 666, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 684, 685, 686, 688, 689, 690, 691, 692, 695, 696, 697, 699, 701, 703, 704, 706, 707, 708, 710, 712, 713, 714, 715, 716, 718, 719, 720, 721, 722, 723, 724, 726, 727, 728, 729]
# branches ['634->635', '634->639', '640->641', '640->647', '648->649', '648->658', '663->664', '663->671', '668->669', '668->670', '672->673', '672->688', '674->675', '674->676', '678->679', '678->688', '685->686', '685->688', '688->689', '688->703', '695->699', '695->701', '703->704', '703->706', '706->707', '706->718', '707->708', '707->710', '712->713', '712->714', '714->715', '714->718']

import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from sanic.response import HTTPResponse
from sanic.exceptions import InvalidUsage, FileNotFound
from sanic.mixins.routes import RouteMixin
from sanic.handlers import ContentRangeHandler, HeaderNotFound, ContentRangeError
from os import path
from urllib.parse import unquote
from re import sub
from time import gmtime, strftime

@pytest.mark.asyncio
async def test_static_request_handler_invalid_url():
    route_mixin = RouteMixin()
    request = MagicMock()
    with pytest.raises(InvalidUsage):
        await route_mixin._static_request_handler(
            file_or_directory="/some/path",
            use_modified_since=False,
            use_content_range=False,
            stream_large_files=False,
            request=request,
            __file_uri__="../invalid/path"
        )

@pytest.mark.asyncio
async def test_static_request_handler_file_not_found():
    route_mixin = RouteMixin()
    request = MagicMock()
    with patch("sanic.mixins.routes.path.abspath", return_value="/some/path/file.txt"):
        with pytest.raises(FileNotFound):
            await route_mixin._static_request_handler(
                file_or_directory="/some/path",
                use_modified_since=False,
                use_content_range=False,
                stream_large_files=False,
                request=request,
                __file_uri__="nonexistent_file.txt"
            )

@pytest.mark.asyncio
async def test_static_request_handler_if_modified_since():
    route_mixin = RouteMixin()
    request = MagicMock()
    request.headers = {"If-Modified-Since": "Wed, 21 Oct 2015 07:28:00 GMT"}
    with patch("sanic.mixins.routes.stat_async", new_callable=AsyncMock) as mock_stat:
        mock_stat.return_value.st_mtime = 1445412480
        response = await route_mixin._static_request_handler(
            file_or_directory="/some/path",
            use_modified_since=True,
            use_content_range=False,
            stream_large_files=False,
            request=request,
            __file_uri__="file.txt"
        )
        assert response.status == 304

@pytest.mark.asyncio
async def test_static_request_handler_content_range():
    route_mixin = RouteMixin()
    request = MagicMock()
    request.method = "GET"
    with patch("sanic.mixins.routes.stat_async", new_callable=AsyncMock) as mock_stat:
        mock_stat.return_value.st_size = 1000
        with patch("sanic.mixins.routes.ContentRangeHandler", side_effect=HeaderNotFound):
            response = await route_mixin._static_request_handler(
                file_or_directory="/some/path",
                use_modified_since=False,
                use_content_range=True,
                stream_large_files=False,
                request=request,
                __file_uri__="file.txt"
            )
            assert "Accept-Ranges" in response.headers
            assert response.headers["Content-Length"] == "1000"

@pytest.mark.asyncio
async def test_static_request_handler_stream_large_files():
    route_mixin = RouteMixin()
    request = MagicMock()
    request.method = "GET"
    with patch("sanic.mixins.routes.stat_async", new_callable=AsyncMock) as mock_stat:
        mock_stat.return_value.st_size = 2 * 1024 * 1024  # 2 MB
        with patch("sanic.mixins.routes.file_stream", new_callable=AsyncMock) as mock_file_stream:
            response = await route_mixin._static_request_handler(
                file_or_directory="/some/path",
                use_modified_since=False,
                use_content_range=False,
                stream_large_files=True,
                request=request,
                __file_uri__="large_file.txt"
            )
            mock_file_stream.assert_awaited_once()

@pytest.mark.asyncio
async def test_static_request_handler_content_range_error():
    route_mixin = RouteMixin()
    request = MagicMock()
    request.method = "GET"
    with patch("sanic.mixins.routes.stat_async", new_callable=AsyncMock) as mock_stat:
        mock_stat.return_value.st_size = 1000
        with patch("sanic.mixins.routes.ContentRangeHandler", side_effect=ContentRangeError):
            with pytest.raises(ContentRangeError):
                await route_mixin._static_request_handler(
                    file_or_directory="/some/path",
                    use_modified_since=False,
                    use_content_range=True,
                    stream_large_files=False,
                    request=request,
                    __file_uri__="file.txt"
                )
