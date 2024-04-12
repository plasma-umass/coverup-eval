# file lib/ansible/module_utils/urls.py:748-764
# lines [764]
# branches ['755->757', '761->764']

import pytest
from ansible.module_utils.urls import RequestWithMethod
from unittest.mock import patch

def test_request_with_method_get_method():
    # Test to cover line 764 and branch 755->757
    # Create an instance without headers to hit line 755
    req_without_headers = RequestWithMethod('http://example.com', 'GET')
    assert req_without_headers.get_method() == 'GET', "The method should be GET"

    # Create an instance with headers to bypass line 755
    req_with_headers = RequestWithMethod('http://example.com', 'GET', headers={'Content-Type': 'application/json'})
    assert req_with_headers.get_method() == 'GET', "The method should be GET"

    # Create an instance with a method that will trigger the else clause on line 761
    with patch('ansible.module_utils.urls.urllib_request.Request.get_method', return_value='POST'):
        req_with_post_method = RequestWithMethod('http://example.com', 'POST')
        assert req_with_post_method.get_method() == 'POST', "The method should be POST"
