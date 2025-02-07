# file: lib/ansible/utils/collection_loader/_collection_finder.py:705-760
# asked: {"lines": [742, 744, 755], "branches": [[741, 742], [743, 744], [753, 755]]}
# gained: {"lines": [742, 744, 755], "branches": [[741, 742], [743, 744], [753, 755]]}

import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef

def test_ansible_collection_ref_role():
    ref = AnsibleCollectionRef('namespace.collection', None, 'myrole', 'role')
    assert ref.n_python_package_name == 'ansible_collections.namespace.collection.roles.myrole'
    assert ref._fqcr == 'namespace.collection.myrole'

def test_ansible_collection_ref_playbook():
    ref = AnsibleCollectionRef('namespace.collection', None, 'myplaybook', 'playbook')
    assert ref.n_python_package_name == 'ansible_collections.namespace.collection.playbooks.myplaybook'
    assert ref._fqcr == 'namespace.collection.myplaybook'

def test_ansible_collection_ref_plugin():
    ref = AnsibleCollectionRef('namespace.collection', None, 'myplugin', 'modules')
    assert ref.n_python_package_name == 'ansible_collections.namespace.collection.plugins.modules'
    assert ref._fqcr == 'namespace.collection.myplugin'
