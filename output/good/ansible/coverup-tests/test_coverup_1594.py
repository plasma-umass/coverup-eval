# file lib/ansible/utils/py3compat.py:24-66
# lines [40, 49, 50, 53, 54, 55, 56]
# branches ['37->40', '49->50', '49->53', '53->54', '53->56']

import os
import sys
import pytest
from ansible.utils.py3compat import _TextEnviron, to_text, to_bytes

# Assuming PY3 is a constant defined in the ansible.utils.py3compat module
# If it's not, you would need to determine the Python version using sys.version_info
PY3 = sys.version_info[0] == 3

@pytest.fixture
def mock_env(mocker):
    return mocker.patch.dict(os.environ, {'TEST_ENV_VAR': 'test_value'}, clear=True)

@pytest.fixture
def mock_getfilesystemencoding(mocker):
    mocker.patch('sys.getfilesystemencoding', return_value='utf-8')

def test_text_environ_encoding_none(mock_env, mock_getfilesystemencoding):
    # Create an instance of _TextEnviron with the default encoding
    text_environ = _TextEnviron()
    assert text_environ.encoding == sys.getfilesystemencoding()

def test_text_environ_encoding_provided(mock_env, mock_getfilesystemencoding):
    # Create an instance of _TextEnviron with a provided encoding
    custom_encoding = 'ascii'
    text_environ = _TextEnviron(encoding=custom_encoding)
    assert text_environ.encoding == custom_encoding

def test_text_environ_getitem_non_py3(mock_env, mock_getfilesystemencoding):
    if PY3:
        pytest.skip("This test is not relevant in a Python 3 environment")

    # Create an instance of _TextEnviron with the mocked environment
    text_environ = _TextEnviron()

    # Access the environment variable to trigger the caching mechanism
    cached_value = text_environ['TEST_ENV_VAR']
    assert cached_value == to_text(b'test_value', encoding='utf-8')

    # Access the environment variable again to hit the cache
    cached_value_again = text_environ['TEST_ENV_VAR']
    assert cached_value_again == cached_value

    # Test __setitem__
    text_environ['TEST_ENV_VAR'] = 'new_value'
    assert to_text(os.environ['TEST_ENV_VAR'], encoding='utf-8') == 'new_value'

    # Test __delitem__
    del text_environ['TEST_ENV_VAR']
    with pytest.raises(KeyError):
        _ = os.environ['TEST_ENV_VAR']

    # Test __iter__ and __len__
    assert 'TEST_ENV_VAR' in list(text_environ)
    assert len(text_environ) == len(os.environ)
