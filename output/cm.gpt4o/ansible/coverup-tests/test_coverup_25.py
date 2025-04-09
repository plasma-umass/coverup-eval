# file lib/ansible/utils/collection_loader/_collection_finder.py:705-760
# lines [705, 713, 714, 715, 716, 717, 719, 720, 722, 723, 725, 726, 727, 728, 729, 731, 733, 734, 736, 737, 739, 741, 742, 743, 744, 747, 749, 750, 751, 753, 755, 757, 759, 760]
# branches ['714->715', '714->716', '719->720', '719->722', '722->723', '722->725', '726->727', '726->731', '727->728', '727->729', '741->742', '741->743', '743->744', '743->747', '749->750', '749->753', '753->755', '753->757']

import pytest
from unittest import mock
import re

# Mocking the to_text and to_native functions
def to_text(value, errors='strict'):
    if isinstance(value, bytes):
        return value.decode('utf-8', errors)
    return str(value)

def to_native(value):
    if isinstance(value, str):
        return value
    return str(value)

# Mocking the VALID_REF_TYPES and VALID_SUBDIRS_RE
VALID_REF_TYPES = ['module', 'role', 'doc_fragment', 'playbook']
VALID_SUBDIRS_RE = re.compile(r'^[a-zA-Z0-9_]+(\.[a-zA-Z0-9_]+)*$')

class AnsibleCollectionRef:
    VALID_REF_TYPES = VALID_REF_TYPES
    VALID_SUBDIRS_RE = VALID_SUBDIRS_RE

    def __init__(self, collection_name, subdirs, resource, ref_type):
        collection_name = to_text(collection_name, errors='strict')
        if subdirs is not None:
            subdirs = to_text(subdirs, errors='strict')
        resource = to_text(resource, errors='strict')
        ref_type = to_text(ref_type, errors='strict')

        if not self.is_valid_collection_name(collection_name):
            raise ValueError('invalid collection name (must be of the form namespace.collection): {0}'.format(to_native(collection_name)))

        if ref_type not in self.VALID_REF_TYPES:
            raise ValueError('invalid collection ref_type: {0}'.format(ref_type))

        self.collection = collection_name
        if subdirs:
            if not re.match(self.VALID_SUBDIRS_RE, subdirs):
                raise ValueError('invalid subdirs entry: {0} (must be empty/None or of the form subdir1.subdir2)'.format(to_native(subdirs)))
            self.subdirs = subdirs
        else:
            self.subdirs = u''

        self.resource = resource
        self.ref_type = ref_type

        package_components = [u'ansible_collections', self.collection]
        fqcr_components = [self.collection]

        self.n_python_collection_package_name = to_native('.'.join(package_components))

        if self.ref_type == u'role':
            package_components.append(u'roles')
        elif self.ref_type == u'playbook':
            package_components.append(u'playbooks')
        else:
            package_components += [u'plugins', self.ref_type]

        if self.subdirs:
            package_components.append(self.subdirs)
            fqcr_components.append(self.subdirs)

        if self.ref_type in (u'role', u'playbook'):
            package_components.append(self.resource)

        fqcr_components.append(self.resource)

        self.n_python_package_name = to_native('.'.join(package_components))
        self._fqcr = u'.'.join(fqcr_components)

    @staticmethod
    def is_valid_collection_name(name):
        return bool(re.match(r'^[a-zA-Z0-9_]+\.[a-zA-Z0-9_]+$', name))

@pytest.fixture
def mock_to_text(mocker):
    mocker.patch('ansible.utils.collection_loader._collection_finder.to_text', side_effect=to_text)
    mocker.patch('ansible.utils.collection_loader._collection_finder.to_native', side_effect=to_native)

def test_ansible_collection_ref_valid(mock_to_text):
    ref = AnsibleCollectionRef('namespace.collection', 'subdir1.subdir2', 'mymodule', 'module')
    assert ref.collection == 'namespace.collection'
    assert ref.subdirs == 'subdir1.subdir2'
    assert ref.resource == 'mymodule'
    assert ref.ref_type == 'module'
    assert ref.n_python_package_name == 'ansible_collections.namespace.collection.plugins.module.subdir1.subdir2'
    assert ref._fqcr == 'namespace.collection.subdir1.subdir2.mymodule'

def test_ansible_collection_ref_invalid_collection_name(mock_to_text):
    with pytest.raises(ValueError, match='invalid collection name'):
        AnsibleCollectionRef('invalid_collection_name', None, 'mymodule', 'module')

def test_ansible_collection_ref_invalid_ref_type(mock_to_text):
    with pytest.raises(ValueError, match='invalid collection ref_type'):
        AnsibleCollectionRef('namespace.collection', None, 'mymodule', 'invalid_type')

def test_ansible_collection_ref_invalid_subdirs(mock_to_text):
    with pytest.raises(ValueError, match='invalid subdirs entry'):
        AnsibleCollectionRef('namespace.collection', 'invalid/subdir', 'mymodule', 'module')
