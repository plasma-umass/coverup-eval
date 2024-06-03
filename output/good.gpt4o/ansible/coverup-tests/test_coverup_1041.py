# file lib/ansible/plugins/filter/core.py:140-170
# lines [143, 145, 146, 147, 148, 149, 150, 151, 152, 154, 156, 157, 158, 159, 160, 162, 163, 164, 165, 167, 168, 169, 170]
# branches ['146->147', '146->156', '147->148', '147->150', '150->151', '150->154', '157->158', '157->159', '159->160', '159->162', '163->exit', '163->164', '164->165', '164->167', '168->169', '168->170']

import pytest
from ansible.plugins.filter.core import regex_search, AnsibleFilterError

def test_regex_search_full_coverage():
    # Test case to cover the conversion of value to text
    value = b"test string"
    regex = r"test"
    result = regex_search(value, regex)
    assert result == "test"

    # Test case to cover the '\\g' group argument
    value = "test string"
    regex = r"(?P<first>test) (?P<second>string)"
    result = regex_search(value, regex, r'\g<first>', r'\g<second>')
    assert result == ["test", "string"]

    # Test case to cover the '\\' group argument
    value = "test string"
    regex = r"(test) (string)"
    result = regex_search(value, regex, r'\1', r'\2')
    assert result == ["test", "string"]

    # Test case to cover the unknown argument
    with pytest.raises(AnsibleFilterError, match="Unknown argument"):
        regex_search(value, regex, r'\1', 'unknown')

    # Test case to cover the ignorecase flag
    value = "Test String"
    regex = r"test"
    result = regex_search(value, regex, ignorecase=True)
    assert result == "Test"

    # Test case to cover the multiline flag
    value = "test\nstring"
    regex = r"^string"
    result = regex_search(value, regex, multiline=True)
    assert result == "string"

    # Test case to cover no match found
    value = "test string"
    regex = r"notfound"
    result = regex_search(value, regex)
    assert result is None
