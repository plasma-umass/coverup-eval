# file lib/ansible/plugins/filter/urls.py:42-55
# lines [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]
# branches ['44->45', '44->46', '46->47', '46->51', '51->52', '51->53']

import pytest
from ansible.plugins.filter.urls import do_urlencode
from ansible.module_utils.six import string_types

# Mocking iteritems for Python 3 compatibility
try:
    from ansible.module_utils.six.moves import iteritems
except ImportError:
    # Define a simple iteritems for testing purposes
    def iteritems(d):
        return iter(d.items())

# Mocking unicode_urlencode for testing purposes
def unicode_urlencode(value, for_qs=False):
    if isinstance(value, string_types):
        return value
    return str(value)

# Patching the original unicode_urlencode with the mock
@pytest.fixture
def mock_unicode_urlencode(mocker):
    mocker.patch('ansible.plugins.filter.urls.unicode_urlencode', side_effect=unicode_urlencode)

def test_do_urlencode_with_dict(mock_unicode_urlencode):
    # Test with a dictionary input
    input_value = {'key1': 'value1', 'key2': 'value2'}
    expected_output = 'key1=value1&key2=value2'
    assert do_urlencode(input_value) == expected_output

def test_do_urlencode_with_list(mock_unicode_urlencode):
    # Test with a list input
    input_value = [('key1', 'value1'), ('key2', 'value2')]
    expected_output = 'key1=value1&key2=value2'
    assert do_urlencode(input_value) == expected_output

def test_do_urlencode_with_unsupported_type(mock_unicode_urlencode):
    # Test with an unsupported type (not a dict or list/tuple)
    input_value = 12345
    expected_output = '12345'
    assert do_urlencode(input_value) == expected_output

def test_do_urlencode_with_string(mock_unicode_urlencode):
    # Test with a string input
    input_value = 'test_string'
    expected_output = 'test_string'
    assert do_urlencode(input_value) == expected_output
