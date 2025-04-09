# file: lib/ansible/module_utils/urls.py:767-850
# asked: {"lines": [767, 774, 775, 781, 782, 783, 784, 785, 788, 789, 792, 793, 795, 798, 799, 800, 801, 802, 803, 805, 807, 809, 810, 811, 813, 814, 817, 820, 822, 825, 826, 827, 830, 831, 835, 836, 839, 840, 842, 843, 844, 845, 846, 847, 850], "branches": [[782, 783], [782, 788], [784, 785], [784, 788], [788, 789], [788, 792], [792, 793], [792, 795], [798, 799], [798, 801], [799, 800], [799, 807], [801, 802], [801, 805], [802, 803], [802, 807], [820, 822], [820, 825], [830, 831], [830, 835], [835, 836], [835, 839], [839, 840], [839, 842]]}
# gained: {"lines": [767, 774, 775, 781, 782, 783, 784, 788, 789, 792, 793, 795, 798, 799, 800, 801, 802, 803, 807, 809, 810, 817, 820, 822, 825, 826, 830, 835, 836, 839, 840, 842, 843, 844, 845, 846, 847, 850], "branches": [[782, 783], [782, 788], [784, 788], [788, 789], [788, 792], [792, 793], [792, 795], [798, 799], [798, 801], [799, 800], [799, 807], [801, 802], [802, 803], [820, 822], [820, 825], [830, 835], [835, 836], [835, 839], [839, 840], [839, 842]]}

import pytest
from unittest import mock
from ansible.module_utils.urls import RedirectHandlerFactory, RequestWithMethod
from urllib import request as urllib_request
from urllib import error as urllib_error

@pytest.fixture
def mock_sslcontext(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.urls.HAS_SSLCONTEXT', True)

@pytest.fixture
def mock_no_sslcontext(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.urls.HAS_SSLCONTEXT', False)

def test_redirect_handler_urllib2(mock_sslcontext):
    handler = RedirectHandlerFactory(follow_redirects='urllib2')()
    req = mock.Mock()
    fp = mock.Mock()
    hdrs = mock.Mock()
    newurl = 'http://example.com'
    with mock.patch.object(urllib_request.HTTPRedirectHandler, 'redirect_request', return_value='redirected'):
        result = handler.redirect_request(req, fp, 301, 'Moved Permanently', hdrs, newurl)
    assert result == 'redirected'

def test_redirect_handler_no_redirect(mock_sslcontext):
    handler = RedirectHandlerFactory(follow_redirects='no')()
    req = mock.Mock()
    fp = mock.Mock()
    hdrs = mock.Mock()
    newurl = 'http://example.com'
    with pytest.raises(urllib_error.HTTPError):
        handler.redirect_request(req, fp, 301, 'Moved Permanently', hdrs, newurl)

def test_redirect_handler_all_redirect(mock_sslcontext):
    handler = RedirectHandlerFactory(follow_redirects='all')()
    req = mock.Mock()
    req.get_method.return_value = 'GET'
    req.get_full_url.return_value = 'http://example.com'
    req.headers = {}
    fp = mock.Mock()
    hdrs = mock.Mock()
    newurl = 'http://example.com'
    with pytest.raises(urllib_error.HTTPError):
        handler.redirect_request(req, fp, 200, 'OK', hdrs, newurl)

def test_redirect_handler_safe_redirect(mock_sslcontext):
    handler = RedirectHandlerFactory(follow_redirects='safe')()
    req = mock.Mock()
    req.get_method.return_value = 'POST'
    req.get_full_url.return_value = 'http://example.com'
    req.headers = {}
    fp = mock.Mock()
    hdrs = mock.Mock()
    newurl = 'http://example.com'
    with pytest.raises(urllib_error.HTTPError):
        handler.redirect_request(req, fp, 301, 'Moved Permanently', hdrs, newurl)

def test_redirect_handler_no_sslcontext(mock_no_sslcontext):
    handler = RedirectHandlerFactory(follow_redirects='all')()
    req = mock.Mock()
    req.get_method.return_value = 'GET'
    req.get_full_url.return_value = 'http://example.com'
    req.headers = {}
    fp = mock.Mock()
    hdrs = mock.Mock()
    newurl = 'http://example.com'
    with mock.patch('ansible.module_utils.urls.maybe_add_ssl_handler', return_value=None):
        with pytest.raises(urllib_error.HTTPError):
            handler.redirect_request(req, fp, 200, 'OK', hdrs, newurl)

def test_redirect_handler_307_308(mock_sslcontext):
    handler = RedirectHandlerFactory(follow_redirects='all')()
    req = mock.Mock()
    req.get_method.return_value = 'POST'
    req.get_full_url.return_value = 'http://example.com'
    req.headers = {'Content-Type': 'application/json'}
    req.get_data.return_value = b'{"key": "value"}'
    fp = mock.Mock()
    hdrs = mock.Mock()
    newurl = 'http://example.com'
    result = handler.redirect_request(req, fp, 307, 'Temporary Redirect', hdrs, newurl)
    assert result.get_method() == 'POST'
    assert result.headers['Content-type'] == req.headers['Content-Type']
    assert result.data == req.get_data()

def test_redirect_handler_302(mock_sslcontext):
    handler = RedirectHandlerFactory(follow_redirects='all')()
    req = mock.Mock()
    req.get_method.return_value = 'POST'
    req.get_full_url.return_value = 'http://example.com'
    req.headers = {}
    req.get_data.return_value = b'{"key": "value"}'
    fp = mock.Mock()
    hdrs = mock.Mock()
    newurl = 'http://example.com'
    result = handler.redirect_request(req, fp, 302, 'Found', hdrs, newurl)
    assert result.get_method() == 'GET'
    assert result.data is None

def test_redirect_handler_301(mock_sslcontext):
    handler = RedirectHandlerFactory(follow_redirects='all')()
    req = mock.Mock()
    req.get_method.return_value = 'POST'
    req.get_full_url.return_value = 'http://example.com'
    req.headers = {}
    req.get_data.return_value = b'{"key": "value"}'
    fp = mock.Mock()
    hdrs = mock.Mock()
    newurl = 'http://example.com'
    result = handler.redirect_request(req, fp, 301, 'Moved Permanently', hdrs, newurl)
    assert result.get_method() == 'GET'
    assert result.data is None
