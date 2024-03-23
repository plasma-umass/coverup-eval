# file lib/ansible/utils/unsafe_proxy.py:109-114
# lines [109, 113, 114]
# branches []

import pytest
from ansible.utils.unsafe_proxy import wrap_var, AnsibleUnsafeText

@pytest.fixture
def cleanup_unsafe_wrappers(mocker):
    # Setup: store original state
    original_wrap_var = wrap_var
    yield
    # Teardown: restore original state
    mocker.stopall()

def test_wrap_sequence(cleanup_unsafe_wrappers, mocker):
    # Mock the wrap_var function to return an AnsibleUnsafeText instance
    mocker.patch('ansible.utils.unsafe_proxy.wrap_var', return_value=AnsibleUnsafeText("unsafe"))

    from ansible.utils.unsafe_proxy import _wrap_sequence

    # Create a list and tuple to test the wrapping
    test_list = [1, 2, 3]
    test_tuple = (1, 2, 3)

    # Wrap the list and tuple
    wrapped_list = _wrap_sequence(test_list)
    wrapped_tuple = _wrap_sequence(test_tuple)

    # Assert that the returned types match the input types
    assert isinstance(wrapped_list, list)
    assert isinstance(wrapped_tuple, tuple)

    # Assert that all items in the wrapped list and tuple are instances of AnsibleUnsafeText
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in wrapped_tuple)
