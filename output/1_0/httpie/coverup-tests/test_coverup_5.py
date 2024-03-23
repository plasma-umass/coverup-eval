# file httpie/cli/dicts.py:6-10
# lines [6, 7]
# branches []

import pytest
from httpie.cli.dicts import RequestHeadersDict

def test_request_headers_dict_case_insensitivity():
    headers = RequestHeadersDict()
    headers['Content-Type'] = 'application/json'
    headers['content-type'] = 'text/html'

    assert headers['Content-Type'] == 'text/html'
    assert headers['CONTENT-TYPE'] == 'text/html'
    assert headers['content-type'] == 'text/html'

    headers['ACCEPT'] = 'application/xml'
    assert headers['accept'] == 'application/xml'
    assert headers['Accept'] == 'application/xml'

    # Clean up is not necessary as the headers dictionary is local to the test function
