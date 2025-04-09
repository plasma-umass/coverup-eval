# file string_utils/validation.py:393-415
# lines [393, 407, 408, 411, 412, 413, 415]
# branches ['407->408', '407->411', '411->412', '411->415', '412->411', '412->413']

import pytest
from string_utils.validation import is_ip_v4

def test_is_ip_v4():
    # Test valid IP
    assert is_ip_v4('255.200.100.75') == True

    # Test invalid IP (not an IP)
    assert is_ip_v4('nope') == False

    # Test invalid IP (out of range)
    assert is_ip_v4('255.200.100.999') == False

    # Test invalid IP (empty string)
    assert is_ip_v4('') == False

    # Test invalid IP (None)
    assert is_ip_v4(None) == False

    # Test invalid IP (integer input)
    assert is_ip_v4(123) == False

    # Test invalid IP (list input)
    assert is_ip_v4(['255', '200', '100', '75']) == False

    # Test invalid IP (missing parts)
    assert is_ip_v4('255.100.75') == False

    # Test invalid IP (extra parts)
    assert is_ip_v4('255.200.100.75.1') == False

    # Test invalid IP (negative number)
    assert is_ip_v4('255.200.-100.75') == False

    # Test invalid IP (leading zeros are actually allowed in IPv4, so this test should expect True)
    assert is_ip_v4('255.200.010.75') == True

    # Test invalid IP (space in the string)
    assert is_ip_v4('255.200.100. 75') == False

    # Test invalid IP (special characters)
    assert is_ip_v4('255.200.100.75#') == False

    # Test invalid IP (only dots)
    assert is_ip_v4('...') == False

    # Test invalid IP (empty parts)
    assert is_ip_v4('255..100.75') == False

    # Test invalid IP (alpha-numeric)
    assert is_ip_v4('255.20a.100.75') == False

# Note: The actual implementation of `is_full_string` and `SHALLOW_IP_V4_RE` is not provided.
# The tests assume that `is_full_string` checks if the input is a non-empty string and
# `SHALLOW_IP_V4_RE` is a regular expression that matches strings in the form of an IP address.
