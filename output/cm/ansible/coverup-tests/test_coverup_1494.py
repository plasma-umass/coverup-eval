# file lib/ansible/plugins/filter/core.py:464-465
# lines [465]
# branches []

import pytest
import base64
from ansible.plugins.filter.core import b64decode

def test_b64decode():
    # Prepare a base64 encoded string
    original_string = "Ansible Test String"
    encoded_string = base64.b64encode(original_string.encode('utf-8')).decode('utf-8')

    # Call the function that needs to be tested
    decoded_string = b64decode(encoded_string)

    # Assert that the decoded string matches the original string
    assert decoded_string == original_string

    # Test with a different encoding
    original_string_latin1 = "Ansible Test String".encode('latin1')
    encoded_string_latin1 = base64.b64encode(original_string_latin1).decode('utf-8')
    decoded_string_latin1 = b64decode(encoded_string_latin1, encoding='latin1')

    # Assert that the decoded string matches the original string with latin1 encoding
    assert decoded_string_latin1.encode('latin1') == original_string_latin1

    # Test with invalid input to cover the 'surrogate_or_strict' error handling
    with pytest.raises(Exception):
        invalid_encoded_string = encoded_string[:-1]  # Create an invalid base64 string
        b64decode(invalid_encoded_string)
