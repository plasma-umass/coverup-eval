# file lib/ansible/plugins/doc_fragments/vars_plugin_staging.py:10-24
# lines [10, 12]
# branches []

import pytest

# Assuming the ModuleDocFragment class is part of a module named vars_plugin_staging
from ansible.plugins.doc_fragments.vars_plugin_staging import ModuleDocFragment

def test_module_doc_fragment():
    # Instantiate the ModuleDocFragment to access its DOCUMENTATION attribute
    doc_fragment = ModuleDocFragment()
    documentation = doc_fragment.DOCUMENTATION

    # Assert that the DOCUMENTATION string contains the expected options
    assert 'options:' in documentation
    assert 'stage:' in documentation
    assert 'description:' in documentation
    assert '- Control when this vars plugin may be executed.' in documentation
    assert 'choices: [\'all\', \'task\', \'inventory\']' in documentation
    assert 'version_added: "2.10"' in documentation
    assert 'type: str' in documentation
