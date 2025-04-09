# file lib/ansible/utils/unsafe_proxy.py:86-102
# lines [88, 89, 90, 91, 97, 98, 100, 101, 102]
# branches ['97->98', '97->100', '100->101', '100->102']

import pytest
from unittest.mock import patch
from ansible.utils.unsafe_proxy import UnsafeProxy
from ansible.utils.unsafe_proxy import AnsibleUnsafeText
from ansible.utils.unsafe_proxy import AnsibleUnsafe
from ansible.module_utils.six import string_types

def test_unsafe_proxy_deprecated_message(mocker):
    # Mock the Display class and its deprecated method
    mock_display = mocker.patch('ansible.utils.display.Display')
    mock_deprecated = mock_display.return_value.deprecated

    # Test with an instance of AnsibleUnsafe
    unsafe_obj = AnsibleUnsafeText("unsafe text")
    result = UnsafeProxy(unsafe_obj)
    assert result is unsafe_obj

    # Ensure the deprecated method was called once
    mock_deprecated.assert_called_once_with(
        'UnsafeProxy is being deprecated. Use wrap_var or AnsibleUnsafeBytes/AnsibleUnsafeText directly instead',
        version='2.13', collection_name='ansible.builtin'
    )
    mock_deprecated.reset_mock()

    # Test with a string type
    test_string = "test string"
    result = UnsafeProxy(test_string)
    assert isinstance(result, AnsibleUnsafeText)
    assert result == "test string"

    # Ensure the deprecated method was called once again
    mock_deprecated.assert_called_once_with(
        'UnsafeProxy is being deprecated. Use wrap_var or AnsibleUnsafeBytes/AnsibleUnsafeText directly instead',
        version='2.13', collection_name='ansible.builtin'
    )
