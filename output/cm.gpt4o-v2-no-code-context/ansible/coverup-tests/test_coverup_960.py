# file: lib/ansible/module_utils/common/validation.py:70-100
# asked: {"lines": [88, 89, 90, 91, 93, 94, 95, 96, 97, 98, 100], "branches": [[85, 88], [88, 89], [88, 93], [90, 88], [90, 91], [93, 94], [93, 100], [96, 97], [96, 98]]}
# gained: {"lines": [88, 89, 90, 91, 93, 94, 95, 96, 97, 98, 100], "branches": [[85, 88], [88, 89], [88, 93], [90, 88], [90, 91], [93, 94], [93, 100], [96, 97], [96, 98]]}

import pytest
from ansible.module_utils.common.validation import check_mutually_exclusive

def count_terms(check, parameters):
    """Mock function to simulate count_terms behavior."""
    return sum(1 for term in check if term in parameters and parameters[term] is not None)

def test_check_mutually_exclusive_no_terms():
    terms = None
    parameters = {}
    result = check_mutually_exclusive(terms, parameters)
    assert result == []

def test_check_mutually_exclusive_no_conflict():
    terms = [['a', 'b'], ['c', 'd']]
    parameters = {'a': 1, 'c': 2}
    result = check_mutually_exclusive(terms, parameters)
    assert result == []

def test_check_mutually_exclusive_conflict():
    terms = [['a', 'b'], ['c', 'd']]
    parameters = {'a': 1, 'b': 2}
    with pytest.raises(TypeError, match="parameters are mutually exclusive: a|b"):
        check_mutually_exclusive(terms, parameters)

def test_check_mutually_exclusive_conflict_with_context():
    terms = [['a', 'b'], ['c', 'd']]
    parameters = {'a': 1, 'b': 2}
    options_context = ['parent']
    with pytest.raises(TypeError, match="parameters are mutually exclusive: a|b found in parent"):
        check_mutually_exclusive(terms, parameters, options_context)

@pytest.fixture(autouse=True)
def mock_count_terms(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.common.validation.count_terms', count_terms)
