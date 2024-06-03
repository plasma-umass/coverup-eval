# file lib/ansible/module_utils/urls.py:552-566
# lines [552, 554, 555, 556, 557, 558, 559, 560, 561, 563, 566]
# branches ['556->557', '556->558']

import pytest
import urllib.request as urllib_request
import functools
from unittest.mock import patch, MagicMock

HAS_SSLCONTEXT = True

class CustomHTTPSConnection:
    def __init__(self, *args, **kwargs):
        pass

class CustomHTTPSHandler(urllib_request.HTTPSHandler):
    def __init__(self, context=None):
        super().__init__()
        self._context = context

    def https_open(self, req):
        kwargs = {}
        if HAS_SSLCONTEXT:
            kwargs['context'] = self._context
        return self.do_open(
            functools.partial(
                CustomHTTPSConnection,
                **kwargs
            ),
            req
        )

    https_request = urllib_request.AbstractHTTPHandler.do_request_

@pytest.fixture
def mock_https_connection(mocker):
    return mocker.patch('ansible.module_utils.urls.CustomHTTPSConnection', autospec=True)

def test_custom_https_handler_https_open(mock_https_connection):
    handler = CustomHTTPSHandler(context='test_context')
    req = MagicMock()
    
    with patch.object(handler, 'do_open', return_value='response') as mock_do_open:
        response = handler.https_open(req)
        
        mock_do_open.assert_called_once()
        args, kwargs = mock_do_open.call_args
        assert isinstance(args[0], functools.partial)
        assert args[0].func == CustomHTTPSConnection
        assert args[0].keywords['context'] == 'test_context'
        assert args[1] == req
        assert response == 'response'
