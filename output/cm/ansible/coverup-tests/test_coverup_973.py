# file lib/ansible/plugins/filter/core.py:460-461
# lines [460, 461]
# branches []

import pytest
import base64
from ansible.plugins.filter.core import b64encode
from ansible.module_utils._text import to_text, to_bytes

def test_b64encode():
    # Test with default encoding
    test_string = "Ansible Test String"
    expected_output = to_text(base64.b64encode(to_bytes(test_string)))
    assert b64encode(test_string) == expected_output

    # Test with different encoding
    test_string_unicode = "Ansible Test String – with unicode"
    expected_output_unicode = to_text(base64.b64encode(to_bytes(test_string_unicode, encoding='utf-8')))
    assert b64encode(test_string_unicode, encoding='utf-8') == expected_output_unicode

    # Clean up is not necessary as the function does not modify any external state
