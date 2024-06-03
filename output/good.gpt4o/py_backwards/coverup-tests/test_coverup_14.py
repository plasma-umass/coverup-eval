# file py_backwards/transformers/dict_unpacking.py:8-14
# lines [8, 9, 10, 11, 12, 13, 14]
# branches ['12->13', '12->14']

import pytest
from py_backwards.transformers.dict_unpacking import merge_dicts

def test_merge_dicts(mocker):
    # Mock the snippet decorator to ensure the function is callable
    mocker.patch('py_backwards.transformers.dict_unpacking.snippet', lambda x: x)

    # Define the function to be tested
    def _py_backwards_merge_dicts(dicts):
        result = {}
        for dict_ in dicts:
            result.update(dict_)
        return result

    # Test case 1: Merging two dictionaries
    dicts = [{'a': 1}, {'b': 2}]
    expected_result = {'a': 1, 'b': 2}
    assert _py_backwards_merge_dicts(dicts) == expected_result

    # Test case 2: Merging dictionaries with overlapping keys
    dicts = [{'a': 1}, {'a': 2, 'b': 3}]
    expected_result = {'a': 2, 'b': 3}
    assert _py_backwards_merge_dicts(dicts) == expected_result

    # Test case 3: Merging empty list of dictionaries
    dicts = []
    expected_result = {}
    assert _py_backwards_merge_dicts(dicts) == expected_result

    # Test case 4: Merging list with one empty dictionary
    dicts = [{}]
    expected_result = {}
    assert _py_backwards_merge_dicts(dicts) == expected_result

    # Test case 5: Merging list with multiple empty dictionaries
    dicts = [{}, {}]
    expected_result = {}
    assert _py_backwards_merge_dicts(dicts) == expected_result
