# file: lib/ansible/playbook/conditional.py:66-76
# asked: {"lines": [66, 67, 69, 70, 71, 72, 73, 74, 76], "branches": [[71, 72], [71, 76]]}
# gained: {"lines": [66, 67, 69, 70, 71, 72, 73, 74, 76], "branches": [[71, 72], [71, 76]]}

import pytest
import re
from ansible.playbook.conditional import Conditional
from ansible.errors import AnsibleError

DEFINED_REGEX = re.compile('(hostvars\\[.+\\]|[\\w_]+)\\s+(not\\s+is|is|is\\s+not)\\s+(defined|undefined)')

class MockLoader:
    pass

@pytest.fixture
def conditional_instance():
    return Conditional(loader=MockLoader())

def test_extract_defined_undefined_single_match(conditional_instance):
    conditional = "variable is defined"
    expected = [('variable', 'is', 'defined')]
    result = conditional_instance.extract_defined_undefined(conditional)
    assert result == expected

def test_extract_defined_undefined_multiple_matches(conditional_instance):
    conditional = "variable1 is defined and variable2 is not defined"
    expected = [('variable1', 'is', 'defined'), ('variable2', 'is not', 'defined')]
    result = conditional_instance.extract_defined_undefined(conditional)
    assert result == expected

def test_extract_defined_undefined_no_match(conditional_instance):
    conditional = "variable is something else"
    expected = []
    result = conditional_instance.extract_defined_undefined(conditional)
    assert result == expected

def test_extract_defined_undefined_hostvars_match(conditional_instance):
    conditional = "hostvars['some_host'] is defined"
    expected = [("hostvars['some_host']", 'is', 'defined')]
    result = conditional_instance.extract_defined_undefined(conditional)
    assert result == expected
