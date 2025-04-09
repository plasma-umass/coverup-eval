# file: lib/ansible/module_utils/common/validation.py:103-134
# asked: {"lines": [103, 118, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131, 132, 134], "branches": [[119, 120], [119, 122], [122, 123], [122, 127], [124, 122], [124, 125], [127, 128], [127, 134], [128, 129], [128, 134], [130, 131], [130, 132]]}
# gained: {"lines": [103, 118, 119, 120, 122, 123, 124, 125, 127, 128, 129, 130, 131, 132, 134], "branches": [[119, 120], [119, 122], [122, 123], [122, 127], [124, 122], [124, 125], [127, 128], [127, 134], [128, 129], [130, 131], [130, 132]]}

import pytest
from ansible.module_utils.common.validation import check_required_one_of

def count_terms(term, parameters):
    return sum(1 for t in term if t in parameters)

def to_native(msg):
    return msg

def test_check_required_one_of_all_terms_present(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.common.validation.count_terms', count_terms)
    monkeypatch.setattr('ansible.module_utils.common.validation.to_native', to_native)
    terms = [['a', 'b'], ['c', 'd']]
    parameters = {'a': 1, 'c': 2}
    result = check_required_one_of(terms, parameters)
    assert result == []

def test_check_required_one_of_some_terms_missing(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.common.validation.count_terms', count_terms)
    monkeypatch.setattr('ansible.module_utils.common.validation.to_native', to_native)
    terms = [['a', 'b'], ['c', 'd']]
    parameters = {'a': 1}
    with pytest.raises(TypeError) as excinfo:
        check_required_one_of(terms, parameters)
    assert "one of the following is required: c, d" in str(excinfo.value)

def test_check_required_one_of_with_options_context(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.common.validation.count_terms', count_terms)
    monkeypatch.setattr('ansible.module_utils.common.validation.to_native', to_native)
    terms = [['a', 'b'], ['c', 'd']]
    parameters = {'a': 1}
    options_context = ['parent']
    with pytest.raises(TypeError) as excinfo:
        check_required_one_of(terms, parameters, options_context)
    assert "one of the following is required: c, d found in parent" in str(excinfo.value)

def test_check_required_one_of_no_terms(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.common.validation.count_terms', count_terms)
    monkeypatch.setattr('ansible.module_utils.common.validation.to_native', to_native)
    terms = None
    parameters = {'a': 1}
    result = check_required_one_of(terms, parameters)
    assert result == []

def test_check_required_one_of_empty_terms(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.common.validation.count_terms', count_terms)
    monkeypatch.setattr('ansible.module_utils.common.validation.to_native', to_native)
    terms = []
    parameters = {'a': 1}
    result = check_required_one_of(terms, parameters)
    assert result == []
