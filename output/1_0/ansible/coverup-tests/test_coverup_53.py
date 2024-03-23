# file lib/ansible/plugins/doc_fragments/action_core.py:9-58
# lines [9, 12, 40]
# branches []

import pytest

# Assuming the code from the question is in a file named action_core.py
from ansible.plugins.doc_fragments import action_core

def test_module_doc_fragment_attributes():
    # Accessing the attributes to ensure they are covered by the test
    doc_attributes = action_core.ModuleDocFragment.DOCUMENTATION
    import_attributes = action_core.ModuleDocFragment.IMPORT

    # Assertions to check the postconditions (if any)
    assert 'attributes' in doc_attributes
    assert 'async' in doc_attributes
    assert 'become' in doc_attributes
    assert 'bypass_task_loop' in doc_attributes
    assert 'core' in doc_attributes
    assert 'connection' in doc_attributes
    assert 'ignore_conditional' in doc_attributes
    assert 'platform' in doc_attributes
    assert 'until' in doc_attributes
    assert 'tags' in doc_attributes

    assert 'attributes' in import_attributes
    assert 'action' in import_attributes
    assert 'bypass_host_loop' in import_attributes
    assert 'bypass_task_loop' in import_attributes
    assert 'delegation' in import_attributes
    assert 'ignore_conditional' in import_attributes
    assert 'tags' in import_attributes

    # No need to mock or clean up as we are directly accessing class attributes
