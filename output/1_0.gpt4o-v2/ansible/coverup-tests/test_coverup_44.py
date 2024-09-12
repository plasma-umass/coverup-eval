# file: lib/ansible/plugins/lookup/list.py:39-44
# asked: {"lines": [39, 41, 42, 43, 44], "branches": [[42, 43], [42, 44]]}
# gained: {"lines": [39, 41, 42, 43, 44], "branches": [[42, 43], [42, 44]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.list import LookupModule
from ansible.module_utils.common._collections_compat import Sequence

def test_run_with_list():
    lookup = LookupModule()
    terms = [1, 2, 3]
    result = lookup.run(terms)
    assert result == terms

def test_run_with_non_list():
    lookup = LookupModule()
    terms = 123  # Using an integer to ensure it's not a sequence
    with pytest.raises(AnsibleError, match="with_list expects a list"):
        lookup.run(terms)
