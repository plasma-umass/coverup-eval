# file lib/ansible/plugins/lookup/indexed_items.py:41-52
# lines [41, 43, 44, 46, 48, 49, 51, 52]
# branches ['48->49', '48->51']

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.indexed_items import LookupModule

def test_lookup_module_with_valid_list(mocker):
    # Setup
    mock_basedir = mocker.MagicMock()
    lookup = LookupModule(basedir=mock_basedir)
    test_list = ['a', 'b', 'c']

    # Exercise
    result = lookup.run(test_list, variables={})

    # Verify
    assert result == [(0, 'a'), (1, 'b'), (2, 'c')]

def test_lookup_module_with_non_list_input(mocker):
    # Setup
    mock_basedir = mocker.MagicMock()
    lookup = LookupModule(basedir=mock_basedir)
    non_list_input = 'not a list'

    # Exercise and Verify
    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(non_list_input, variables={})
    assert "with_indexed_items expects a list" in str(excinfo.value)
