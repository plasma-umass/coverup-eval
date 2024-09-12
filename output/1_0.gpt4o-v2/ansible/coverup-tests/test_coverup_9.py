# file: lib/ansible/plugins/doc_fragments/validate.py:9-21
# asked: {"lines": [9, 11], "branches": []}
# gained: {"lines": [9, 11], "branches": []}

import pytest
from ansible.plugins.doc_fragments.validate import ModuleDocFragment

def test_module_doc_fragment_documentation():
    # Ensure the DOCUMENTATION attribute exists
    assert hasattr(ModuleDocFragment, 'DOCUMENTATION')
    
    # Ensure the DOCUMENTATION attribute is a string
    assert isinstance(ModuleDocFragment.DOCUMENTATION, str)
    
    # Check that the DOCUMENTATION string contains expected content
    assert 'options:' in ModuleDocFragment.DOCUMENTATION
    assert 'validate:' in ModuleDocFragment.DOCUMENTATION
    assert 'description:' in ModuleDocFragment.DOCUMENTATION
    assert 'type: str' in ModuleDocFragment.DOCUMENTATION
