# file lib/ansible/plugins/doc_fragments/decrypt.py:9-20
# lines [9, 12]
# branches []

import pytest

# Assuming the code provided is part of a larger module, we will mock the necessary parts for testing.
# The test will focus on the ModuleDocFragment class and its DOCUMENTATION attribute.

# Test function to check if the DOCUMENTATION attribute is a string and contains the expected content.
def test_module_doc_fragment_documentation():
    from ansible.plugins.doc_fragments.decrypt import ModuleDocFragment

    assert isinstance(ModuleDocFragment.DOCUMENTATION, str)
    assert 'options:' in ModuleDocFragment.DOCUMENTATION
    assert 'decrypt:' in ModuleDocFragment.DOCUMENTATION
    assert 'description:' in ModuleDocFragment.DOCUMENTATION
    assert 'This option controls the autodecryption of source files using vault.' in ModuleDocFragment.DOCUMENTATION
    assert 'type: bool' in ModuleDocFragment.DOCUMENTATION
    assert 'default: yes' in ModuleDocFragment.DOCUMENTATION
    assert 'version_added: \'2.4\'' in ModuleDocFragment.DOCUMENTATION
