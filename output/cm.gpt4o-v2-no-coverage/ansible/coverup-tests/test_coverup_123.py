# file: lib/ansible/utils/collection_loader/_collection_finder.py:769-810
# asked: {"lines": [769, 770, 783, 784, 786, 787, 788, 790, 791, 792, 793, 794, 796, 797, 798, 802, 803, 804, 806, 808, 810], "branches": [[783, 784], [783, 786], [790, 791], [790, 796], [803, 804], [803, 806]]}
# gained: {"lines": [769, 770, 783, 784, 786, 787, 788, 790, 791, 792, 793, 794, 796, 797, 798, 802, 803, 804, 806, 808, 810], "branches": [[783, 784], [783, 786], [790, 791], [790, 796], [803, 804], [803, 806]]}

import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef
from ansible.module_utils.common.text.converters import to_native

def test_from_fqcr_valid_module(monkeypatch):
    ref = 'ns.coll.module_name'
    ref_type = 'modules'
    result = AnsibleCollectionRef.from_fqcr(ref, ref_type)
    assert result.collection == 'ns.coll'
    assert result.subdirs == ''
    assert result.resource == 'module_name'
    assert result.ref_type == 'modules'

def test_from_fqcr_valid_role():
    ref = 'ns.coll.role_name'
    ref_type = 'role'
    result = AnsibleCollectionRef.from_fqcr(ref, ref_type)
    assert result.collection == 'ns.coll'
    assert result.subdirs == ''
    assert result.resource == 'role_name'
    assert result.ref_type == 'role'

def test_from_fqcr_valid_with_subdirs():
    ref = 'ns.coll.subdir1.subdir2.resource'
    ref_type = 'modules'
    result = AnsibleCollectionRef.from_fqcr(ref, ref_type)
    assert result.collection == 'ns.coll'
    assert result.subdirs == 'subdir1.subdir2'
    assert result.resource == 'resource'
    assert result.ref_type == 'modules'

def test_from_fqcr_invalid():
    ref = 'invalid_ref'
    ref_type = 'modules'
    with pytest.raises(ValueError, match=r'.*is not a valid collection reference.*'):
        AnsibleCollectionRef.from_fqcr(ref, ref_type)

def test_from_fqcr_playbook_with_extension(monkeypatch):
    ref = 'ns.coll.playbook_name.yml'
    ref_type = 'playbook'
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder.PB_EXTENSIONS', ('.yml', '.yaml'))
    result = AnsibleCollectionRef.from_fqcr(ref, ref_type)
    assert result.collection == 'ns.coll'
    assert result.subdirs == ''
    assert result.resource == 'playbook_name.yml'
    assert result.ref_type == 'playbook'
