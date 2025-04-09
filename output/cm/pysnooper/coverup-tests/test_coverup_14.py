# file pysnooper/utils.py:90-95
# lines [90, 91, 92, 93, 95]
# branches ['91->93', '91->95']

import pytest
from pysnooper.utils import ensure_tuple
from collections import abc as collections_abc
from six import string_types

def test_ensure_tuple_with_iterable():
    iterable_input = [1, 2, 3]
    expected_output = (1, 2, 3)
    assert ensure_tuple(iterable_input) == expected_output

def test_ensure_tuple_with_string():
    string_input = "test"
    expected_output = (string_input,)
    assert ensure_tuple(string_input) == expected_output

def test_ensure_tuple_with_non_iterable():
    non_iterable_input = 42
    expected_output = (non_iterable_input,)
    assert ensure_tuple(non_iterable_input) == expected_output

def test_ensure_tuple_with_dict():
    dict_input = {'a': 1, 'b': 2}
    expected_output = ('a', 'b')  # Corrected to match the keys of the dict as a tuple
    assert ensure_tuple(dict_input) == expected_output

def test_ensure_tuple_with_set():
    set_input = {1, 2, 3}
    expected_output = tuple(set_input)
    assert ensure_tuple(set_input) == expected_output
