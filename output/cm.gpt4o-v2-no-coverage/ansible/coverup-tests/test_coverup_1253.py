# file: lib/ansible/module_utils/urls.py:767-850
# asked: {"lines": [782, 783, 784, 785, 788, 789, 792, 793, 795, 798, 799, 800, 801, 802, 803, 805, 807, 809, 810, 811, 813, 814, 817, 820, 822, 825, 826, 827, 830, 831, 835, 836, 839, 840, 842, 843, 844, 845, 846, 847], "branches": [[782, 783], [782, 788], [784, 785], [784, 788], [788, 789], [788, 792], [792, 793], [792, 795], [798, 799], [798, 801], [799, 800], [799, 807], [801, 802], [801, 805], [802, 803], [802, 807], [820, 822], [820, 825], [830, 831], [830, 835], [835, 836], [835, 839], [839, 840], [839, 842]]}
# gained: {"lines": [782, 788, 789, 792, 793, 795, 798, 799, 801, 802, 803, 807, 809, 811, 813, 814, 817, 820, 825, 826, 830, 835, 836, 839, 840, 842, 843, 844, 845, 846, 847], "branches": [[782, 788], [788, 789], [788, 792], [792, 793], [792, 795], [798, 799], [798, 801], [799, 807], [801, 802], [802, 803], [820, 825], [830, 835], [835, 836], [835, 839], [839, 840], [839, 842]]}

import pytest
import ansible.module_utils.six.moves.urllib.request as urllib_request
import ansible.module_utils.six.moves.urllib.error as urllib_error
from ansible.module_utils.urls import RedirectHandlerFactory, RequestWithMethod

@pytest.fixture
def mock_opener(mocker):
    mocker.patch('ansible.module_utils.six.moves.urllib.request.build_opener', autospec=True)

@pytest.fixture
def mock_ssl_handler(mocker):
    return mocker.patch('ansible.module_utils.urls.maybe_add_ssl_handler', return_value=None)

@pytest.fixture
def mock_ssl_context(mocker):
    mocker.patch('ansible.module_utils.urls.HAS_SSLCONTEXT', True)

def test_redirect_handler_urllib2(mock_opener, mock_ssl_handler, mock_ssl_context):
    handler = RedirectHandlerFactory(follow_redirects='urllib2')()
    req = urllib_request.Request('http://example.com')
    fp = None
    code = 302
    msg = 'Found'
    hdrs = {}
    newurl = 'http://example.com/redirect'
    
    result = handler.redirect_request(req, fp, code, msg, hdrs, newurl)
    assert isinstance(result, urllib_request.Request)
    assert result.get_full_url() == newurl

def test_redirect_handler_no_redirect(mock_opener, mock_ssl_handler, mock_ssl_context):
    handler = RedirectHandlerFactory(follow_redirects='no')()
    req = urllib_request.Request('http://example.com')
    fp = None
    code = 302
    msg = 'Found'
    hdrs = {}
    newurl = 'http://example.com/redirect'
    
    with pytest.raises(urllib_error.HTTPError):
        handler.redirect_request(req, fp, code, msg, hdrs, newurl)

def test_redirect_handler_all(mock_opener, mock_ssl_handler, mock_ssl_context):
    handler = RedirectHandlerFactory(follow_redirects='all')()
    req = urllib_request.Request('http://example.com')
    fp = None
    code = 302
    msg = 'Found'
    hdrs = {}
    newurl = 'http://example.com/redirect'
    
    result = handler.redirect_request(req, fp, code, msg, hdrs, newurl)
    assert isinstance(result, RequestWithMethod)
    assert result.get_full_url() == newurl
    assert result.get_method() == 'GET'

def test_redirect_handler_safe(mock_opener, mock_ssl_handler, mock_ssl_context):
    handler = RedirectHandlerFactory(follow_redirects='safe')()
    req = urllib_request.Request('http://example.com', method='POST')
    fp = None
    code = 302
    msg = 'Found'
    hdrs = {}
    newurl = 'http://example.com/redirect'
    
    with pytest.raises(urllib_error.HTTPError):
        handler.redirect_request(req, fp, code, msg, hdrs, newurl)

def test_redirect_handler_post_to_get(mock_opener, mock_ssl_handler, mock_ssl_context):
    handler = RedirectHandlerFactory(follow_redirects='all')()
    req = urllib_request.Request('http://example.com', method='POST')
    fp = None
    code = 301
    msg = 'Moved Permanently'
    hdrs = {}
    newurl = 'http://example.com/redirect'
    
    result = handler.redirect_request(req, fp, code, msg, hdrs, newurl)
    assert isinstance(result, RequestWithMethod)
    assert result.get_full_url() == newurl
    assert result.get_method() == 'GET'
