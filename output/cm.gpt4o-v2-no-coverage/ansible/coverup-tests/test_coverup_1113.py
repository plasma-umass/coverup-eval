# file: lib/ansible/module_utils/common/validation.py:103-134
# asked: {"lines": [122, 123, 124, 125, 127, 128, 129, 130, 131, 132, 134], "branches": [[119, 122], [122, 123], [122, 127], [124, 122], [124, 125], [127, 128], [127, 134], [128, 129], [128, 134], [130, 131], [130, 132]]}
# gained: {"lines": [122, 123, 124, 125, 127, 128, 129, 130, 131, 132, 134], "branches": [[119, 122], [122, 123], [122, 127], [124, 122], [124, 125], [127, 128], [127, 134], [128, 129], [130, 131], [130, 132]]}

import pytest
from ansible.module_utils.common.validation import check_required_one_of

def test_check_required_one_of_no_terms():
    assert check_required_one_of(None, {}) == []

def test_check_required_one_of_empty_terms():
    assert check_required_one_of([], {}) == []

def test_check_required_one_of_no_parameters():
    terms = [['a'], ['b', 'c']]
    with pytest.raises(TypeError, match="one of the following is required: a"):
        check_required_one_of(terms, {})

def test_check_required_one_of_single_term():
    terms = [['a']]
    parameters = {'a': 1}
    assert check_required_one_of(terms, parameters) == []

def test_check_required_one_of_multiple_terms():
    terms = [['a', 'b'], ['c', 'd']]
    parameters = {'a': 1, 'c': 2}
    assert check_required_one_of(terms, parameters) == []

def test_check_required_one_of_missing_terms():
    terms = [['a', 'b'], ['c', 'd']]
    parameters = {'a': 1}
    with pytest.raises(TypeError, match="one of the following is required: c, d"):
        check_required_one_of(terms, parameters)

def test_check_required_one_of_with_options_context():
    terms = [['a', 'b'], ['c', 'd']]
    parameters = {'a': 1}
    options_context = ['parent']
    with pytest.raises(TypeError, match="one of the following is required: c, d found in parent"):
        check_required_one_of(terms, parameters, options_context)
