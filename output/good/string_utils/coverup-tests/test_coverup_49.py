# file string_utils/validation.py:434-448
# lines [448]
# branches []

import pytest
from string_utils.validation import is_ip

def test_is_ip_v4_and_v6(mocker):
    # Mock the is_ip_v4 and is_ip_v6 functions to control their behavior
    mock_is_ip_v4 = mocker.patch('string_utils.validation.is_ip_v4', return_value=False)
    mock_is_ip_v6 = mocker.patch('string_utils.validation.is_ip_v6', return_value=False)

    # Test with a string that is neither a valid IPv4 nor a valid IPv6 address
    assert not is_ip('invalid_ip')

    # Test with a string that is a valid IPv4 address
    mock_is_ip_v4.return_value = True
    assert is_ip('255.200.100.75')

    # Test with a string that is a valid IPv6 address
    mock_is_ip_v6.return_value = True
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334')

    # Verify that the mocks were called
    mock_is_ip_v4.assert_called()
    mock_is_ip_v6.assert_called()
