# file sanic/mixins/routes.py:622-730
# lines [622, 629, 630, 634, 635, 639, 640, 641, 642, 647, 648, 649, 650, 651, 653, 654, 655, 656, 658, 659, 662, 663, 664, 665, 666, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 684, 685, 686, 688, 689, 690, 691, 692, 695, 696, 697, 699, 701, 703, 704, 706, 707, 708, 710, 712, 713, 714, 715, 716, 718, 719, 720, 721, 722, 723, 724, 726, 727, 728, 729]
# branches ['634->635', '634->639', '640->641', '640->647', '648->649', '648->658', '663->664', '663->671', '668->669', '668->670', '672->673', '672->688', '674->675', '674->676', '678->679', '678->688', '685->686', '685->688', '688->689', '688->703', '695->699', '695->701', '703->704', '703->706', '706->707', '706->718', '707->708', '707->710', '712->713', '712->714', '714->715', '714->718']

import os
from unittest.mock import MagicMock
from sanic.exceptions import InvalidUsage, FileNotFound
from sanic.response import HTTPResponse
from sanic.mixins.routes import RouteMixin
from urllib.parse import unquote
from os import path
import pytest

@pytest.mark.asyncio
async def test_static_request_handler_invalid_url(mocker):
    mixin = RouteMixin()
    request = MagicMock()
    request.headers = {}
    request.method = 'GET'
    
    with pytest.raises(InvalidUsage):
        await mixin._static_request_handler(
            file_or_directory='/valid/path',
            use_modified_since=False,
            use_content_range=False,
            stream_large_files=False,
            request=request,
            __file_uri__='../invalid/path'
        )

@pytest.mark.asyncio
async def test_static_request_handler_file_not_found(mocker):
    mixin = RouteMixin()
    request = MagicMock()
    request.headers = {}
    request.method = 'GET'
    mocker.patch('os.path.abspath', side_effect=lambda x: x)
    mocker.patch('os.path.join', side_effect=lambda x, y: x + y)
    mocker.patch('os.path.realpath', side_effect=lambda x: x)
    mocker.patch('os.path.exists', return_value=False)
    mocker.patch('os.stat', side_effect=FileNotFoundError)
    mocker.patch('sanic.log.error_logger.exception')

    with pytest.raises(FileNotFound):
        await mixin._static_request_handler(
            file_or_directory='/valid/path',
            use_modified_since=False,
            use_content_range=False,
            stream_large_files=False,
            request=request,
            __file_uri__='/unexisting/file'
        )

@pytest.mark.asyncio
async def test_static_request_handler_directory_traversal(mocker):
    mixin = RouteMixin()
    request = MagicMock()
    request.headers = {}
    request.method = 'GET'
    mocker.patch('os.path.abspath', side_effect=lambda x: x)
    mocker.patch('os.path.join', side_effect=lambda x, y: x + y)
    mocker.patch('os.path.realpath', side_effect=lambda x: x)
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.stat', side_effect=FileNotFoundError)
    mocker.patch('sanic.log.error_logger.exception')

    with pytest.raises(FileNotFound):
        await mixin._static_request_handler(
            file_or_directory='/valid/path',
            use_modified_since=False,
            use_content_range=False,
            stream_large_files=False,
            request=request,
            __file_uri__='/../outside/path'
        )
