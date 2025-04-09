# file lib/ansible/module_utils/urls.py:748-764
# lines [748, 749, 754, 755, 756, 757, 758, 760, 761, 762, 764]
# branches ['755->756', '755->757', '761->762', '761->764']

import pytest
from unittest import mock
from urllib import request as urllib_request

# Import the class from the module
from ansible.module_utils.urls import RequestWithMethod

def test_request_with_method_get():
    url = 'http://example.com'
    method = 'GET'
    req = RequestWithMethod(url, method)
    assert req.get_method() == 'GET'

def test_request_with_method_post():
    url = 'http://example.com'
    method = 'POST'
    data = b'some data'
    req = RequestWithMethod(url, method, data=data)
    assert req.get_method() == 'POST'
    assert req.data == data

def test_request_with_method_put():
    url = 'http://example.com'
    method = 'PUT'
    req = RequestWithMethod(url, method)
    assert req.get_method() == 'PUT'

def test_request_with_method_delete():
    url = 'http://example.com'
    method = 'DELETE'
    req = RequestWithMethod(url, method)
    assert req.get_method() == 'DELETE'

def test_request_with_method_default():
    url = 'http://example.com'
    method = 'GET'  # Use a default method to avoid the AttributeError
    req = RequestWithMethod(url, method)
    with mock.patch.object(urllib_request.Request, 'get_method', return_value='GET') as mock_get_method:
        req._method = None  # Set _method to None to test the default behavior
        assert req.get_method() == 'GET'
        mock_get_method.assert_called_once()

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
