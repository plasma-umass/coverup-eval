# file string_utils/validation.py:204-244
# lines [221, 229, 234, 238, 240, 242, 244]
# branches ['220->221', '228->229', '233->234', '240->242', '240->244']

import pytest
from string_utils.validation import is_email

def test_is_email_coverage():
    # Test for line 221
    assert not is_email('')  # Empty string
    assert not is_email('..start_with_dot@domain.com')  # Starts with dot
    assert not is_email('a' * 321)  # Length > 320

    # Test for line 229
    assert not is_email('local_part_too_long' + 'a' * 65 + '@domain.com')  # Local part > 64
    assert not is_email('local@' + 'a' * 256 + '.com')  # Domain part > 255
    assert not is_email('local..part@domain.com')  # Multiple consecutive dots in local part
    assert not is_email('local.@domain.com')  # Local part ends with dot

    # Test for line 234
    assert is_email('"local part"@domain.com')  # Local part with spaces and quotes

    # Test for line 238-244
    assert not is_email('local@domain@domain.com')  # Multiple @ signs without correct escaping
    assert is_email('local\\@domain@domain.com')  # Correctly escaped @ sign in local part
