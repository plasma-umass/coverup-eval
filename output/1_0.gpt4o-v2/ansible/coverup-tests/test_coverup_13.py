# file: lib/ansible/plugins/lookup/items.py:69-73
# asked: {"lines": [69, 71, 73], "branches": []}
# gained: {"lines": [69, 71, 73], "branches": []}

import pytest
from ansible.plugins.lookup.items import LookupModule

@pytest.fixture
def lookup_module():
    return LookupModule()

def test_run_method_executes_all_lines(lookup_module, mocker):
    terms = [[1, 2], [3, 4]]
    mocker.patch.object(lookup_module, '_flatten', return_value=[1, 2, 3, 4])
    
    result = lookup_module.run(terms)
    
    lookup_module._flatten.assert_called_once_with(terms)
    assert result == [1, 2, 3, 4]
