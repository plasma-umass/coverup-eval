# file: lib/ansible/inventory/host.py:105-113
# asked: {"lines": [105, 107, 108, 109, 111, 112, 113], "branches": [[107, 108], [107, 111], [108, 0], [108, 109], [111, 0], [111, 112], [112, 111], [112, 113]]}
# gained: {"lines": [105, 107, 108, 109, 111, 112, 113], "branches": [[107, 108], [107, 111], [108, 0], [108, 109], [111, 0], [111, 112], [112, 111], [112, 113]]}

import pytest
from ansible.inventory.host import Host

def test_populate_ancestors_no_additions(monkeypatch):
    host = Host(name='testhost')
    host.groups = ['group1', 'group2']
    
    def mock_add_group(self, group):
        if group not in self.groups:
            self.groups.append(group)
    
    monkeypatch.setattr(Host, 'add_group', mock_add_group)
    
    host.populate_ancestors()
    assert host.groups == ['group1', 'group2']

def test_populate_ancestors_with_additions(monkeypatch):
    host = Host(name='testhost')
    host.groups = ['group1']
    
    def mock_add_group(self, group):
        if group not in self.groups:
            self.groups.append(group)
    
    monkeypatch.setattr(Host, 'add_group', mock_add_group)
    
    host.populate_ancestors(additions=['group2', 'group3'])
    assert host.groups == ['group1', 'group2', 'group3']

def test_populate_ancestors_with_existing_additions(monkeypatch):
    host = Host(name='testhost')
    host.groups = ['group1', 'group2']
    
    def mock_add_group(self, group):
        if group not in self.groups:
            self.groups.append(group)
    
    monkeypatch.setattr(Host, 'add_group', mock_add_group)
    
    host.populate_ancestors(additions=['group2', 'group3'])
    assert host.groups == ['group1', 'group2', 'group3']
