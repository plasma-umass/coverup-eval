# file lib/ansible/plugins/doc_fragments/files.py:9-58
# lines [9, 15]
# branches []

import pytest

# Assuming the ModuleDocFragment class is in a file named files.py
from ansible.plugins.doc_fragments.files import ModuleDocFragment

def test_module_doc_fragment():
    # Instantiate the ModuleDocFragment to access the DOCUMENTATION attribute
    doc_fragment = ModuleDocFragment()
    
    # Check if the DOCUMENTATION attribute is a string
    assert isinstance(doc_fragment.DOCUMENTATION, str)
    
    # Check if the DOCUMENTATION contains expected keys
    assert 'options' in doc_fragment.DOCUMENTATION
    assert 'mode' in doc_fragment.DOCUMENTATION
    assert 'owner' in doc_fragment.DOCUMENTATION
    assert 'group' in doc_fragment.DOCUMENTATION
    assert 'seuser' in doc_fragment.DOCUMENTATION
    assert 'serole' in doc_fragment.DOCUMENTATION
    assert 'setype' in doc_fragment.DOCUMENTATION
    assert 'selevel' in doc_fragment.DOCUMENTATION

    # Check if the mode description is correct
    assert 'The permissions the resulting filesystem object should have.' in doc_fragment.DOCUMENTATION
    assert 'For those used to I(/usr/bin/chmod) remember that modes are actually octal numbers.' in doc_fragment.DOCUMENTATION
    assert 'As of Ansible 1.8, the mode may be specified as a symbolic mode' in doc_fragment.DOCUMENTATION
    assert 'If C(mode) is not specified and the destination filesystem object B(does not) exist' in doc_fragment.DOCUMENTATION
    assert 'If C(mode) is not specified and the destination filesystem object B(does) exist' in doc_fragment.DOCUMENTATION
    assert 'Specifying C(mode) is the best way to ensure filesystem objects are created with the correct permissions.' in doc_fragment.DOCUMENTATION
    assert 'See CVE-2020-1736 for further details.' in doc_fragment.DOCUMENTATION

    # Check if the owner description is correct
    assert 'Name of the user that should own the filesystem object, as would be fed to I(chown).' in doc_fragment.DOCUMENTATION

    # Check if the group description is correct
    assert 'Name of the group that should own the filesystem object, as would be fed to I(chown).' in doc_fragment.DOCUMENTATION

    # Check if the seuser description is correct
    assert 'The user part of the SELinux filesystem object context.' in doc_fragment.DOCUMENTATION
    assert 'By default it uses the C(system) policy, where applicable.' in doc_fragment.DOCUMENTATION
    assert 'When set to C(_default), it will use the C(user) portion of the policy if available.' in doc_fragment.DOCUMENTATION

    # Check if the serole description is correct
    assert 'The role part of the SELinux filesystem object context.' in doc_fragment.DOCUMENTATION
    assert 'When set to C(_default), it will use the C(role) portion of the policy if available.' in doc_fragment.DOCUMENTATION

    # Check if the setype description is correct
    assert 'The type part of the SELinux filesystem object context.' in doc_fragment.DOCUMENTATION
    assert 'When set to C(_default), it will use the C(type) portion of the policy if available.' in doc_fragment.DOCUMENTATION

    # Check if the selevel description is correct
    assert 'selevel' in doc_fragment.DOCUMENTATION
