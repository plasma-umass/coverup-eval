# file lib/ansible/utils/unsafe_proxy.py:86-102
# lines [88, 89, 90, 91, 97, 98, 100, 101, 102]
# branches ['97->98', '97->100', '100->101', '100->102']

import pytest
from ansible.utils.unsafe_proxy import UnsafeProxy
from ansible.module_utils._text import to_text
from ansible.utils.unsafe_proxy import AnsibleUnsafeText

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.utils.display.Display')

def test_unsafe_proxy_deprecation_warning(mock_display):
    test_string = "test"
    unsafe_proxy = UnsafeProxy(test_string)
    
    # Check that the deprecation warning was called
    mock_display().deprecated.assert_called_once_with(
        'UnsafeProxy is being deprecated. Use wrap_var or AnsibleUnsafeBytes/AnsibleUnsafeText directly instead',
        version='2.13', collection_name='ansible.builtin'
    )
    
    # Check that the object returned is an instance of AnsibleUnsafeText
    assert isinstance(unsafe_proxy, AnsibleUnsafeText)
    # Check that the value is correctly converted to text
    assert str(unsafe_proxy) == to_text(test_string, errors='surrogate_or_strict')
