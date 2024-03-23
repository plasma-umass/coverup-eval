# file lib/ansible/plugins/filter/urls.py:20-23
# lines [20, 21, 22, 23]
# branches ['21->22', '21->23']

import pytest
from ansible.plugins.filter.urls import unicode_urldecode
from ansible.module_utils.six import PY3

# Test function for unicode_urldecode
def test_unicode_urldecode():
    # Setup: Define a string that needs url decoding
    encoded_string = 'hello%20world%21'
    expected_decoded = 'hello world!'

    # Exercise: Call the function with the encoded string
    decoded_string = unicode_urldecode(encoded_string)

    # Verify: Check if the decoded string matches the expected result
    assert decoded_string == expected_decoded

    # Cleanup: No cleanup required for this test as it does not affect external state
