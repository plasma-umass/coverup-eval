# file sanic/response.py:499-524
# lines [499, 501, 502, 503, 514, 517, 520, 522, 523]
# branches []

import pytest
from sanic.response import HTTPResponse, redirect
from urllib.parse import quote_plus

def test_redirect():
    # Test with default parameters
    response = redirect('/test')
    assert response.status == 302
    assert response.headers['Location'] == '/test'
    assert response.content_type == "text/html; charset=utf-8"

    # Test with custom status
    response = redirect('/test', status=301)
    assert response.status == 301

    # Test with custom headers
    custom_headers = {'X-Custom-Header': 'Value'}
    response = redirect('/test', headers=custom_headers)
    assert response.headers['X-Custom-Header'] == 'Value'

    # Test with characters that need to be quoted in the URL
    response = redirect('/test redirect?param=value')
    quoted_url = quote_plus('/test redirect?param=value', safe=":/%#?&=@[]!$&'()*+,;")
    assert response.headers['Location'] == quoted_url

    # Test with custom content type
    response = redirect('/test', content_type='application/json')
    assert response.content_type == 'application/json'

    # Clean up is not necessary as the redirect function does not modify any global state
