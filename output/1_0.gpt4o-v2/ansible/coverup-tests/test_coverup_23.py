# file: lib/ansible/plugins/lookup/indexed_items.py:41-52
# asked: {"lines": [41, 43, 44, 46, 48, 49, 51, 52], "branches": [[48, 49], [48, 51]]}
# gained: {"lines": [41, 43, 44, 46, 48, 49, 51, 52], "branches": [[48, 49], [48, 51]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.indexed_items import LookupModule

@pytest.fixture
def lookup_module():
    return LookupModule()

def test_init_with_basedir():
    basedir = "/some/path"
    lookup = LookupModule(basedir=basedir)
    assert lookup.basedir == basedir

def test_init_without_basedir():
    lookup = LookupModule()
    assert lookup.basedir is None

def test_run_with_non_list_terms(lookup_module):
    with pytest.raises(AnsibleError, match="with_indexed_items expects a list"):
        lookup_module.run("not a list", {})

def test_run_with_empty_list(lookup_module, mocker):
    mocker.patch.object(LookupModule, '_flatten', return_value=[])
    result = lookup_module.run([], {})
    assert result == []

def test_run_with_list(lookup_module, mocker):
    terms = ["a", "b", "c"]
    mocker.patch.object(LookupModule, '_flatten', return_value=terms)
    result = lookup_module.run(terms, {})
    assert result == list(zip(range(len(terms)), terms))
