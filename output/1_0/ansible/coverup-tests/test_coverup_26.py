# file lib/ansible/plugins/doc_fragments/backup.py:9-20
# lines [9, 12]
# branches []

import pytest

# Assuming the ModuleDocFragment class is in a file named backup.py
from ansible.plugins.doc_fragments.backup import ModuleDocFragment

def test_module_doc_fragment_backup_option(mocker):
    # Mock the environment where the ModuleDocFragment is used
    mocker.patch('ansible.plugins.doc_fragments.backup.ModuleDocFragment')

    # Instantiate the ModuleDocFragment to access the DOCUMENTATION attribute
    doc_fragment = ModuleDocFragment()

    # Assert that the 'backup' option is present in the DOCUMENTATION attribute
    assert 'backup' in doc_fragment.DOCUMENTATION
    assert 'description' in doc_fragment.DOCUMENTATION
    assert 'type: bool' in doc_fragment.DOCUMENTATION
    assert 'default: no' in doc_fragment.DOCUMENTATION

    # Clean up is not necessary as we are not creating any persistent changes
