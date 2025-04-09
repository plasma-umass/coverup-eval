# file: httpie/cli/requestitems.py:23-29
# asked: {"lines": [23, 24, 25, 26, 27, 29], "branches": []}
# gained: {"lines": [23, 24, 25, 26, 27, 29], "branches": []}

import pytest
from httpie.cli.requestitems import RequestItems
from httpie.cli.dicts import (
    RequestHeadersDict,
    RequestDataDict,
    RequestFilesDict,
    RequestJSONDataDict,
    RequestQueryParamsDict,
    MultipartRequestDataDict
)

def test_request_items_init_as_form():
    request_items = RequestItems(as_form=True)
    assert isinstance(request_items.headers, RequestHeadersDict)
    assert isinstance(request_items.data, RequestDataDict)
    assert isinstance(request_items.files, RequestFilesDict)
    assert isinstance(request_items.params, RequestQueryParamsDict)
    assert isinstance(request_items.multipart_data, MultipartRequestDataDict)

def test_request_items_init_not_as_form():
    request_items = RequestItems(as_form=False)
    assert isinstance(request_items.headers, RequestHeadersDict)
    assert isinstance(request_items.data, RequestJSONDataDict)
    assert isinstance(request_items.files, RequestFilesDict)
    assert isinstance(request_items.params, RequestQueryParamsDict)
    assert isinstance(request_items.multipart_data, MultipartRequestDataDict)
