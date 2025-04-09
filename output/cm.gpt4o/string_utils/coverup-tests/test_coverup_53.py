# file string_utils/validation.py:393-415
# lines [407, 408, 411, 412, 413, 415]
# branches ['407->408', '407->411', '411->412', '411->415', '412->411', '412->413']

import pytest
from string_utils.validation import is_ip_v4
import string_utils.validation

def test_is_ip_v4_invalid_string(mocker):
    # Mocking is_full_string to return False to hit line 407
    mocker.patch('string_utils.validation.is_full_string', return_value=False)
    assert not is_ip_v4('invalid_string')

def test_is_ip_v4_no_match(mocker):
    # Mocking is_full_string to return True to proceed to regex match
    mocker.patch('string_utils.validation.is_full_string', return_value=True)
    # Mocking SHALLOW_IP_V4_RE.match to return None to hit line 407
    mocker.patch('string_utils.validation.SHALLOW_IP_V4_RE', new_callable=mocker.Mock)
    string_utils.validation.SHALLOW_IP_V4_RE.match.return_value = None
    assert not is_ip_v4('invalid_string')

def test_is_ip_v4_out_of_range():
    # This should hit the range check and return False
    assert not is_ip_v4('255.200.100.999')

def test_is_ip_v4_valid():
    # This should be a valid IP and return True
    assert is_ip_v4('255.200.100.75')
