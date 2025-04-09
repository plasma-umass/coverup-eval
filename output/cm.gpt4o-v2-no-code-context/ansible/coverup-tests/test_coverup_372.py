# file: lib/ansible/cli/inventory.py:237-244
# asked: {"lines": [237, 238, 240, 241, 242, 244], "branches": [[240, 241], [240, 244], [241, 240], [241, 242]]}
# gained: {"lines": [237, 238, 240, 241, 242, 244], "branches": [[240, 241], [240, 244], [241, 242]]}

import pytest
from ansible.cli.inventory import InventoryCLI

INTERNAL_VARS = ['_internal_var1', '_internal_var2']

@pytest.fixture
def sample_dump():
    return {
        '_internal_var1': 'value1',
        '_internal_var2': 'value2',
        'external_var': 'value3'
    }

def test_remove_internal_vars(sample_dump, monkeypatch):
    monkeypatch.setattr('ansible.cli.inventory.INTERNAL_VARS', INTERNAL_VARS)
    result = InventoryCLI._remove_internal(sample_dump)
    assert '_internal_var1' not in result
    assert '_internal_var2' not in result
    assert 'external_var' in result
    assert result['external_var'] == 'value3'
