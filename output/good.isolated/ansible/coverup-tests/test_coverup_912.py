# file lib/ansible/plugins/filter/urls.py:26-27
# lines [26, 27]
# branches []

import pytest
from ansible.plugins.filter.urls import do_urldecode

def test_do_urldecode():
    # Test with a string that needs url decoding
    encoded_str = 'hello%20world'
    expected_decoded_str = 'hello world'
    assert do_urldecode(encoded_str) == expected_decoded_str

    # Test with a string that does not need url decoding
    plain_str = 'hello_world'
    assert do_urldecode(plain_str) == plain_str

    # Test with a string that includes plus sign
    encoded_str_with_plus = 'hello+world'
    expected_decoded_str_with_plus = 'hello world'
    assert do_urldecode(encoded_str_with_plus) == expected_decoded_str_with_plus

    # Test with a string that includes special characters
    encoded_str_special_chars = 'hello%21%40%23'
    expected_decoded_str_special_chars = 'hello!@#'
    assert do_urldecode(encoded_str_special_chars) == expected_decoded_str_special_chars

    # Test with a string that includes utf-8 characters
    encoded_str_utf8 = 'hello%20world%20%E2%9C%93'
    expected_decoded_str_utf8 = 'hello world ✓'
    assert do_urldecode(encoded_str_utf8) == expected_decoded_str_utf8

    # Test with an empty string
    assert do_urldecode('') == ''
