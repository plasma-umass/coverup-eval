# file: lib/ansible/plugins/doc_fragments/decrypt.py:9-20
# asked: {"lines": [9, 12], "branches": []}
# gained: {"lines": [9, 12], "branches": []}

import pytest
from ansible.plugins.doc_fragments.decrypt import ModuleDocFragment

def test_documentation_fragment():
    # Check if the DOCUMENTATION attribute exists and is a string
    assert hasattr(ModuleDocFragment, 'DOCUMENTATION')
    assert isinstance(ModuleDocFragment.DOCUMENTATION, str)

    # Check if the DOCUMENTATION string contains expected content
    expected_content = '''
options:
  decrypt:
    description:
      - This option controls the autodecryption of source files using vault.
    type: bool
    default: yes
    version_added: '2.4'
'''
    assert ModuleDocFragment.DOCUMENTATION.strip() == expected_content.strip()
