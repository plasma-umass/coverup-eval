# file: httpie/cli/requestitems.py:23-29
# asked: {"lines": [23, 24, 25, 26, 27, 29], "branches": []}
# gained: {"lines": [23, 24, 25, 26, 27, 29], "branches": []}

import pytest
from httpie.cli.requestitems import RequestItems, RequestHeadersDict, RequestDataDict, RequestJSONDataDict, RequestFilesDict, RequestQueryParamsDict, MultipartRequestDataDict

def test_request_items_initialization_as_form(monkeypatch):
    # Mock the dependent classes
    monkeypatch.setattr('httpie.cli.requestitems.RequestHeadersDict', lambda: 'mock_headers')
    monkeypatch.setattr('httpie.cli.requestitems.RequestDataDict', lambda: 'mock_data')
    monkeypatch.setattr('httpie.cli.requestitems.RequestFilesDict', lambda: 'mock_files')
    monkeypatch.setattr('httpie.cli.requestitems.RequestQueryParamsDict', lambda: 'mock_params')
    monkeypatch.setattr('httpie.cli.requestitems.MultipartRequestDataDict', lambda: 'mock_multipart_data')

    request_items = RequestItems(as_form=True)

    assert request_items.headers == 'mock_headers'
    assert request_items.data == 'mock_data'
    assert request_items.files == 'mock_files'
    assert request_items.params == 'mock_params'
    assert request_items.multipart_data == 'mock_multipart_data'

def test_request_items_initialization_as_json(monkeypatch):
    # Mock the dependent classes
    monkeypatch.setattr('httpie.cli.requestitems.RequestHeadersDict', lambda: 'mock_headers')
    monkeypatch.setattr('httpie.cli.requestitems.RequestJSONDataDict', lambda: 'mock_json_data')
    monkeypatch.setattr('httpie.cli.requestitems.RequestFilesDict', lambda: 'mock_files')
    monkeypatch.setattr('httpie.cli.requestitems.RequestQueryParamsDict', lambda: 'mock_params')
    monkeypatch.setattr('httpie.cli.requestitems.MultipartRequestDataDict', lambda: 'mock_multipart_data')

    request_items = RequestItems(as_form=False)

    assert request_items.headers == 'mock_headers'
    assert request_items.data == 'mock_json_data'
    assert request_items.files == 'mock_files'
    assert request_items.params == 'mock_params'
    assert request_items.multipart_data == 'mock_multipart_data'
