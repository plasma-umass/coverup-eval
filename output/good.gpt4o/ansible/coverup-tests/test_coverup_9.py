# file lib/ansible/module_utils/urls.py:767-850
# lines [767, 774, 775, 781, 782, 783, 784, 785, 788, 789, 792, 793, 795, 798, 799, 800, 801, 802, 803, 805, 807, 809, 810, 811, 813, 814, 817, 820, 822, 825, 826, 827, 830, 831, 835, 836, 839, 840, 842, 843, 844, 845, 846, 847, 850]
# branches ['782->783', '782->788', '784->785', '784->788', '788->789', '788->792', '792->793', '792->795', '798->799', '798->801', '799->800', '799->807', '801->802', '801->805', '802->803', '802->807', '820->822', '820->825', '830->831', '830->835', '835->836', '835->839', '839->840', '839->842']

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

def test_redirect_handler_no_redirects(mock_opener, mock_sslcontext, mock_maybe_add_ssl_handler):
    follow_redirects = 'none'
    validate_certs = True
    ca_path = None

    RedirectHandler = RedirectHandlerFactory(follow_redirects, validate_certs, ca_path)
    handler = RedirectHandler()

    req = urllib_request.Request('http://example.com')
    fp = mock.Mock()
    code = 301
    msg = 'Moved Permanently'
    hdrs = {}
    newurl = 'http://example.com/new'

    with pytest.raises(urllib_error.HTTPError) as excinfo:
        handler.redirect_request(req, fp, code, msg, hdrs, newurl)
    assert excinfo.value.code == 301
    assert excinfo.value.filename == newurl

def test_redirect_handler_urllib2(mock_opener, mock_sslcontext, mock_maybe_add_ssl_handler):
    follow_redirects = 'urllib2'
    validate_certs = True
    ca_path = None

    RedirectHandler = RedirectHandlerFactory(follow_redirects, validate_certs, ca_path)
    handler = RedirectHandler()

    req = urllib_request.Request('http://example.com')
    fp = mock.Mock()
    code = 301
    msg = 'Moved Permanently'
    hdrs = {}
    newurl = 'http://example.com/new'

    result = handler.redirect_request(req, fp, code, msg, hdrs, newurl)
    assert isinstance(result, urllib_request.Request)
    assert result.full_url == newurl

def test_redirect_handler_safe_redirect(mock_opener, mock_sslcontext, mock_maybe_add_ssl_handler):
    follow_redirects = 'safe'
    validate_certs = True
    ca_path = None

    RedirectHandler = RedirectHandlerFactory(follow_redirects, validate_certs, ca_path)
    handler = RedirectHandler()

    req = urllib_request.Request('http://example.com', method='POST')
    fp = mock.Mock()
    code = 301
    msg = 'Moved Permanently'
    hdrs = {}
    newurl = 'http://example.com/new'

    with pytest.raises(urllib_error.HTTPError) as excinfo:
        handler.redirect_request(req, fp, code, msg, hdrs, newurl)
    assert excinfo.value.code == 301
    assert excinfo.value.filename == req.get_full_url()

def test_redirect_handler_all_redirects(mock_opener, mock_sslcontext, mock_maybe_add_ssl_handler):
    follow_redirects = 'all'
    validate_certs = True
    ca_path = None

    RedirectHandler = RedirectHandlerFactory(follow_redirects, validate_certs, ca_path)
    handler = RedirectHandler()

    req = urllib_request.Request('http://example.com')
    fp = mock.Mock()
    code = 301
    msg = 'Moved Permanently'
    hdrs = {}
    newurl = 'http://example.com/new'

    result = handler.redirect_request(req, fp, code, msg, hdrs, newurl)
    assert isinstance(result, urllib_request.Request)
    assert result.full_url == newurl
    assert result.get_method() == 'GET'
