# file: httpie/client.py:181-194
# asked: {"lines": [181, 182, 183, 184, 189, 190, 192, 193, 194], "branches": [[183, 184], [183, 194], [184, 189], [184, 193], [190, 192], [190, 193]]}
# gained: {"lines": [181, 182, 183, 184, 189, 190, 192, 193, 194], "branches": [[183, 184], [183, 194], [184, 189], [184, 193], [190, 192]]}

import pytest
from httpie.client import finalize_headers
from httpie.cli.dicts import RequestHeadersDict

def test_finalize_headers():
    headers = RequestHeadersDict({
        'Content-Type': ' application/json ',
        'Accept': 'text/html',
        'Authorization': None,
        'User-Agent': 'httpie'
    })

    expected_headers = RequestHeadersDict({
        'Content-Type': b'application/json',
        'Accept': b'text/html',
        'User-Agent': b'httpie'
    })

    result = finalize_headers(headers)
    for key in expected_headers:
        assert result[key] == expected_headers[key]
