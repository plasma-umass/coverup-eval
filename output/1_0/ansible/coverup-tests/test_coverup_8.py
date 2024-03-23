# file lib/ansible/plugins/doc_fragments/action_common_attributes.py:8-57
# lines [8, 11, 22, 30, 40, 46, 54]
# branches []

import pytest

# Assuming the ModuleDocFragment class is in a file named action_common_attributes.py
from ansible.plugins.doc_fragments.action_common_attributes import ModuleDocFragment

def test_module_doc_fragment_documentation():
    assert 'check_mode' in ModuleDocFragment.DOCUMENTATION
    assert 'diff_mode' in ModuleDocFragment.DOCUMENTATION
    assert 'platform' in ModuleDocFragment.DOCUMENTATION

def test_module_doc_fragment_actiongroups():
    assert 'action_group' in ModuleDocFragment.ACTIONGROUPS

def test_module_doc_fragment_conn():
    assert 'become' in ModuleDocFragment.CONN
    assert 'connection' in ModuleDocFragment.CONN
    assert 'delegation' in ModuleDocFragment.CONN

def test_module_doc_fragment_facts():
    assert 'facts' in ModuleDocFragment.FACTS

def test_module_doc_fragment_files():
    assert 'safe_file_operations' in ModuleDocFragment.FILES
    assert 'vault' in ModuleDocFragment.FILES

def test_module_doc_fragment_flow():
    assert 'action' in ModuleDocFragment.FLOW
