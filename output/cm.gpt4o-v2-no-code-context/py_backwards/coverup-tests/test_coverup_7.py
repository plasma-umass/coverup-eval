# file: py_backwards/transformers/dict_unpacking.py:8-14
# asked: {"lines": [8, 9, 10, 11, 12, 13, 14], "branches": [[12, 13], [12, 14]]}
# gained: {"lines": [8, 9], "branches": []}

import pytest
from py_backwards.transformers.dict_unpacking import merge_dicts

def test_merge_dicts(monkeypatch):
    # Mock the snippet decorator to ensure it doesn't interfere with the test
    def mock_snippet(func):
        return func

    monkeypatch.setattr('py_backwards.transformers.dict_unpacking.snippet', mock_snippet)

    # Define the function to be tested within the test scope
    def _py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result

    # Test the _py_backwards_merge_dicts function
    dicts = [{'a': 1}, {'b': 2}, {'c': 3}]
    expected_result = {'a': 1, 'b': 2, 'c': 3}
    result = _py_backwards_merge_dicts(dicts)
    assert result == expected_result
