# file lib/ansible/cli/doc.py:234-252
# lines [234, 235, 236, 238, 239, 240, 241, 242, 243, 244, 245, 246, 249, 250, 252]
# branches ['235->236', '235->238', '243->244', '243->249', '244->243', '244->245', '249->250', '249->252']

import pytest
from ansible.cli.doc import RoleMixin

@pytest.fixture
def role_mixin():
    return RoleMixin()

def test_build_doc_with_no_entry_points(role_mixin):
    role = "test_role"
    path = "/path/to/role"
    collection = "test.collection"
    argspec = {"main": None}
    entry_point = "non_existent_entry_point"

    fqcn, doc = role_mixin._build_doc(role, path, collection, argspec, entry_point)

    assert fqcn == "test.collection.test_role"
    assert doc is None

def test_build_doc_with_entry_points(role_mixin):
    role = "test_role"
    path = "/path/to/role"
    collection = "test.collection"
    argspec = {"main": {"description": "Main entry point"}}
    entry_point = "main"

    fqcn, doc = role_mixin._build_doc(role, path, collection, argspec, entry_point)

    assert fqcn == "test.collection.test_role"
    assert doc is not None
    assert doc['path'] == path
    assert doc['collection'] == collection
    assert doc['entry_points'] == {"main": {"description": "Main entry point"}}
