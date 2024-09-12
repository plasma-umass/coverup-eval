# file: lib/ansible/module_utils/common/validation.py:103-134
# asked: {"lines": [103, 118, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131, 132, 134], "branches": [[119, 120], [119, 122], [122, 123], [122, 127], [124, 122], [124, 125], [127, 128], [127, 134], [128, 129], [128, 134], [130, 131], [130, 132]]}
# gained: {"lines": [103, 118, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131, 132, 134], "branches": [[119, 120], [119, 122], [122, 123], [122, 127], [124, 122], [124, 125], [127, 128], [127, 134], [128, 129], [130, 131], [130, 132]]}

import pytest
from ansible.module_utils.common.validation import check_required_one_of

def count_terms(term, parameters):
    """Helper function to count terms in parameters"""
    return sum(1 for t in term if t in parameters and parameters[t] is not None)

def to_native(msg):
    """Helper function to convert message to native string"""
    return str(msg)

def test_check_required_one_of_no_terms():
    assert check_required_one_of(None, {}) == []

def test_check_required_one_of_empty_terms():
    assert check_required_one_of([], {}) == []

def test_check_required_one_of_single_term_present():
    assert check_required_one_of([['a']], {'a': 1}) == []

def test_check_required_one_of_single_term_missing():
    with pytest.raises(TypeError, match="one of the following is required: a"):
        check_required_one_of([['a']], {})

def test_check_required_one_of_multiple_terms_one_present():
    assert check_required_one_of([['a', 'b']], {'a': 1}) == []

def test_check_required_one_of_multiple_terms_none_present():
    with pytest.raises(TypeError, match="one of the following is required: a, b"):
        check_required_one_of([['a', 'b']], {})

def test_check_required_one_of_multiple_lists_one_missing():
    with pytest.raises(TypeError, match="one of the following is required: c, d"):
        check_required_one_of([['a', 'b'], ['c', 'd']], {'a': 1})

def test_check_required_one_of_with_options_context():
    with pytest.raises(TypeError, match="one of the following is required: a, b found in parent -> child"):
        check_required_one_of([['a', 'b']], {}, options_context=['parent', 'child'])

def test_check_required_one_of_all_present():
    assert check_required_one_of([['a', 'b'], ['c', 'd']], {'a': 1, 'c': 2}) == []

@pytest.fixture(autouse=True)
def cleanup(monkeypatch):
    # Ensure no state pollution
    monkeypatch.undo()
