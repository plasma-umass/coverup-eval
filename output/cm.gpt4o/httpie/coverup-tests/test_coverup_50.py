# file httpie/cli/requestitems.py:23-29
# lines [23, 24, 25, 26, 27, 29]
# branches []

import pytest
from httpie.cli.requestitems import RequestItems, RequestHeadersDict, RequestDataDict, RequestJSONDataDict, RequestFilesDict, RequestQueryParamsDict, MultipartRequestDataDict

def test_request_items_initialization(mocker):
    mocker.patch('httpie.cli.requestitems.RequestHeadersDict', return_value={})
    mocker.patch('httpie.cli.requestitems.RequestDataDict', return_value={})
    mocker.patch('httpie.cli.requestitems.RequestJSONDataDict', return_value={})
    mocker.patch('httpie.cli.requestitems.RequestFilesDict', return_value={})
    mocker.patch('httpie.cli.requestitems.RequestQueryParamsDict', return_value={})
    mocker.patch('httpie.cli.requestitems.MultipartRequestDataDict', return_value={})

    # Test with as_form=False
    request_items = RequestItems(as_form=False)
    assert isinstance(request_items.headers, dict)
    assert isinstance(request_items.data, dict)
    assert isinstance(request_items.files, dict)
    assert isinstance(request_items.params, dict)
    assert isinstance(request_items.multipart_data, dict)

    # Test with as_form=True
    request_items = RequestItems(as_form=True)
    assert isinstance(request_items.headers, dict)
    assert isinstance(request_items.data, dict)
    assert isinstance(request_items.files, dict)
    assert isinstance(request_items.params, dict)
    assert isinstance(request_items.multipart_data, dict)
