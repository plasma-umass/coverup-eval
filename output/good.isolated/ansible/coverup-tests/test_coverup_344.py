# file lib/ansible/plugins/filter/core.py:113-124
# lines [113, 116, 118, 119, 120, 121, 122, 123, 124]
# branches ['119->120', '119->121', '121->122', '121->123']

import pytest
from ansible.plugins.filter.core import regex_replace

def test_regex_replace_ignorecase_and_multiline():
    # Test with ignorecase=True and multiline=True
    result = regex_replace(value='Example Text', pattern='^example', replacement='Test', ignorecase=True, multiline=True)
    assert result == 'Test Text', "The regex should replace 'Example' with 'Test' at the beginning of the string, case insensitive and considering each line."

    # Test with ignorecase=False and multiline=True
    result = regex_replace(value='Example Text\nexample text', pattern='^example', replacement='Test', ignorecase=False, multiline=True)
    assert result == 'Example Text\nTest text', "The regex should replace 'example' with 'Test' at the beginning of the second line only."

    # Test with ignorecase=True and multiline=False
    result = regex_replace(value='Example Text\nexample text', pattern='example', replacement='Test', ignorecase=True, multiline=False)
    assert result == 'Test Text\nTest text', "The regex should replace all occurrences of 'example' with 'Test', case insensitive."

    # Test with ignorecase=False and multiline=False
    result = regex_replace(value='Example Text\nexample text', pattern='example', replacement='Test', ignorecase=False, multiline=False)
    assert result == 'Example Text\nTest text', "The regex should replace 'example' with 'Test' only in the second line, case sensitive."
