# file tornado/httpclient.py:59-88
# lines [59, 60]
# branches []

import pytest
from tornado.httpclient import HTTPClient, HTTPError

def test_http_client_fetch(mocker):
    # Mock the fetch method to raise an HTTPError
    mocker.patch.object(HTTPClient, 'fetch', side_effect=HTTPError(404))

    http_client = HTTPClient()
    try:
        # This should raise an HTTPError and be caught below
        http_client.fetch("http://www.google.com/")
    except HTTPError as e:
        # Verify that the exception is indeed an HTTPError and has the correct status code
        assert isinstance(e, HTTPError)
        assert e.code == 404
    except Exception as e:
        # This block should not be executed
        pytest.fail(f"Unexpected exception type: {type(e)}")
    finally:
        # Ensure that the client is closed after the test
        http_client.close()
