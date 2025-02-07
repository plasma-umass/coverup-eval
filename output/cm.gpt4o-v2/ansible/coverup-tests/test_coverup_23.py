# file: lib/ansible/utils/collection_loader/_collection_finder.py:705-760
# asked: {"lines": [705, 713, 714, 715, 716, 717, 719, 720, 722, 723, 725, 726, 727, 728, 729, 731, 733, 734, 736, 737, 739, 741, 742, 743, 744, 747, 749, 750, 751, 753, 755, 757, 759, 760], "branches": [[714, 715], [714, 716], [719, 720], [719, 722], [722, 723], [722, 725], [726, 727], [726, 731], [727, 728], [727, 729], [741, 742], [741, 743], [743, 744], [743, 747], [749, 750], [749, 753], [753, 755], [753, 757]]}
# gained: {"lines": [705, 713, 714, 715, 716, 717, 719, 720, 722, 723, 725, 726, 727, 728, 729, 731, 733, 734, 736, 737, 739, 741, 743, 747, 749, 750, 751, 753, 757, 759, 760], "branches": [[714, 715], [714, 716], [719, 720], [719, 722], [722, 723], [722, 725], [726, 727], [726, 731], [727, 728], [727, 729], [741, 743], [743, 747], [749, 750], [749, 753], [753, 757]]}

import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef

def test_ansible_collection_ref_valid():
    ref = AnsibleCollectionRef('namespace.collection', 'subdir1.subdir2', 'mymodule', 'modules')
    assert ref.collection == 'namespace.collection'
    assert ref.subdirs == 'subdir1.subdir2'
    assert ref.resource == 'mymodule'
    assert ref.ref_type == 'modules'
    assert ref.n_python_package_name == 'ansible_collections.namespace.collection.plugins.modules.subdir1.subdir2'
    assert ref._fqcr == 'namespace.collection.subdir1.subdir2.mymodule'

def test_ansible_collection_ref_no_subdirs():
    ref = AnsibleCollectionRef('namespace.collection', None, 'mymodule', 'modules')
    assert ref.collection == 'namespace.collection'
    assert ref.subdirs == ''
    assert ref.resource == 'mymodule'
    assert ref.ref_type == 'modules'
    assert ref.n_python_package_name == 'ansible_collections.namespace.collection.plugins.modules'
    assert ref._fqcr == 'namespace.collection.mymodule'

def test_ansible_collection_ref_invalid_collection_name():
    with pytest.raises(ValueError, match='invalid collection name'):
        AnsibleCollectionRef('invalid_collection_name', 'subdir1.subdir2', 'mymodule', 'modules')

def test_ansible_collection_ref_invalid_ref_type():
    with pytest.raises(ValueError, match='invalid collection ref_type'):
        AnsibleCollectionRef('namespace.collection', 'subdir1.subdir2', 'mymodule', 'invalid_ref_type')

def test_ansible_collection_ref_invalid_subdirs():
    with pytest.raises(ValueError, match='invalid subdirs entry'):
        AnsibleCollectionRef('namespace.collection', 'invalid/subdir', 'mymodule', 'modules')
