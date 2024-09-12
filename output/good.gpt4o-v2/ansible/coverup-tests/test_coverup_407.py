# file: lib/ansible/cli/inventory.py:237-244
# asked: {"lines": [237, 238, 240, 241, 242, 244], "branches": [[240, 241], [240, 244], [241, 240], [241, 242]]}
# gained: {"lines": [237, 238, 240, 241, 242, 244], "branches": [[240, 241], [240, 244], [241, 240], [241, 242]]}

import pytest
from ansible.cli.inventory import InventoryCLI

INTERNAL_VARS = frozenset([
    'ansible_diff_mode', 'ansible_config_file', 'ansible_facts', 'ansible_forks', 
    'ansible_inventory_sources', 'ansible_limit', 'ansible_playbook_python', 
    'ansible_run_tags', 'ansible_skip_tags', 'ansible_verbosity', 'ansible_version', 
    'inventory_dir', 'inventory_file', 'inventory_hostname', 'inventory_hostname_short', 
    'groups', 'group_names', 'omit', 'playbook_dir'
])

class TestInventoryCLI:
    
    @pytest.fixture
    def dump_data(self):
        return {
            'ansible_diff_mode': True,
            'ansible_config_file': '/etc/ansible/ansible.cfg',
            'custom_var': 'value'
        }

    def test_remove_internal(self, dump_data):
        result = InventoryCLI._remove_internal(dump_data)
        assert 'ansible_diff_mode' not in result
        assert 'ansible_config_file' not in result
        assert 'custom_var' in result
        assert result['custom_var'] == 'value'
