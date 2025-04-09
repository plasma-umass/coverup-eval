# file flutils/namedtupleutils.py:32-90
# lines [32, 90]
# branches []

import pytest
from collections import namedtuple, OrderedDict
from types import SimpleNamespace
from flutils.namedtupleutils import to_namedtuple

def test_to_namedtuple_with_various_types(mocker):
    # Mock the _to_namedtuple function to track its calls
    mock_to_namedtuple = mocker.patch('flutils.namedtupleutils._to_namedtuple')

    # Test with a list
    test_list = [1, 2, 3]
    to_namedtuple(test_list)
    mock_to_namedtuple.assert_called_once_with(test_list)

    # Reset mock for the next test
    mock_to_namedtuple.reset_mock()

    # Test with a tuple
    test_tuple = (1, 2, 3)
    to_namedtuple(test_tuple)
    mock_to_namedtuple.assert_called_once_with(test_tuple)

    # Reset mock for the next test
    mock_to_namedtuple.reset_mock()

    # Test with a dict
    test_dict = {'a': 1, 'b': 2}
    to_namedtuple(test_dict)
    mock_to_namedtuple.assert_called_once_with(test_dict)

    # Reset mock for the next test
    mock_to_namedtuple.reset_mock()

    # Test with an OrderedDict
    test_ordered_dict = OrderedDict([('a', 1), ('b', 2)])
    to_namedtuple(test_ordered_dict)
    mock_to_namedtuple.assert_called_once_with(test_ordered_dict)

    # Reset mock for the next test
    mock_to_namedtuple.reset_mock()

    # Test with a SimpleNamespace
    test_simple_namespace = SimpleNamespace(a=1, b=2)
    to_namedtuple(test_simple_namespace)
    mock_to_namedtuple.assert_called_once_with(test_simple_namespace)

    # Reset mock for the next test
    mock_to_namedtuple.reset_mock()

    # Test with a namedtuple
    TestNamedTuple = namedtuple('TestNamedTuple', 'a b')
    test_namedtuple = TestNamedTuple(a=1, b=2)
    to_namedtuple(test_namedtuple)
    mock_to_namedtuple.assert_called_once_with(test_namedtuple)

    # No need to reset mock as this is the last test
