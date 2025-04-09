# file httpie/cli/requestitems.py:23-29
# lines [23, 24, 25, 26, 27, 29]
# branches []

import pytest
from httpie.cli.requestitems import RequestItems
from httpie.cli.requestitems import (
    RequestHeadersDict,
    RequestDataDict,
    RequestJSONDataDict,
    RequestFilesDict,
    RequestQueryParamsDict,
    MultipartRequestDataDict
)

def test_request_items_initialization(mocker):
    # Mock the RequestHeadersDict, RequestDataDict, RequestJSONDataDict, RequestFilesDict, and RequestQueryParamsDict
    mocker.patch('httpie.cli.requestitems.RequestHeadersDict', return_value=RequestHeadersDict())
    mocker.patch('httpie.cli.requestitems.RequestDataDict', return_value=RequestDataDict())
    mocker.patch('httpie.cli.requestitems.RequestJSONDataDict', return_value=RequestJSONDataDict())
    mocker.patch('httpie.cli.requestitems.RequestFilesDict', return_value=RequestFilesDict())
    mocker.patch('httpie.cli.requestitems.RequestQueryParamsDict', return_value=RequestQueryParamsDict())
    mocker.patch('httpie.cli.requestitems.MultipartRequestDataDict', return_value=MultipartRequestDataDict())

    # Test initialization with as_form=False
    items = RequestItems(as_form=False)
    assert isinstance(items.data, RequestJSONDataDict)

    # Test initialization with as_form=True
    items = RequestItems(as_form=True)
    assert isinstance(items.data, RequestDataDict)
