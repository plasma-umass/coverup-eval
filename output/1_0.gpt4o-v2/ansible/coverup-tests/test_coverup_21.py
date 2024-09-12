# file: lib/ansible/plugins/doc_fragments/vars_plugin_staging.py:10-24
# asked: {"lines": [10, 12], "branches": []}
# gained: {"lines": [10, 12], "branches": []}

import pytest
from ansible.plugins.doc_fragments.vars_plugin_staging import ModuleDocFragment

def test_module_doc_fragment_documentation():
    # Check if the DOCUMENTATION attribute exists
    assert hasattr(ModuleDocFragment, 'DOCUMENTATION')
    
    # Check if the DOCUMENTATION attribute is a string
    assert isinstance(ModuleDocFragment.DOCUMENTATION, str)
    
    # Check if the DOCUMENTATION string contains expected content
    assert 'options:' in ModuleDocFragment.DOCUMENTATION
    assert 'stage:' in ModuleDocFragment.DOCUMENTATION
    assert 'description:' in ModuleDocFragment.DOCUMENTATION
    assert 'choices: [\'all\', \'task\', \'inventory\']' in ModuleDocFragment.DOCUMENTATION
    assert 'version_added: "2.10"' in ModuleDocFragment.DOCUMENTATION
    assert 'type: str' in ModuleDocFragment.DOCUMENTATION
