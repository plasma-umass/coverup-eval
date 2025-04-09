# file lib/ansible/utils/unsafe_proxy.py:105-106
# lines [105, 106]
# branches []

import pytest
from ansible.utils.unsafe_proxy import wrap_var

@pytest.fixture
def cleanup_wrap_var(mocker):
    # Assuming that wrap_var might have some global state or side effects,
    # we'll use a fixture to ensure that any mocking is undone after the test.
    # If wrap_var does not have side effects, this fixture might not be necessary.
    mocker.patch('ansible.utils.unsafe_proxy.wrap_var', side_effect=lambda x: x)
    yield
    mocker.stopall()

def test_wrap_dict(cleanup_wrap_var):
    # Test the _wrap_dict function to ensure it wraps keys and values correctly.
    from ansible.utils.unsafe_proxy import _wrap_dict

    test_dict = {'key1': 'value1', 'key2': 'value2'}
    expected_dict = {'key1': 'value1', 'key2': 'value2'}

    wrapped_dict = _wrap_dict(test_dict)

    assert wrapped_dict == expected_dict, "The wrapped dictionary does not match the expected dictionary"
    for key, value in wrapped_dict.items():
        assert isinstance(key, str), "The key should remain a string after wrapping"
        assert isinstance(value, str), "The value should remain a string after wrapping"
