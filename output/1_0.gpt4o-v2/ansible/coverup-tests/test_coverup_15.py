# file: lib/ansible/plugins/doc_fragments/connection_pipelining.py:7-29
# asked: {"lines": [7, 10], "branches": []}
# gained: {"lines": [7, 10], "branches": []}

import pytest
from ansible.plugins.doc_fragments.connection_pipelining import ModuleDocFragment

def test_module_doc_fragment_documentation():
    # Ensure the DOCUMENTATION attribute exists
    assert hasattr(ModuleDocFragment, 'DOCUMENTATION')
    
    # Ensure the DOCUMENTATION attribute is a string
    assert isinstance(ModuleDocFragment.DOCUMENTATION, str)
    
    # Check that the DOCUMENTATION string contains expected content
    assert 'options:' in ModuleDocFragment.DOCUMENTATION
    assert 'pipelining:' in ModuleDocFragment.DOCUMENTATION
    assert 'default: ANSIBLE_PIPELINING' in ModuleDocFragment.DOCUMENTATION
    assert 'description:' in ModuleDocFragment.DOCUMENTATION
    assert 'env:' in ModuleDocFragment.DOCUMENTATION
    assert 'ini:' in ModuleDocFragment.DOCUMENTATION
    assert 'type: boolean' in ModuleDocFragment.DOCUMENTATION
    assert 'vars:' in ModuleDocFragment.DOCUMENTATION
