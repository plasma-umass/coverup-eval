# file lib/ansible/plugins/lookup/nested.py:57-85
# lines [57, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 71, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85]
# branches ['61->62', '61->67', '76->77', '76->78', '79->80', '79->82', '83->84', '83->85']

import pytest
from ansible.errors import AnsibleError, AnsibleUndefinedVariable
from ansible.plugins.lookup.nested import LookupModule
from ansible.template import Templar
from ansible.parsing.dataloader import DataLoader

# Mock classes and functions
class MockTemplar(Templar):
    def __init__(self, *args, **kwargs):
        pass

    def template(self, variable, fail_on_undefined=False):
        if variable == "undefined_variable":
            raise AnsibleUndefinedVariable("undefined variable: %s" % variable)
        return variable

def mock_listify_lookup_plugin_terms(term, templar=None, loader=None, fail_on_undefined=False):
    if term == "undefined_variable":
        raise AnsibleUndefinedVariable("undefined variable: %s" % term)
    return [term]

@pytest.fixture
def lookup_module(mocker):
    mocker.patch('ansible.plugins.lookup.nested.listify_lookup_plugin_terms', side_effect=mock_listify_lookup_plugin_terms)
    return LookupModule(loader=DataLoader(), templar=MockTemplar())

def test_lookup_module_with_undefined_variable(lookup_module):
    with pytest.raises(AnsibleUndefinedVariable):
        lookup_module.run(["undefined_variable"])

def test_lookup_module_with_empty_list(lookup_module):
    with pytest.raises(AnsibleError):
        lookup_module.run([])

def test_lookup_module_with_single_element(lookup_module):
    result = lookup_module.run([["a"]])
    assert result == [["a"]]

def test_lookup_module_with_multiple_elements(lookup_module):
    result = lookup_module.run([["a"], ["b"], ["c"]])
    assert result == [["a", "b", "c"]]

# Run the tests
# Note: The actual test execution should be handled by the pytest framework, not by calling pytest.main() here.
