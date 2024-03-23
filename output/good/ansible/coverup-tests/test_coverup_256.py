# file lib/ansible/cli/doc.py:210-232
# lines [210, 222, 223, 225, 226, 227, 228, 229, 230, 231, 232]
# branches ['222->223', '222->225', '229->230', '229->232']

import pytest
from ansible.cli.doc import RoleMixin

@pytest.fixture
def role_mixin():
    return RoleMixin()

@pytest.fixture
def role_argspec():
    return {
        'main': {
            'short_description': 'Main entry point'
        },
        'setup': {
            'short_description': 'Setup tasks'
        },
        'teardown': None
    }

def test_build_summary_with_collection(role_mixin, role_argspec):
    role = 'testrole'
    collection = 'test.collection'
    fqcn, summary = role_mixin._build_summary(role, collection, role_argspec)
    assert fqcn == 'test.collection.testrole'
    assert summary['collection'] == collection
    assert summary['entry_points']['main'] == 'Main entry point'
    assert summary['entry_points']['setup'] == 'Setup tasks'
    assert summary['entry_points']['teardown'] == ''

def test_build_summary_without_collection(role_mixin, role_argspec):
    role = 'testrole'
    collection = ''
    fqcn, summary = role_mixin._build_summary(role, collection, role_argspec)
    assert fqcn == 'testrole'
    assert summary['collection'] == ''
    assert summary['entry_points']['main'] == 'Main entry point'
    assert summary['entry_points']['setup'] == 'Setup tasks'
    assert summary['entry_points']['teardown'] == ''
