# file: lib/ansible/module_utils/urls.py:767-850
# asked: {"lines": [774, 775, 781, 782, 783, 784, 785, 788, 789, 792, 793, 795, 798, 799, 800, 801, 802, 803, 805, 807, 809, 810, 811, 813, 814, 817, 820, 822, 825, 826, 827, 830, 831, 835, 836, 839, 840, 842, 843, 844, 845, 846, 847, 850], "branches": [[782, 783], [782, 788], [784, 785], [784, 788], [788, 789], [788, 792], [792, 793], [792, 795], [798, 799], [798, 801], [799, 800], [799, 807], [801, 802], [801, 805], [802, 803], [802, 807], [820, 822], [820, 825], [830, 831], [830, 835], [835, 836], [835, 839], [839, 840], [839, 842]]}
# gained: {"lines": [774, 775, 781, 782, 788, 789, 792, 793, 795, 798, 799, 800, 801, 802, 803, 807, 809, 810, 817, 820, 822, 825, 826, 827, 830, 831, 835, 836, 839, 840, 842, 843, 844, 845, 846, 847, 850], "branches": [[782, 788], [788, 789], [788, 792], [792, 793], [792, 795], [798, 799], [798, 801], [799, 800], [799, 807], [801, 802], [802, 803], [820, 822], [820, 825], [830, 831], [830, 835], [835, 836], [835, 839], [839, 840], [839, 842]]}

import pytest
import urllib.request as urllib_request
import urllib.error as urllib_error
from ansible.module_utils.urls import RedirectHandlerFactory

@pytest.fixture
def mock_request(mocker):
    req = mocker.Mock()
    req.get_method.return_value = 'GET'
    req.get_full_url.return_value = 'http://example.com'
    req.get_data.return_value = None
    req.get_origin_req_host.return_value = 'example.com'
    req.headers = {'Content-Type': 'application/json'}
    return req

@pytest.fixture
def mock_response(mocker):
    fp = mocker.Mock()
    return fp

@pytest.fixture
def mock_headers():
    return {'Location': 'http://example.com/redirect'}

@pytest.fixture
def mock_newurl():
    return 'http://example.com/redirect'

def test_redirect_handler_urllib2(mocker, mock_request, mock_response, mock_headers, mock_newurl):
    handler = RedirectHandlerFactory(follow_redirects='urllib2')()
    result = handler.redirect_request(mock_request, mock_response, 302, 'Found', mock_headers, mock_newurl)
    assert result.get_full_url() == mock_newurl

def test_redirect_handler_no_redirect(mocker, mock_request, mock_response, mock_headers, mock_newurl):
    handler = RedirectHandlerFactory(follow_redirects='no')()
    with pytest.raises(urllib_error.HTTPError):
        handler.redirect_request(mock_request, mock_response, 302, 'Found', mock_headers, mock_newurl)

def test_redirect_handler_all_redirect(mocker, mock_request, mock_response, mock_headers, mock_newurl):
    handler = RedirectHandlerFactory(follow_redirects='all')()
    with pytest.raises(urllib_error.HTTPError):
        handler.redirect_request(mock_request, mock_response, 200, 'OK', mock_headers, mock_newurl)

def test_redirect_handler_safe_redirect(mocker, mock_request, mock_response, mock_headers, mock_newurl):
    handler = RedirectHandlerFactory(follow_redirects='safe')()
    with pytest.raises(urllib_error.HTTPError):
        handler.redirect_request(mock_request, mock_response, 200, 'OK', mock_headers, mock_newurl)

def test_redirect_handler_307_redirect(mocker, mock_request, mock_response, mock_headers, mock_newurl):
    handler = RedirectHandlerFactory(follow_redirects='all')()
    mock_request.get_method.return_value = 'POST'
    result = handler.redirect_request(mock_request, mock_response, 307, 'Temporary Redirect', mock_headers, mock_newurl)
    assert result.get_full_url() == mock_newurl
    assert result.get_method() == 'POST'

def test_redirect_handler_303_redirect(mocker, mock_request, mock_response, mock_headers, mock_newurl):
    handler = RedirectHandlerFactory(follow_redirects='all')()
    mock_request.get_method.return_value = 'POST'
    result = handler.redirect_request(mock_request, mock_response, 303, 'See Other', mock_headers, mock_newurl)
    assert result.get_full_url() == mock_newurl
    assert result.get_method() == 'GET'

def test_redirect_handler_302_redirect(mocker, mock_request, mock_response, mock_headers, mock_newurl):
    handler = RedirectHandlerFactory(follow_redirects='all')()
    mock_request.get_method.return_value = 'POST'
    result = handler.redirect_request(mock_request, mock_response, 302, 'Found', mock_headers, mock_newurl)
    assert result.get_full_url() == mock_newurl
    assert result.get_method() == 'GET'

def test_redirect_handler_301_redirect(mocker, mock_request, mock_response, mock_headers, mock_newurl):
    handler = RedirectHandlerFactory(follow_redirects='all')()
    mock_request.get_method.return_value = 'POST'
    result = handler.redirect_request(mock_request, mock_response, 301, 'Moved Permanently', mock_headers, mock_newurl)
    assert result.get_full_url() == mock_newurl
    assert result.get_method() == 'GET'
