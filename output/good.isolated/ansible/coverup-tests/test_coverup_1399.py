# file lib/ansible/utils/vars.py:185-210
# lines [191]
# branches ['190->191']

import pytest
from ansible.errors import AnsibleOptionsError
from ansible.utils.vars import load_extra_vars
from ansible.parsing.dataloader import DataLoader
from ansible.utils.vars import combine_vars
from ansible.module_utils.common.collections import ImmutableDict
from collections.abc import MutableMapping
from ansible.utils.vars import parse_kv
from unittest.mock import MagicMock

@pytest.fixture
def mock_context(monkeypatch):
    mock_cliargs = {'extra_vars': [None, '']}
    monkeypatch.setattr('ansible.utils.vars.context.CLIARGS', mock_cliargs)

def test_load_extra_vars_skips_empty_values(mock_context, mocker):
    loader = DataLoader()
    mocker.patch('ansible.utils.vars.to_text', side_effect=lambda x, errors: x)
    mocker.patch('ansible.utils.vars.combine_vars', side_effect=lambda x, y: {**x, **y})
    mocker.patch('ansible.utils.vars.parse_kv', side_effect=lambda x: x)

    result = load_extra_vars(loader)
    assert result == {}, "Expected empty dictionary when extra_vars are None or empty string"
