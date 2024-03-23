# file lib/ansible/utils/py3compat.py:24-66
# lines [40, 45, 49, 50, 53, 54, 55, 56, 59, 60, 63, 66]
# branches ['31->33', '37->40', '49->50', '49->53', '53->54', '53->56']

import os
import pytest
import sys
from ansible.utils.py3compat import _TextEnviron, PY3, to_text, to_bytes

# Mocking the to_text and to_bytes functions to ensure they are called
@pytest.fixture
def mock_to_text(mocker):
    return mocker.patch('ansible.utils.py3compat.to_text', side_effect=lambda x, **kwargs: x)

@pytest.fixture
def mock_to_bytes(mocker):
    return mocker.patch('ansible.utils.py3compat.to_bytes', side_effect=lambda x, **kwargs: x.encode())

def test_text_environ_full_coverage(mock_to_text, mock_to_bytes):
    # Set up a fake environment with byte strings
    fake_env = {'FAKE_ENV_VAR': b'fake_value'}
    # Create a _TextEnviron instance with the fake environment
    text_env = _TextEnviron(env=fake_env, encoding='utf-8')

    # Test __delitem__
    text_env.__delitem__('FAKE_ENV_VAR')
    assert 'FAKE_ENV_VAR' not in fake_env

    # Reset fake environment
    fake_env['FAKE_ENV_VAR'] = b'fake_value'

    # Test __getitem__ for Python 2
    if not PY3:
        value = text_env.__getitem__('FAKE_ENV_VAR')
        assert value == 'fake_value'
        # Verify that the value is cached
        assert fake_env['FAKE_ENV_VAR'] in text_env._value_cache

    # Test __setitem__
    text_env.__setitem__('FAKE_ENV_VAR', 'new_fake_value')
    assert fake_env['FAKE_ENV_VAR'] == b'new_fake_value'

    # Test __iter__
    assert list(text_env.__iter__()) == list(fake_env.keys())

    # Test __len__
    assert text_env.__len__() == len(fake_env)

    # Verify that to_text and to_bytes were called
    if not PY3:
        mock_to_text.assert_called_with(b'fake_value', encoding='utf-8', nonstring='passthru', errors='surrogate_or_strict')
    mock_to_bytes.assert_called_with('new_fake_value', encoding='utf-8', nonstring='strict', errors='surrogate_or_strict')
