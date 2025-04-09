# file lib/ansible/module_utils/urls.py:767-850
# lines [785, 800, 805, 810, 822, 827, 831, 836, 840]
# branches ['782->788', '784->785', '799->800', '801->805', '802->807', '820->822', '830->831', '835->836', '839->840']

import pytest
import urllib.request as urllib_request
import urllib.error as urllib_error
from unittest import mock

# Assuming the RedirectHandlerFactory is imported from ansible.module_utils.urls
from ansible.module_utils.urls import RedirectHandlerFactory

@pytest.fixture
def mock_opener(mocker):
    mock_opener = mocker.patch('urllib.request._opener')
    mock_opener.add_handler = mocker.Mock()
    return mock_opener

@pytest.fixture
def mock_sslcontext(mocker):
    mocker.patch('ansible.module_utils.urls.HAS_SSLCONTEXT', False)

@pytest.fixture
def mock_maybe_add_ssl_handler(mocker):
    return mocker.patch('ansible.module_utils.urls.maybe_add_ssl_handler', return_value=None)

def test_redirect_handler_no_sslcontext(mock_opener, mock_sslcontext, mock_maybe_add_ssl_handler):
    handler = RedirectHandlerFactory(follow_redirects='urllib2', validate_certs=True, ca_path=None)()
    req = mock.Mock()
    req.get_method.return_value = 'GET'
    req.get_full_url.return_value = 'http://example.com'
    req.headers = {'Content-Type': 'application/json'}
    req.get_data.return_value = b'data'
    req.get_origin_req_host.return_value = 'example.com'
    
    fp = mock.Mock()
    hdrs = {}
    newurl = 'http://example.com/redirect'
    
    # Test follow_redirects='urllib2'
    result = handler.redirect_request(req, fp, 301, 'Moved Permanently', hdrs, newurl)
    assert result.get_full_url() == newurl
    
    # Test follow_redirects='no'
    handler = RedirectHandlerFactory(follow_redirects='no', validate_certs=True, ca_path=None)()
    with pytest.raises(urllib_error.HTTPError):
        handler.redirect_request(req, fp, 301, 'Moved Permanently', hdrs, newurl)
    
    # Test follow_redirects='all'
    handler = RedirectHandlerFactory(follow_redirects='all', validate_certs=True, ca_path=None)()
    with pytest.raises(urllib_error.HTTPError):
        handler.redirect_request(req, fp, 200, 'OK', hdrs, newurl)
    
    # Test follow_redirects='safe'
    handler = RedirectHandlerFactory(follow_redirects='safe', validate_certs=True, ca_path=None)()
    with pytest.raises(urllib_error.HTTPError):
        handler.redirect_request(req, fp, 200, 'OK', hdrs, newurl)
    
    # Test follow_redirects='invalid'
    handler = RedirectHandlerFactory(follow_redirects='invalid', validate_certs=True, ca_path=None)()
    with pytest.raises(urllib_error.HTTPError):
        handler.redirect_request(req, fp, 301, 'Moved Permanently', hdrs, newurl)
    
    # Test follow_redirects='all' with 307 status code
    handler = RedirectHandlerFactory(follow_redirects='all', validate_certs=True, ca_path=None)()
    req.get_method.return_value = 'POST'
    req.data = b'data'
    req.origin_req_host = 'example.com'
    result = handler.redirect_request(req, fp, 307, 'Temporary Redirect', hdrs, newurl)
    assert result.get_method() == 'POST'
    assert {k.lower(): v for k, v in result.headers.items()} == {k.lower(): v for k, v in req.headers.items()}
    assert result.data == req.data
    
    # Test follow_redirects='all' with 303 status code
    result = handler.redirect_request(req, fp, 303, 'See Other', hdrs, newurl)
    assert result.get_method() == 'GET'
    
    # Test follow_redirects='all' with 302 status code
    result = handler.redirect_request(req, fp, 302, 'Found', hdrs, newurl)
    assert result.get_method() == 'GET'
    
    # Test follow_redirects='all' with 301 status code
    result = handler.redirect_request(req, fp, 301, 'Moved Permanently', hdrs, newurl)
    assert result.get_method() == 'GET'
