# file: httpie/cli/dicts.py:6-10
# asked: {"lines": [6, 7], "branches": []}
# gained: {"lines": [6, 7], "branches": []}

import pytest
from requests.structures import CaseInsensitiveDict
from httpie.cli.dicts import RequestHeadersDict

def test_request_headers_dict_inheritance():
    headers = RequestHeadersDict()
    assert isinstance(headers, CaseInsensitiveDict)

def test_request_headers_dict_case_insensitivity():
    headers = RequestHeadersDict()
    headers['Content-Type'] = 'application/json'
    assert headers['content-type'] == 'application/json'
    assert headers['CONTENT-TYPE'] == 'application/json'

def test_request_headers_dict_multiple_values_not_supported():
    headers = RequestHeadersDict()
    headers['Accept'] = 'application/json'
    headers['Accept'] = 'text/html'
    assert headers['Accept'] == 'text/html'
    assert len(headers) == 1
