# file: lib/ansible/module_utils/urls.py:767-850
# asked: {"lines": [774, 775, 781, 782, 783, 784, 785, 788, 789, 792, 793, 795, 798, 799, 800, 801, 802, 803, 805, 807, 809, 810, 811, 813, 814, 817, 820, 822, 825, 826, 827, 830, 831, 835, 836, 839, 840, 842, 843, 844, 845, 846, 847, 850], "branches": [[782, 783], [782, 788], [784, 785], [784, 788], [788, 789], [788, 792], [792, 793], [792, 795], [798, 799], [798, 801], [799, 800], [799, 807], [801, 802], [801, 805], [802, 803], [802, 807], [820, 822], [820, 825], [830, 831], [830, 835], [835, 836], [835, 839], [839, 840], [839, 842]]}
# gained: {"lines": [774, 775, 781, 782, 788, 789, 792, 793, 795, 798, 799, 800, 801, 802, 803, 807, 809, 810, 817, 820, 822, 825, 826, 830, 835, 839, 842, 843, 844, 845, 846, 847, 850], "branches": [[782, 788], [788, 789], [788, 792], [792, 793], [792, 795], [798, 799], [798, 801], [799, 800], [799, 807], [801, 802], [802, 803], [820, 822], [820, 825], [830, 835], [835, 839], [839, 842]]}

import pytest
import ansible.module_utils.six.moves.urllib.request as urllib_request
import ansible.module_utils.six.moves.urllib.error as urllib_error
from ansible.module_utils.urls import RedirectHandlerFactory

class MockRequest(urllib_request.Request):
    def __init__(self, url, method='GET', data=None, headers=None):
        super(MockRequest, self).__init__(url, data, headers or {})
        self._method = method

    def get_method(self):
        return self._method

    def get_data(self):
        return self.data

    def get_origin_req_host(self):
        return self.origin_req_host

@pytest.fixture
def mock_response():
    class MockResponse:
        def __init__(self, code, msg, headers):
            self.code = code
            self.msg = msg
            self.headers = headers
    return MockResponse

def test_redirect_handler_urllib2(monkeypatch):
    def mock_redirect_request(self, req, fp, code, msg, hdrs, newurl):
        return 'redirected'
    
    monkeypatch.setattr(urllib_request.HTTPRedirectHandler, 'redirect_request', mock_redirect_request)
    
    handler = RedirectHandlerFactory(follow_redirects='urllib2')()
    req = MockRequest('http://example.com')
    resp = handler.redirect_request(req, None, 301, 'Moved Permanently', {}, 'http://example.com/new')
    
    assert resp == 'redirected'

def test_redirect_handler_no_redirects():
    handler = RedirectHandlerFactory(follow_redirects='no')()
    req = MockRequest('http://example.com')
    
    with pytest.raises(urllib_error.HTTPError):
        handler.redirect_request(req, None, 301, 'Moved Permanently', {}, 'http://example.com/new')

def test_redirect_handler_all_redirects():
    handler = RedirectHandlerFactory(follow_redirects='all')()
    req = MockRequest('http://example.com')
    
    with pytest.raises(urllib_error.HTTPError):
        handler.redirect_request(req, None, 200, 'OK', {}, 'http://example.com/new')

def test_redirect_handler_safe_redirects():
    handler = RedirectHandlerFactory(follow_redirects='safe')()
    req = MockRequest('http://example.com', method='POST')
    
    with pytest.raises(urllib_error.HTTPError):
        handler.redirect_request(req, None, 301, 'Moved Permanently', {}, 'http://example.com/new')

def test_redirect_handler_preserve_payload():
    handler = RedirectHandlerFactory(follow_redirects='all')()
    req = MockRequest('http://example.com', data=b'data')
    
    new_req = handler.redirect_request(req, None, 307, 'Temporary Redirect', {}, 'http://example.com/new')
    
    assert new_req.data == b'data'
    assert new_req.get_method() == 'GET'

def test_redirect_handler_replace_spaces():
    handler = RedirectHandlerFactory(follow_redirects='all')()
    req = MockRequest('http://example.com')
    
    new_req = handler.redirect_request(req, None, 301, 'Moved Permanently', {}, 'http://example.com/new path')
    
    assert new_req.full_url == 'http://example.com/new%20path'
