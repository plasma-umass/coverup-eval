# file: httpie/client.py:181-194
# asked: {"lines": [182, 183, 184, 189, 190, 192, 193, 194], "branches": [[183, 184], [183, 194], [184, 189], [184, 193], [190, 192], [190, 193]]}
# gained: {"lines": [182, 183, 184, 189, 190, 192, 193, 194], "branches": [[183, 184], [183, 194], [184, 189], [184, 193], [190, 192]]}

import pytest
from httpie.client import finalize_headers
from httpie.cli.dicts import RequestHeadersDict

def test_finalize_headers_all_none():
    headers = RequestHeadersDict({
        'Header1': None,
        'Header2': None
    })
    final_headers = finalize_headers(headers)
    assert final_headers == {'Header1': None, 'Header2': None}

def test_finalize_headers_strip_and_encode():
    headers = RequestHeadersDict({
        'Header1': '  value1  ',
        'Header2': 'value2'
    })
    final_headers = finalize_headers(headers)
    assert final_headers == {
        'Header1': b'value1',
        'Header2': b'value2'
    }

def test_finalize_headers_mixed():
    headers = RequestHeadersDict({
        'Header1': '  value1  ',
        'Header2': None,
        'Header3': 'value3'
    })
    final_headers = finalize_headers(headers)
    assert final_headers == {
        'Header1': b'value1',
        'Header2': None,
        'Header3': b'value3'
    }
