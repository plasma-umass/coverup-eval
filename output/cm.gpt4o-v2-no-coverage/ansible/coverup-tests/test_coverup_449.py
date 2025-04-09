# file: lib/ansible/playbook/conditional.py:66-76
# asked: {"lines": [66, 67, 69, 70, 71, 72, 73, 74, 76], "branches": [[71, 72], [71, 76]]}
# gained: {"lines": [66, 67, 69, 70, 71, 72, 73, 74, 76], "branches": [[71, 72], [71, 76]]}

import re
import pytest
from ansible.playbook.conditional import Conditional
from ansible.errors import AnsibleError

DEFINED_REGEX = re.compile(r'(hostvars\[.+\]|[\w_]+)\s+(not\s+is|is|is\s+not)\s+(defined|undefined)')

class MockLoader:
    pass

@pytest.fixture
def conditional_instance():
    return Conditional(loader=MockLoader())

def test_extract_defined_undefined_no_match(conditional_instance):
    result = conditional_instance.extract_defined_undefined("no match here")
    assert result == []

def test_extract_defined_undefined_single_match(conditional_instance):
    result = conditional_instance.extract_defined_undefined("var1 is defined")
    assert result == [('var1', 'is', 'defined')]

def test_extract_defined_undefined_multiple_matches(conditional_instance):
    result = conditional_instance.extract_defined_undefined("var1 is defined and var2 is not defined")
    assert result == [('var1', 'is', 'defined'), ('var2', 'is not', 'defined')]

def test_extract_defined_undefined_hostvars_match(conditional_instance):
    result = conditional_instance.extract_defined_undefined("hostvars['some_host'] is defined")
    assert result == [("hostvars['some_host']", 'is', 'defined')]

def test_extract_defined_undefined_mixed_matches(conditional_instance):
    result = conditional_instance.extract_defined_undefined("var1 is defined and hostvars['some_host'] is not defined")
    assert result == [('var1', 'is', 'defined'), ("hostvars['some_host']", 'is not', 'defined')]
