# file lib/ansible/cli/doc.py:234-252
# lines [235, 236, 238, 239, 240, 241, 242, 243, 244, 245, 246, 249, 250, 252]
# branches ['235->236', '235->238', '243->244', '243->249', '244->243', '244->245', '249->250', '249->252']

import pytest
from unittest.mock import MagicMock
from ansible.cli.doc import RoleMixin

@pytest.fixture
def role_mixin():
    return RoleMixin()

def test_build_doc_with_collection(role_mixin):
    role = "test_role"
    path = "/path/to/role"
    collection = "test_collection"
    argspec = {"default": {"arg1": "value1"}, "other": {"arg2": "value2"}}
    entry_point = None

    fqcn, doc = role_mixin._build_doc(role, path, collection, argspec, entry_point)

    assert fqcn == "test_collection.test_role"
    assert doc is not None
    assert doc['path'] == path
    assert doc['collection'] == collection
    assert 'default' in doc['entry_points']
    assert 'other' in doc['entry_points']

def test_build_doc_without_collection(role_mixin):
    role = "test_role"
    path = "/path/to/role"
    collection = None
    argspec = {"default": {"arg1": "value1"}, "other": {"arg2": "value2"}}
    entry_point = None

    fqcn, doc = role_mixin._build_doc(role, path, collection, argspec, entry_point)

    assert fqcn == "test_role"
    assert doc is not None
    assert doc['path'] == path
    assert doc['collection'] == collection
    assert 'default' in doc['entry_points']
    assert 'other' in doc['entry_points']

def test_build_doc_with_entry_point_filtering(role_mixin):
    role = "test_role"
    path = "/path/to/role"
    collection = "test_collection"
    argspec = {"default": {"arg1": "value1"}, "other": {"arg2": "value2"}}
    entry_point = "default"

    fqcn, doc = role_mixin._build_doc(role, path, collection, argspec, entry_point)

    assert fqcn == "test_collection.test_role"
    assert doc is not None
    assert doc['path'] == path
    assert doc['collection'] == collection
    assert 'default' in doc['entry_points']
    assert 'other' not in doc['entry_points']

def test_build_doc_no_entry_points(role_mixin):
    role = "test_role"
    path = "/path/to/role"
    collection = "test_collection"
    argspec = {"default": None}
    entry_point = "other"

    fqcn, doc = role_mixin._build_doc(role, path, collection, argspec, entry_point)

    assert fqcn == "test_collection.test_role"
    assert doc is None
