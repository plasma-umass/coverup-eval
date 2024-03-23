# file lib/ansible/cli/doc.py:234-252
# lines [238]
# branches ['235->238']

import pytest
from ansible.cli.doc import RoleMixin

@pytest.fixture
def role_mixin():
    return RoleMixin()

def test_role_mixin_build_doc_without_collection(role_mixin, mocker):
    role = "test_role"
    path = "/path/to/role"
    collection = None
    argspec = {"defaults": None}
    entry_point = None

    fqcn, doc = role_mixin._build_doc(role, path, collection, argspec, entry_point)

    assert fqcn == "test_role"
    assert doc is not None
    assert doc['path'] == path
    assert doc['collection'] is None
    assert 'defaults' in doc['entry_points']
    assert doc['entry_points']['defaults'] == {}

@pytest.fixture(autouse=True)
def cleanup():
    # No cleanup is required as the test does not modify any external state
    yield
