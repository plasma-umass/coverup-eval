# file: lib/ansible/plugins/doc_fragments/backup.py:9-20
# asked: {"lines": [9, 12], "branches": []}
# gained: {"lines": [9, 12], "branches": []}

import pytest
from ansible.plugins.doc_fragments.backup import ModuleDocFragment

def test_module_doc_fragment_documentation():
    # Ensure the DOCUMENTATION attribute exists
    assert hasattr(ModuleDocFragment, 'DOCUMENTATION')
    
    # Ensure the DOCUMENTATION attribute is a string
    assert isinstance(ModuleDocFragment.DOCUMENTATION, str)
    
    # Ensure the DOCUMENTATION string contains expected content
    assert 'options:' in ModuleDocFragment.DOCUMENTATION
    assert 'backup:' in ModuleDocFragment.DOCUMENTATION
    assert 'description:' in ModuleDocFragment.DOCUMENTATION
    assert 'type: bool' in ModuleDocFragment.DOCUMENTATION
    assert 'default: no' in ModuleDocFragment.DOCUMENTATION
